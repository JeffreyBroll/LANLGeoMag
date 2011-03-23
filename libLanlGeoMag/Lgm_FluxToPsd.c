#ifdef HAVE_CONFIG_H
#include "config.h"
#endif
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "Lgm/Lgm_FluxToPsd.h"
#include "Lgm/Lgm_CTrans.h"
#include "Lgm/Lgm_MagModelInfo.h"
#include "Lgm/Lgm_DynamicMemory.h"



// Routines for converting between Flux and Phase Space Density





/**
 *     Computes relativisitic first adiabatic invariant, \f$\mu\f$, given: Particle's
 *     kinetic energy \f$E_k\f$, Pitch Angle \f$\alpha\f$, the local B-field strength \f$B\f$, and the
 *     particle's rest energy \f$E_\circ\f$. The relationship is:
 *
 *      \f[\mu = {p_\perp^2\over 2 m_\circ B}\f].
 *
 *      Since, 
 *
 *            \f[ p^2c^2 = E_k^2 + 2 E_k E_\circ \f]
 *
 *      we have,
 *
 *          \f{eqnarray*}{
 *              \mu = {p_\perp^2 \over 2 m_\circ B } &=& {p^2c^2\over (2 m_\circ c^2 B)} \sin^2(\alpha) \\
 *                                                   &=& {p^2c^2\over (2 E_\circ B)} \sin^2(\alpha) \\
 *                                                   &=& {E_k\over B}\left[1+{E_k \over 2 E_\circ}\right] \sin^2(\alpha)
 *          \f}
 *      
 *      \param[in]        Ek    Kinetic Energy of Particle.    <b>( MeV )</b>
 *      \param[in]        E0    Rest mass of Particle.         <b>( MeV )</b>
 *      \param[in]        a     Pitch Angle of Particle.       <b>( Degrees )</b>
 *      \param[in]        B     Local magnetic field strength. <b>( nT )</b>
 *
 *      \return           First adiabatic invariant, Mu. <b>( MeV/G )</b>
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 */
double  Lgm_Ek_to_Mu( double Ek, double a, double B, double E0 ) {

    double  sa, sa2, mu;

    if ( B <= 1e-12 ) return( 9e99 );

    sa = sin( a*RadPerDeg );    // sin(Alpha)
    sa2 = sa*sa;                // sin^2(Alpha)
    
    mu = Ek*(1.0+0.5*Ek/E0)*sa2*nT_Per_Gauss/B;
    
    return( mu ); 
    
}



/**
 * Returns Particle's Kinetic Energy, Ek, given: Particle's relativistic first
 * invariant, Mu, Pitch Angle and the local B-field strength and rest energy.
 *  
 *        \param[in]  Mu Kinetic Energy of Particle.    <b>( MeV/G )</b>
 *        \param[in]  a  Pitch Angle of Particle.       <b>( Degrees )</b>
 *        \param[in]  B  Local magnetic field strength. <b>( nT )</b>
 *
 *        \return     First adiabatic invariant, Mu. <b>( MeV )</b>
 */
double  Lgm_Mu_to_Ek( double Mu, double a, double B, double E0 ) {

    double  sa, sa2, Ek;

    if ( a < 0.0 ) return( -9e99 );
    
    sa = sin( a*RadPerDeg );    // sin(Alpha)
    sa2 = sa*sa;                // sin^2(Alpha)

    if ( sa2 < 1e-12 ) {
        return( 9e99 );
    } else {
        Ek = sqrt( 2*E0*B*Mu/(sa2*nT_Per_Gauss) + E0*E0) - E0;
        return( Ek );
    }


}


/**
 * Compute \f$ p^2c^2 \f$  given a particle's kinetic energy and rest energy.
 *
 *  Some relativistic equations:
 *  
 *  With,
 *          \f{eqnarray*}{
 *                  m       &=& \mbox{Particle mass.}\\
 *                  m_\circ &=& \mbox{Particle rest mass.}\\
 *                  v       &=& \mbox{Particle speed.}\\
 *                  c       &=& \mbox{Speed of Light.}\\
 *                  \gamma  &=& (1-v^2/c^2)^{-1/2}.\\
 *
 *          \f}
 *
 *      \f[ 
 *          m = m_\circ \gamma = m_\circ (1-v^2/c^2)^{-1/2} 
 *      \f]
 *
 *  Rearrange this to get,
 *      \f[ 
 *          (mc^2)^2 = (m_\circ c^2)^ + p^2c^2
 *      \f]
 *
 *  With,
 *          \f{eqnarray*}{
 *              E  = mc^2             &=& \mbox{Total Energy of particle} \\
 *              E_\circ = m_\circ c^2 &=& \mbox{Rest Energy of particle} \\
 *              p                     &=& \mbox{relativistic momentum of particle}
 *          \f}
 *
 *  this is,
 *      \f[ 
 *          E^2 = E_\circ^2 + (pc)^2
 *      \f]
 *  
 *  so, 
 *      \f[ 
 *          p^2c^2  = E^2 - E_\circ^2
 *      \f]
 *  
 *  Let \f$ E = E_k+E_\circ \f$ (kinetic energy + rest energy). Then,
 *          \f{eqnarray*}{
 *              p^2c^2  &=& (E_k+E_\circ)^2 - E_\circ^2 \\
 *                      &=& E_k (E_k+2E_\circ)
 *          \f}
 *  
 *
 *      \param[in]    E    Kinetic Energy of Particle.    <b>( MeV )</b>
 *      \param[in]    E0 (\f$ = E_\circ) \f$ Rest energy of Particle.       <b>( MeV )</b>
 *
 *      \return       p2c2 (\f$ = p^2c^2 = E_k(E_k+2E_\circ)\f$)     <b>( MeV^2 )</b>
 */
double  Lgm_p2c2( double Ek, double E0 ) {
    return( Ek*(Ek+2.0*E0) );    // p^2c^2 in units of MeV^2
}


/**
 * returns \f$ (v/c)^2 \f$ as a function of Ek and E0 using the following relation,
 *
 *          \f{eqnarray*}{
 *              (v/c)^2 &=& m^2v^2/(m^2c^2) \\
 *                      &=& m^2v^2c^2/(m^2c^4) \\
 *                      &=& p^2c^2/(m^2c^4) \\
 *                      &=& p^2c^2/E^2 \\
 *                      &=& {E_k(E_k+2E_\circ) \over (E_k+E_\circ)^2}
 *          \f}
 */
double  Lgm_v2overc2( double Ek, double E0 ) {
    double  E = Ek + E0;
    return( Ek*(Ek+2.0*E0)/(E*E) );    // dimensionless
}


/**
 *   Returns relativistic factor \f$ \gamma = [ 1 - (v/c)^2 ]^{-1/2} \f$
 *   Note that \f$ (v/c)^2 = E_k(E_k+2E_\circ)/(E_k+E_\circ)^2 \f$ (see Lgm_v2overc2().)
 */
double  Lgm_gamma( double Ek, double E0 ) {
    double  E = Ek + E0;
    return( 1.0/sqrt( 1.0 - Ek*(Ek+2.0*E0)/(E*E) ) );    // dimensionless
}


/**
 *  Convert differential flux to phase space density.
 *
 *  The basic relationship is;
 *      \f[
 *      f = {j \over p^2}
 *      \f]
 *
 *  Multiply top and bottom by \f$ c^2 \f$ gives,
 *      \f{eqnarray*}{
 *          f &=& {j c^2 \over p^2c^2 } \\
 *          f &=& { j\over c } {c^3 \over (p^2c^2)}
 *      \f}
 *  
 *  The reason for making it \f$ c^3 \f$ is that the final units simplify to,
 *  \f$ c^3 \mbox{cm}^{-3} \mbox{MeV}^{-3}\f$ or \f$ \left[c\over \mbox{cm} \mbox{MeV}\right]^3 \f$
 *
 *     \param[in]     j    Differential Flux in units of <b>#/cm^2/s/sr/MeV</b>
 *     \param[in]     p2c2 (\f$ = p^2 c^2\f$) in units of <b>Mev^2</b>
 *  
 *      \return       f, Phase space density in units of <b>(c/cm/MeV)^3</b>
 *  
 */
double Lgm_DiffFluxToPsd( double j, double p2c2 ){
    return( j/(p2c2*2.9979e10) ); // f in units of (c/cm/MeV)^3
}




/**
 * Convert phase space density to differential flux.
 *
 *  The basic relationship is;
 *      \f[
 *      f = j/p^2
 *      \f]
 *
 *  Multiply top and bottom by \f$ c^2 \f$ gives,
 *      \f{eqnarray*}{
 *          f &=& {j c^2 \over p^2c^2 } \\
 *          f &=& { j\over c } {c^3 \over (p^2c^2)}
 *      \f}
 *  
 *  The reason for making it \f$ c^3 \f$ is that the final units simplify to,
 *  \f$ c^3 \mbox{cm}^{-3} \mbox{MeV}^{-3}\f$ or \f$ \left[c\over \mbox{cm} \mbox{MeV}\right]^3 \f$
 *
 *     \param[in]     f    Phase space density in units of <b>(c/cm/MeV)^3</b>
 *     \param[in]     p2c2 (\f$ = p^2 c^2\f$) in units of  <b>Mev^2</b>
 *  
 *      \return       j, Differential Flux in units of     <b>#/cm^2/s/sr/MeV</b>

 *
 */
double Lgm_PsdToDiffFlux( double f, double p2c2 ){
    return( f*2.9979e10/p2c2 ); // j in units of #/cm^2/s/sr/MeV
}



/**
 * Create a calloc'd Lgm_FluxToPsd structure.
 *
 *  \param[in] DumpDiagnostics  Boolean flag to turn on/off dumping of diagnostics.
 *  \return    A pointer to an allocated and initialized Lgm_FluxToPsd stucture.
 *
 *  You must destroy this with Lgm_FreeFluxToPsd() when you are done.
 *
 */
Lgm_FluxToPsd *Lgm_CreateFluxToPsd( int DumpDiagnostics ) {

    Lgm_FluxToPsd *f;

    /*
     * Allocate memory for a Lgm_PhaseSpaceDensity structure.
     */
    f = (Lgm_FluxToPsd *) calloc( 1, sizeof(*f) );

    /*
     * Set DumpDiagnostics flag to what we got here. This can be changed later as well.
     */
    f->DumpDiagnostics = DumpDiagnostics;

    f->Alloced1 = FALSE;
    f->Alloced2 = FALSE;


    return f;

}

/**
 * Destroy a Lgm_FluxToPsd structure.
 *
 *  \param f  Pointer to the allocated Lgm_FluxToPsd structure that you want to destroy.
 *
 */
void Lgm_FreeFluxToPsd( Lgm_FluxToPsd *f ) {

    if ( f->Alloced1 ) {
        LGM_ARRAY_1D_FREE( f->E );
        LGM_ARRAY_1D_FREE( f->A );
        LGM_ARRAY_2D_FREE( f->FLUX_EA );
        LGM_ARRAY_2D_FREE( f->PSD_EA );
    }

    if ( f->Alloced2 ) {
        LGM_ARRAY_1D_FREE( f->Mu );
        LGM_ARRAY_1D_FREE( f->K );
        LGM_ARRAY_1D_FREE( f->AofK );
        LGM_ARRAY_2D_FREE( f->EofMu );
        LGM_ARRAY_2D_FREE( f->PSD_MK );
    }

    free( f );

    return;
}


/**
 *  Set Date/Time and position in the Lgm_FluxToPsd structure.
 *      
 *     
 *      \param[in]          d   Date/Time of measurement.
 *      \param[in]          u   Position of measurment.
 *      \param[in,out]      f   Lgm_FluxToPsd sturcture.
 */
void Lgm_FluxToPsd_SetDateTimeAndPos( Lgm_DateTime *d, Lgm_Vector *u, Lgm_FluxToPsd *f ) {

    f->DateTime = *d;
    f->Position = *u;

}


/**
 *     Adds (to a Lgm_FluxToPsd structure) the user-supplied arrays containing J[Energy][Alpha],  Energy[], Alpha[]
 *
 *    \param[in]      J                 2D array containing the differential flux values as a function of energy and pitch angle.
 *    \param[in]      E                 1D array containing the energy values implied by the first index of Flux[][] array.
 *    \param[in]      nE                number of energies.
 *    \param[in]      A                 1D array containing the pitch angles values implied by the second index of Flux[][] array.
 *    \param[in]      nA                number of pitch angles.
 *    \param[in,out]  f                 Lgm_FluxToPsd sturcture.
 *
 */
void Lgm_FluxToPsd_SetFlux( double **J, double *E, int nE, double *A, int nA, Lgm_FluxToPsd *f ) {

    
    int     i, j;
    double  flux, p2c2, fp, Min, Max;


    /*
     * If arrays are already alloc'd, free them first
     */
    if ( f->Alloced1 ) {
        LGM_ARRAY_1D_FREE( f->E );
        LGM_ARRAY_1D_FREE( f->A );
        LGM_ARRAY_2D_FREE( f->FLUX_EA );
        LGM_ARRAY_2D_FREE( f->PSD_EA );
    }


    /*
     * Add Flux array to f structure. Alloc arrays appropriately.
     */
    f->nE = nE; 
    f->nA = nA; 
    LGM_ARRAY_1D( f->E, f->nE, double );
    LGM_ARRAY_1D( f->A, f->nA, double );
    LGM_ARRAY_2D( f->FLUX_EA, f->nE, f->nA, double );
    for (i=0; i<f->nE; i++) f->E[i] = E[i];
    for (i=0; i<f->nA; i++) f->A[i] = A[i];
    for (i=0; i<f->nE; i++) {
        for (j=0; j<f->nA; j++) {
            f->FLUX_EA[i][j] = J[i][j]; // FLUX_EA is "Flux versus Energy and Pitch Angle".
        }
    }
    if ( f->DumpDiagnostics ) {
        DumpGif( "Lgm_FluxToPsd_SetFlux_FLUX_EA.gif", f->nA, f->nE, f->FLUX_EA );
    }


    /*
     * Alloc mem for the PSD array.
     * Convert Flux array into to PSD array.
     * Note, the result here is not PSD at constant Mu and K, it is PSD at the
     * same Es and Alphas we started with.
     */
    LGM_ARRAY_2D( f->PSD_EA, f->nE, f->nA, double );
    for (j=0; j<f->nA; j++) {
        for (i=0; i<f->nE; i++) {
            flux   = f->FLUX_EA[i][j];
            p2c2   = Lgm_p2c2( f->E[i], LGM_Ee0 );
            fp     = Lgm_DiffFluxToPsd( flux, p2c2 );
            f->PSD_EA[i][j] = fp; // PSD_EA is "PSD versus Energy and Pitch Angle".
        }
    }
    if ( f->DumpDiagnostics ) {
        DumpGif( "Lgm_FluxToPsd_SetFlux_PSD_EA.gif", f->nA, f->nE, f->PSD_EA );
    }

    f->Alloced1 = TRUE;
   
    return;

}




/**
 *  The routine Lgm_FluxPsd_SetFlux() gives us an  array of f(E, Alpha).  BUT,
 *  what we really need in the end is f( mu, K ). Although mu is easy to
 *  compute, it is dependant on both E and Alpha. K is only dependant upon
 *  Alpha, but on the other hand K is not so easy to compute from Alpha.
 * 
 *  Note that f( E, a ) is the same as f( E(mu, a(K)), a(K) ). Thus, for a
 *  given mu and K, we can figure out what E and a they correspond to and then
 *  we can just use the f(E, a) array to compute the desired f values. The
 *  steps are;
 *
 *      1. For each K, compute Alpha(K). We already have this routine ( AlphaOfK() ).
 *
 *      2. Then we compute E from Alpha and the given mu and Alpha values.
 *
 *      3. Then just look up f(E,Alpha) from the array (interp or fit or whatever).
 *
 *  Inputs:
 *          nMu -- Number of Mu values
 *           Mu -- 1-D array of Mu values
 *           nK -- Number of K values
 *            K -- 1-D array of K values
 *
 *  Outputs:
 *          PSD -- 2-D array of f(Mu, K). The user must alloc memory for this array.
 * 
 *  Usage:
 * 
 * 
 */
void Lgm_FluxPsd_GetPsdAtConstMusAndKs( double *Mu, int nMu, double *K, int nK, Lgm_FluxToPsd *f ) {

    int                 k, m;
    double              AlphaEq, SinA;
    Lgm_MagModelInfo    *mInfo;

    /*
     * Init mInfo
     */
    mInfo = Lgm_InitMagInfo();

    /*
     * If arrays are already alloc'd, free them first
     */
    if ( f->Alloced2 ) {
        LGM_ARRAY_1D_FREE( f->Mu );
        LGM_ARRAY_1D_FREE( f->K );
        LGM_ARRAY_1D_FREE( f->AofK );
        LGM_ARRAY_2D_FREE( f->EofMu );
        LGM_ARRAY_2D_FREE( f->PSD_MK );
    }
    
    f->nMu = nMu; 
    f->nK  = nK; 
    LGM_ARRAY_1D( f->Mu,    f->nMu, double );
    LGM_ARRAY_1D( f->K,     f->nK,  double );
    LGM_ARRAY_1D( f->AofK,  f->nK,  double );
    LGM_ARRAY_2D( f->EofMu, f->nMu,  f->nK,  double );

    /*
     * Copy K's into f structure.
     * Transform the K's into Alpha's using Lgm_AlphaOfK().
     * Save the results in the f structure.
     */
    Lgm_Setup_AlphaOfK( &(f->DateTime), &(f->Position), mInfo );
    f->B = mInfo->Blocal;
    for ( k=0; k<nK; k++ ){
        f->K[k]    = K[k];
        AlphaEq    = Lgm_AlphaOfK( f->K[k], mInfo ); // Lgm_AlphaOfK() returns equatorial pitch angle.
        SinA       = sqrt( mInfo->Blocal/mInfo->Bmin ) * sin( RadPerDeg*AlphaEq );
        if ( AlphaEq > 0.0 ) {
            if ( SinA <= 1.0 ) {
                f->AofK[k] = DegPerRad*asin( SinA );
            } else {
                f->AofK[k] = -9e99;
                //printf("Particles with Eq. PA of %g mirror below us. (I.e. S/C does not see K's this low).\n");
            }
        } else {
            f->AofK[k] = -9e99;
            //printf("Particles mirror below LC height. (I.e. S/C does not see K's this high).\n");
        }
        printf("f->K[k] = %g   AlphaEq = %g SinA = %g f->AofK[k] = %g\n\n", f->K[k], AlphaEq, SinA, f->AofK[k]);
    }
    Lgm_TearDown_AlphaOfK( mInfo );


    /*
     * Copy Mu's into f structure.
     * Transform the Mu's into (Kinetic) Energies.
     * Save the results in the f structure.
     * Note that since this conversion involves Mu and Alpha, the result is 2D.
assumes electrons -- generalize this...
     */
    for ( m=0; m<nK; m++ ){
        f->Mu[m] = Mu[m];
        for ( k=0; k<nK; k++ ){
            f->EofMu[m][k] = Lgm_Mu_to_Ek( f->Mu[m], f->AofK[k], f->B, LGM_Ee0 );
            printf("f->Mu[%d], f->AofK[%d], f->B, f->EofMu[%d][%d] = %g %g %g %g\n", m, k, m, k, f->Mu[m], f->AofK[k], f->B, f->EofMu[m][k]);
        }
    }


    /*
     * Now, from the PSD[E][a] array, get PSD at the E's and Alpha's we just computed.
     * The result will be the same as PSD at the given Mu's and K's
     */
    LGM_ARRAY_2D( f->PSD_MK, f->nMu,  f->nK,  double );
    for ( m=0; m<nK; m++ ){
        for ( k=0; k<nK; k++ ){
            f->PSD_MK[m][k] =  Lgm_FluxPsd_GetPsdAtEandAlpha( f->EofMu[m][k], f->AofK[k], f );
        }
    }


    Lgm_FreeMagInfo( mInfo );

    f->Alloced2 = TRUE;

    return;

}

double Cost( double *x, int *data ){


    return(0.0);

}



/**
 * The f structure should have an initialized PSD[E][a] array in it.
 * This routine computes psd given a value of E and a.
 */
double  Lgm_FluxPsd_GetPsdAtEandAlpha( double E, double a, Lgm_FluxToPsd *f ) {

    int     j, i, i0, i1;
    double  a0, a1, y0, y1, slp, *g, psd;

    // if a < 0, we should return fill value.
    if ( a < 0.0 ) return(-9e99);

    /*
     * Since pitch angle, a is bounded (here its constrained to be between 0
     * and 90), we will interpolate on that first to produce a 1D array of
     * f(E).
     */
    if ( a < f->A[0] ) {
        i0 = 0; i1 = 1;
    } else if ( a > f->A[f->nA - 1] ) {
        i0 = f->nA - 2; i1 = f->nA - 1;
    } else {
        for (i=1; i<f->nA; i++) {
            if ( a < f->A[i] ) {
                i0 = i-1; i1 = i;
                break;
            }
        }
    }
    //printf("i0, i1 = %d %d\n", i0, i1);


    // interpolate PA
    LGM_ARRAY_1D( g, f->nE, double );
    for (j=0; j<f->nE; ++j){
        a0   = f->A[i0];
        a1   = f->A[i1];
        y0   = f->PSD_EA[j][i0];
        y1   = f->PSD_EA[j][i1];
        slp  = (y1-y0)/(a1-a0);
        g[j] = slp*(a-a0) + y0;
        //printf("a = %g, g[%d] = %g\n", a, j, g[j]);
    }


    // interpolate/fit E
    // for now just do a linear interp.
    // no lets try a fit...
    double  in[10], out[7], x[3];
    in[0] = 1e-8;
    in[1] = in[2] = 1e-9; //Info->Praxis_Tolerance;
    in[5] = 30000.0; //(double)Info->Praxis_Max_Function_Evals;
    in[6] = 10.0; //Info->Praxis_Maximum_Step_Size;
    in[7] = 10.0; //Info->Praxis_Bad_Scale_Paramater;
    in[8] = 4.0; //(double)Info->Praxis_Max_Its_Without_Improvement;
    in[9] = 1.0; //(double)Info->Praxis_Ill_Conditioned_Problem;
    praxis( 2, x, (int *)g, Cost, in, out);
printf("out[2] = %g\n", out[2]);

FILE *fp;
printf("E = %g\n", E);
fp = fopen("data.txt", "w");
for (j=0; j<f->nE; ++j){
fprintf(fp, "%g %g\n", f->E[j], g[j]);
}
fclose(fp);
    
exit(0);
    

    
    

    LGM_ARRAY_1D_FREE( g );

printf("psd = %g\n", psd);

    return( psd );

}




/*
 *  Reverse direction....
 *
 *  Note that f( mu, K ) is the same as f( mu( E, a), K(a) ). Thus, for a given
 *  E and a, we can figure out what mu and K they correspond to and then we
 *  can just look up the f value in our HiRes array. The steps would be;
 *
 *      1. For each a, compute K(a). We already have this routine somewhere.
 *
 *      2. Also compute mu from the given E and a.
 *
 *      3. Then just look f( mu, K ) up from the array (interp or fit or whatever).
 * 
 */












/**
 * Routine to increase the size of an image smoothly. Uses an area-weighting
 * interpolation scheme.
 */
void UpSizeImage( double **Orig, double *X, double *Y, int M, int N, double **New, double *U, double *V, int K, int J ) {

    double  DX, DY, DXO2, DYO2, A;
    double  x, y, xe, ye, xx, yy, xp, yp;
    double  f[4], w0, w1, w2, w3;
    double  dxm, dxp, dym, dyp;
    int     j, k, np, mp, ne, me;
    int     n0, n1, n2, n3;
    int     m0, m1, m2, m3;



    /*
     * compute size and area of a pixel in orig image.
     */
    DX = 1.0/(double)N;
    DY = 1.0/(double)M;
    DXO2 = 0.5*DX;
    DYO2 = 0.5*DY;
    A    = DX*DY;
    printf("A = %g\n", A);


    for (j=0; j<J; j++ ){
        for (k=0; k<K; k++ ){


            /*
             *  Compute the normalized coords (x,y) for the center of this
             *  pixel.
             */
            x = ((double)j+0.5)/(double)J;
            y = ((double)k+0.5)/(double)K;



            /*
             *  Determine which pixel of the original image we are in.
             */
            np = (int)(x*N);
            mp = (int)(y*M);
            xp = ((double)np+0.5)/(double)N;
            yp = ((double)mp+0.5)/(double)M;



            /*
             *  Find the edges in the original image that this pixel is closest to.
             */
            ne = (int)(x*N + 0.5);
            me = (int)(y*M + 0.5);
            xe = (double)ne/(double)N;
            ye = (double)me/(double)M;




            /*
             * Compute coords of the four closest pixels
             */
            //if        ( ( np < ne ) && ( mp < me ) ){  // we are in upper left  Pix #0
            if        ( ( x > xp ) && ( y > yp ) ){  // we are in upper left  Pix #0
                n0 = np;   m0 = mp;
                n1 = np+1; m1 = mp;
                n2 = np+1; m2 = mp+1;
                n3 = np;   m3 = mp+1;
            //} else if ( ( np > ne ) && ( mp < me ) ){  // we are in upper right Pix #1
            } else if ( ( x < xp ) && ( y > yp ) ){  // we are in upper right Pix #1
                n0 = np-1; m0 = mp;
                n1 = np;   m1 = mp;
                n2 = np;   m2 = mp+1;
                n3 = np-1; m3 = mp+1;
            //} else if ( ( np > ne ) && ( mp > me ) ){  // we are in lower right Pix #2
            } else if ( ( x < xp ) && ( y < yp ) ){  // we are in lower right Pix #2
                n0 = np-1; m0 = mp-1;
                n1 = np;   m1 = mp-1;
                n2 = np;   m2 = mp;
                n3 = np-1; m3 = mp;
            } else {                                   // we are in lower left  Pix #3
                n0 = np;   m0 = mp-1;
                n1 = np+1; m1 = mp-1;
                n2 = np+1; m2 = mp;
                n3 = np;   m3 = mp;
            }

  xe = 0.5*(n0+n1+1.0)/(double)N;
  ye = 0.5*(m1+m2+1.0)/(double)M;



            /*
             *  Check for edge problems
             */
            if (n0 < 0)   n0 = 0;
            if (n3 < 0)   n3 = 0;
            if (n1 > N-1) n1 = N-1;
            if (n2 > N-1) n2 = N-1;

            if (m0 < 0)     m0 = 0;
            if (m1 < 0)     m1 = 0;
            if (m2 > M-1)   m2 = M-1;
            if (m3 > M-1)   m3 = M-1;

            

            /*
             * Extract the pixel vals.
             */
            f[0] = Orig[ m0 ][ n0 ];
            f[1] = Orig[ m1 ][ n1 ];
            f[2] = Orig[ m2 ][ n2 ];
            f[3] = Orig[ m3 ][ n3 ];



            /*
             *  Compute (x',y') (i.e. the coords relative to center of 4 pixels.)
             */
            xx = x - xe;
            yy = y - ye;



            /*
             *  Compute weights (i.e. overlapping areas)
             */
            dxm = DXO2 - xx;
            dxp = DXO2 + xx;
            dym = DYO2 - yy;
            dyp = DYO2 + yy;
//if (dxm < 0.0) { printf("dxm = %g\n", dxm); exit(0); }
//if (dxp < 0.0) { printf("dxp = %g\n", dxp); exit(0); }
//if (dym < 0.0) { printf("dym = %g    DYO2 = %g  x, y = %g %g   xx, yy = %g %g\n", dym, DYO2, x, y, xx, yy); exit(0); }
//if (dyp < 0.0) { printf("dyp = %g\n", dyp); exit(0); }

            w0 = dxm*dym;
            w1 = dxp*dym;
            w2 = dxp*dyp;
            w3 = dxm*dyp;
            /*
            w0=0.1;
            w1=0.2;
            w2=0.3;
            w3=0.4;
            */

if ((j==189)&&(k==118)) {
                printf("np,mp = %d %d    pixels:  %d %d   %d %d   %d %d   %d %d\n", np, mp, n0, m0, n1, m1, n2, m2, n3, m3);
                printf("j,k = %d %d     f = %g %g %g %g     w = %g %g %g %g     xp, yp = %g %g   x,y = %g %g    xx, yy = %g %g\n", j, k, f[0], f[1], f[2], f[3], w0, w1, w2, w3, xp, yp, x, y, xx, yy);
}

            /*
             *  Finally compute weighted average and assign to current pixel of new image.
             *  A is the total area of an original pixel. w's are the partial overlap areas.
             */
            New[k][j] = (f[0]*w0 + f[1]*w1 + f[2]*w2 + f[3]*w3)/A;
            //New[k][j] = (f[0]*w0 + f[1]*w1 )/A;
            //New[k][j] = (f[0]*w0 )/A;
            //New[k][j] = (double)k;


        }
    }






}

/**
 *   Routine to write out a GIF image
 */
void DumpGif( char *Filename, int W, int H, double **Image ){

    double           Val, Min, Max;
    int              w, h;
    unsigned char   *uImage, uVal;
    FILE            *fp_gif;

    int             LogScale;

    LogScale = FALSE;
    LogScale = TRUE;


    // Determine Min/Max values...
    Min =  9e99;
    Max = -9e99;
    for ( w=0; w<W; w++ ){
        for ( h=0; h<H; h++ ) {

            if ( LogScale ) {
                Val = Image[h][w] > 0.0 ? log10( Image[h][w] ) : -9e99;
            } else {
                Val = Image[h][w];
            }
            if (Val > Max) Max = Val;
            if ((Val < Min)&&(Val > -1e99)) Min = Val;

        }
    }

    printf("Min, Max = %g %g\n", Min, Max);




    uImage = (unsigned char *)calloc( W*H, sizeof(unsigned char) );

    for ( w=0; w<W; w++ ){
        for ( h=0; h<H; h++ ) {

            if ( LogScale ) {
                Val = Image[h][w] > 0.0 ? log10( Image[h][w] ) : -9e99;
            } else {
                Val = Image[h][w];
            }
            if ( Val < -1e99 ) {
                uVal = 0;
            } else {
                uVal = (unsigned char)( (Val - Min)/(Max-Min)*255.0 );
            }
            *(uImage + W*(H-1-h) + w) = uVal;

        }
    }

    fp_gif = fopen(Filename, "w");
    WriteGIF(fp_gif, (byte *)uImage, 0, W, H, Rainbow2_Red, Rainbow2_Grn, Rainbow2_Blu, 256, 0, "");
    fclose(fp_gif);

    free( uImage );



}








