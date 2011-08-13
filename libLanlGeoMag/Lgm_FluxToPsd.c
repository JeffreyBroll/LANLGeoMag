#ifdef HAVE_CONFIG_H
#include "config.h"
#endif
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include "Lgm/Lgm_FluxToPsd.h"
#include "Lgm/Lgm_CTrans.h"
#include "Lgm/Lgm_MagModelInfo.h"
#include "Lgm/Lgm_DynamicMemory.h"




typedef struct _FitData { 

    int     n;
    double  *E;
    double  *g;

} _FitData;



// Routines for converting between Flux and Phase Space Density





/**
 *  \brief
 *     Computes relativisitic first adiabatic invariant.
 *  \details
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
 *      \param[in]      Ek  Kinetic Energy of Particle.     <b>( MeV )</b>
 *      \param[in]      a   Pitch Angle of Particle.        <b>( Degrees )</b>
 *      \param[in]      B   Local magnetic field strength.  <b>( nT )</b>
 *      \param[in]      E0  Rest mass of Particle.          <b>( MeV )</b>
 *
 *      \return         First adiabatic invariant, Mu.      <b>( MeV/G )</b>
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
 * Returns Particle's Kinetic Energy, \f$E_k\f$, given: Particle's relativistic
 * first invariant, \f$\alpha\f$, Pitch Angle \f$\alpha\f$ and the local
 * B-field strength and rest energy. This is the inverse of Lgm_Ek_to_Mu(). See
 * description of Lgm_Ek_to_Mu() for more details on the equations used.
 *  
 *      \param[in]      Mu  First adiabatic invariant.      <b>( MeV/G )</b>
 *      \param[in]      a   Pitch Angle of Particle.        <b>( Degrees )</b>
 *      \param[in]      B   Local magnetic field strength.  <b>( nT )</b>
 *      \param[in]      E0  Rest mass of Particle.          <b>( MeV )</b>
 *
 *      \return         First adiabatic invariant, Mu.      <b>( MeV )</b>
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
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
 *      \param[in]      Ek (\f$ = E_k) \f$  Kinetic Energy of Particle.   <b>( MeV )</b>
 *      \param[in]      E0 (\f$ = E_\circ) \f$ Rest energy of Particle.   <b>( MeV )</b>
 *
 *      \return         p2c2 (\f$ = p^2c^2 = E_k(E_k+2E_\circ)\f$)        <b>( MeV^2 )</b>
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 */
double  Lgm_p2c2( double Ek, double E0 ) {
    return( Ek*(Ek+2.0*E0) );    // p^2c^2 in units of MeV^2
}


/**
 * Returns \f$ (v/c)^2 \f$ as a function of \f$E_k\f$ and \f$E_\circ\f$ using the following relation,
 *
 *          \f{eqnarray*}{
 *              (v/c)^2 &=& m^2v^2/(m^2c^2) \\
 *                      &=& m^2v^2c^2/(m^2c^4) \\
 *                      &=& p^2c^2/(m^2c^4) \\
 *                      &=& p^2c^2/E^2 \\
 *                      &=& {E_k(E_k+2E_\circ) \over (E_k+E_\circ)^2}
 *          \f}
 *
 *      \param[in]    Ek   Kinetic Energy of Particle.                  <b>( MeV )</b>
 *      \param[in]    E0 (\f$ = E_\circ) \f$ Rest energy of Particle.   <b>( MeV )</b>
 *
 *      \return       v2overc2 (\f$ = v^2/c^2)\f$)                      <b>( dimensionless )</b>
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 */
double  Lgm_v2overc2( double Ek, double E0 ) {
    double  E = Ek + E0;
    return( Ek*(Ek+2.0*E0)/(E*E) );    // dimensionless
}


/**
 *   Returns relativistic factor \f$ \gamma = [ 1 - (v/c)^2 ]^{-1/2} \f$
 *   Note that \f$ (v/c)^2 = E_k(E_k+2E_\circ)/(E_k+E_\circ)^2 \f$ (see Lgm_v2overc2().)
 *
 *      \param[in]    Ek   Kinetic Energy of Particle.                  <b>( MeV )</b>
 *      \param[in]    E0 (\f$ = E_\circ) \f$ Rest energy of Particle.   <b>( MeV )</b>
 *
 *      \return       gamma (\f$ = [ 1 - (v/c)^2 ]^{-1/2} \f$)          <b>( dimensionless )</b>
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
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
 *  Multiplying the top and bottom by \f$ c^2 \f$ gives,
 *      \f{eqnarray*}{
 *          f &=& {j c^2 \over p^2c^2 } \\
 *          f &=& { j\over c } {c^3 \over (p^2c^2)}
 *      \f}
 *  
 *  The reason for making it \f$ c^3 \f$ is that the final units simplify to,
 *  \f$ c^3 \mbox{cm}^{-3} \mbox{MeV}^{-3}\f$ or \f$ \left[c\over \mbox{cm}
 *  \mbox{MeV}\right]^3 \f$. These are the standard GEM phase space density
 *  units.
 *
 *      \param[in]      j               Differential Flux in units of   <b>#/cm^2/s/sr/MeV</b>
 *      \param[in]      p2c2 (\f$ = p^2 c^2\f$) in units of             <b>Mev^2</b>
 *  
 *      \return         f, Phase space density in units of              <b>(c/cm/MeV)^3</b>
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
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
 *      \param[in]      f    Phase space density in units of    <b>(c/cm/MeV)^3</b>
 *      \param[in]      p2c2 (\f$ = p^2 c^2\f$) in units of     <b>Mev^2</b>
 *  
 *      \return         j, Differential Flux in units of        <b>#/cm^2/s/sr/MeV</b>
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *  
 */
double Lgm_PsdToDiffFlux( double f, double p2c2 ){
    return( f*2.9979e10*p2c2 ); // j in units of #/cm^2/s/sr/MeV
}



/**
 *  Returns ma pointer to a dynamically allocated Lgm_FluxToPsd structure.
 *  User must destroy this with Lgm_F2P_FreeFluxToPsd() when done.
 *
 *      \param[in]      DumpDiagnostics  Boolean flag to turn on/off dumping of diagnostics.
 *      \return         A pointer to an allocated and initialized Lgm_FluxToPsd stucture.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
Lgm_FluxToPsd *Lgm_F2P_CreateFluxToPsd( int DumpDiagnostics ) {

    Lgm_FluxToPsd *f;

    /*
     * Allocate memory for a Lgm_PhaseSpaceDensity structure.
     */
    f = (Lgm_FluxToPsd *) calloc( 1, sizeof(*f) );

    /*
     * Set DumpDiagnostics flag to what we got here. This can be changed later as well.
     */
    f->DumpDiagnostics = DumpDiagnostics;

    f->Extrapolate = TRUE;

    f->Alloced1 = FALSE;
    f->Alloced2 = FALSE;


    return f;

}

/**
 * Destroy a dynamically allocated Lgm_FluxToPsd structure. (E.g. one that was
 * created by Lgm_F2P_CreateFluxToPsd().)
 *
 *      \param          f  Pointer to the allocated Lgm_FluxToPsd structure that you want to destroy.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
void Lgm_F2P_FreeFluxToPsd( Lgm_FluxToPsd *f ) {

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
 *      \param[in]      d   Date/Time of measurement.
 *      \param[in]      u   Position of measurment (in GSM).
 *      \param[in,out]  f   Lgm_FluxToPsd sturcture.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
void Lgm_F2P_SetDateTimeAndPos( Lgm_DateTime *d, Lgm_Vector *u, Lgm_FluxToPsd *f ) {

    f->DateTime = *d;
    f->Position = *u;

}


/**
 *     Adds (to a Lgm_FluxToPsd structure) the user-supplied arrays containing J[Energy][Alpha],  Energy[], Alpha[]
 *
 *      \param[in]      J                 2D array containing the differential flux values as a function of energy and pitch angle.
 *      \param[in]      E                 1D array containing the energy values implied by the first index of Flux[][] array.
 *      \param[in]      nE                number of energies.
 *      \param[in]      A                 1D array containing the pitch angles values implied by the second index of Flux[][] array.
 *      \param[in]      nA                number of pitch angles.
 *      \param[in,out]  f                 Lgm_FluxToPsd sturcture.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
void Lgm_F2P_SetFlux( double **J, double *E, int nE, double *A, int nA, Lgm_FluxToPsd *f ) {

    
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
        DumpGif( "Lgm_FluxToPsd_FLUX_EA", f->nA, f->nE, f->FLUX_EA );
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
        DumpGif( "Lgm_FluxToPsd_PSD_EA", f->nA, f->nE, f->PSD_EA );
    }

    f->Alloced1 = TRUE;
   
    return;

}




/**
 *  Computes Phase Space Density at user-supplied constant values of \f$\mu\f$
 *  and K.
 *
 *  This routine ( Lgm_FluxPsd_GetPsdAtConstMusAndKs() ) must operate on a
 *  pre-initialized Lgm_FluxToPsd structure.  The routine Lgm_FluxToPsd_SetFlux()
 *  is used to add differential flux data/info to an Lgm_FluxToPsd structure
 *  and it also converts the differential flux to Phase Space Density at
 *  constant E and \f$\alpha\f$ (i.e. it computes \f$ f(E, \alpha) \f$ ).
 *
 *  However, what we really want is Phase Space Density at constant \f$\mu and
 *  K\f$ (i.e. we want \f$f( \mu, K )\f$). Although \f$mu\f$ is easy to
 *  compute, it is dependant on both E and \f$\alpha\f$. K is only dependant
 *  upon \f$\alpha\f$, but on the other hand K is not so easy to compute from
 *  \f$\alpha\f$.
 * 
 *  To perform the calculation we note that \f$f( E, \alpha )\f$ is the same as
 *  \f$f( E(\mu, \alpha(K)), \alpha(K) )\f$. Thus, for a given \f$\mu\f$ and K,
 *  we can figure out what E and \f$\alpha\f$ they correspond to and then we
 *  can just use the \f$f(E, \alpha)\f$ array to compute the desired f values.
 *  The steps are;
 *
 *      - For each K, compute \f$\alpha(K)\f$. This is done with the routine
 *        Lgm_AlphaOfK().
 *
 *      - Then we compute E from \f$\alpha\f$ and the given mu and Alpha
 *        values.
 *
 *      - Then we look up \f$f(E, \alpha)\f$ from the array (interp or fit or
 *        whatever).
 *
 *      \param[in]      nMu         Number of Mu values
 *      \param[in]      Mu          1-D array of Mu values
 *      \param[in]      nK          Number of K values
 *      \param[in]      K           1-D array of K values
 *      \param[in]      Extrapolate Turns on/off extrapolation capability
 *      \param[in,out]  f           A properly pre-initialized Lgm_FluxToPsd structure.
 *
 *      \author     Mike Henderson
 *      \date       2011
 *      \warning    Still working on this code. It is not finished.
 * 
 */
void Lgm_F2P_GetPsdAtConstMusAndKs( double *Mu, int nMu, double *K, int nK, Lgm_FluxToPsd *f ) {

    int                 k, m, DoIt;
    double              AlphaEq, SinA;
    Lgm_MagModelInfo    *mInfo, *mInfo2;

    /*
     * Init mInfo
This is no good! How does user define mag model etc...?
I think there needs to be a Lgm_MagModelInfo struct in f
Then add a routine to set stuff up in there. Or just use the ones we have already....
For now we will just go with the defaults.
     */
    mInfo = Lgm_InitMagInfo();
//mInfo->Bfield = Lgm_B_edip;

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
    
    /*
     * Alloc arrays
     */
    f->nMu = nMu; 
    f->nK  = nK; 
    LGM_ARRAY_1D( f->Mu,    f->nMu, double );
    LGM_ARRAY_1D( f->K,     f->nK,  double );
    LGM_ARRAY_1D( f->AofK,  f->nK,  double );
    LGM_ARRAY_2D( f->EofMu, f->nMu,  f->nK,  double );


    /*
     * Copy K's (given in the arguments) into f structure.
     * Transform the K's into Alpha's using Lgm_AlphaOfK().
     * Save the results in the f structure.
     */

    Lgm_Setup_AlphaOfK( &(f->DateTime), &(f->Position), mInfo );
    f->B = mInfo->Blocal;
    {
        #pragma omp parallel private(mInfo2,AlphaEq,SinA)
        #pragma omp for schedule(dynamic, 1)
        for ( k=0; k<nK; k++ ){

            mInfo2 = Lgm_CopyMagInfo( mInfo );  // make a private (per-thread) copy of mInfo

            f->K[k]    = K[k];
            AlphaEq    = Lgm_AlphaOfK( f->K[k], mInfo2 ); // Lgm_AlphaOfK() returns equatorial pitch angle.
            SinA       = sqrt( mInfo2->Blocal/mInfo2->Bmin ) * sin( RadPerDeg*AlphaEq );
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
            //printf("f->K[k] = %g   AlphaEq = %g SinA = %g f->AofK[k] = %g\n", f->K[k], AlphaEq, SinA, f->AofK[k]);

            Lgm_FreeMagInfo( mInfo2 ); // free mInfo2
            

        }
    }
    Lgm_TearDown_AlphaOfK( mInfo );


    /*
     * Copy Mu's (given in the arguments) into f structure.
     * Transform the Mu's into (Kinetic) Energies.
     * Save the results in the f structure.
     * Note that since this conversion involves Mu and Alpha, the result is 2D.
assumes electrons -- generalize this...
     */
    for ( m=0; m<nMu; m++ ){
        f->Mu[m] = Mu[m];
        for ( k=0; k<nK; k++ ){
            f->EofMu[m][k] = Lgm_Mu_to_Ek( f->Mu[m], f->AofK[k], f->B, LGM_Ee0 );
            //printf("f->Mu[%d], f->K[%d], f->AofK[%d], f->B, f->EofMu[%d][%d] = %g %g %g %g %g\n", m, k, k, m, k, f->Mu[m], f->K[k], f->AofK[k], f->B, f->EofMu[m][k]);
        }
    }


    /*
     * Now, from the PSD[E][a] array, get PSD at the E's and Alpha's we just computed.
     * The result will be the same as PSD at the given Mu's and K's
     */
    LGM_ARRAY_2D( f->PSD_MK, f->nMu,  f->nK,  double );
    for ( m=0; m<nMu; m++ ){
        for ( k=0; k<nK; k++ ){
            DoIt = FALSE;

            if ( f->Extrapolate > 2 ){ // extrapolate above and below

                DoIt = TRUE;

            } else if ( f->Extrapolate == 2) {

                if (f->EofMu[m][k] >= f->E[0] ) DoIt = TRUE; // extrapolate above

            } else if ( f->Extrapolate == 1) {

                if (f->EofMu[m][k] <= f->E[f->nE-1] ) DoIt = TRUE; // extrapolate below

            } else if ( f->Extrapolate == 0) {

                if ((f->EofMu[m][k] >= f->E[0])&&(f->EofMu[m][k] <= f->E[f->nE-1])) DoIt = TRUE; // interp only

            }

            if (DoIt) {
                f->PSD_MK[m][k] =  Lgm_F2P_GetPsdAtEandAlpha( f->EofMu[m][k], f->AofK[k], f );
            } else {
                f->PSD_MK[m][k] = 0.0;
            }

        }
    }

    if ( f->DumpDiagnostics ) {
        DumpGif( "Lgm_FluxToPsd_PSD_MK", f->nK, f->nMu, f->PSD_MK );
    }


// FIX this... The create and destroy of this should not be in here...
    Lgm_FreeMagInfo( mInfo );

    f->Alloced2 = TRUE;

    return;

}

double  Model( double *x, double E ) {

    double  n1, T1, n2, T2, val;

    n1 = pow( 10.0,  x[1] );
    T1 = fabs( x[2] );

    n2 = pow( 10.0,  x[3] );
    T2 = fabs( x[4] );

    val = Lgm_MaxJut( n1, T1, E, LGM_Ee0 )
            + Lgm_MaxJut( n2, T2, E, LGM_Ee0 );
//    val = Lgm_MaxJut( n1, T1, E, LGM_Ee0 );

    return( val );

}

double Cost( double *x, void *data ){

    _FitData    *FitData;
    int         i;
    double      g_model, d, sum;

    if ( (x[1] > 2.0) || ( x[1] < -30.0) ) return( 9e99 );
    if ( (fabs( x[2] ) > 1000.0) || (fabs( x[2] ) < 1.0) ) return( 9e99 );
    if ( (x[3] > 2.0) || ( x[3] < -30.0) ) return( 9e99 );
    if ( (fabs( x[4] ) > 1000.0) || (fabs( x[4] ) < 1.0) ) return( 9e99 );

    FitData = (_FitData *)data; 


    for ( sum = 0.0, i=0; i<FitData->n; ++i ){


        g_model = log10( Model( x, FitData->E[i] ) );
        d = log10( FitData->g[i] ) - g_model;

        sum += d*d;
        //sum += fabs(d);
if (isinf(sum)) {
//    printf("Cost, INF: g_model, g = %g %g %g     x[1], x[2] = %g %g\n", g_model, FitData->g[i], log10( FitData->g[i] ), x[1], x[2]);
    return( 9e99 );
}
if (isnan(sum)) {
//    printf("Cost, NaN: g_model, g = %g %g %g     x[1], x[2] = %g %g\n", g_model, FitData->g[i], log10( FitData->g[i] ), x[1], x[2]);
//    printf("FitData->n = %d\n", FitData->n);
    return( 9e99 );
}

    }


    return( sum );

}



/**
 * The f structure should have an initialized PSD[E][a] array in it.
 * This routine computes psd given a value of E and a.
 */
double  Lgm_F2P_GetPsdAtEandAlpha( double E, double a, Lgm_FluxToPsd *f ) {

    int         j, i, i0, i1;
    double      a0, a1, y0, y1, slp, psd, g;
    _FitData    *FitData;

    // if a < 0, we should return fill value.
    if ( a < 0.0 ) return(-9e99);

    FitData = (_FitData *) calloc( 1, sizeof( _FitData ) );


    /*
     * Since pitch angle, a is bounded (here its constrained to be between 0
     * and 90), we will interpolate on that first to produce a 1D array of
     * f(E).
     */
    if ( a < f->A[0] ) {
        return(-9e99);
        i0 = 0; i1 = 1;
    } else if ( a > f->A[f->nA - 1] ) {
        return(-9e99);
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
    LGM_ARRAY_1D( FitData->E, f->nE, double );
    LGM_ARRAY_1D( FitData->g, f->nE, double );
    FitData->n = 0;
    for (j=0; j<f->nE; ++j){
        a0   = f->A[i0];
        a1   = f->A[i1];
        y0   = f->PSD_EA[j][i0];
        y1   = f->PSD_EA[j][i1];
        if ( (y0>0.0)&&(y1>0.0) ){ // if one of the 'y' vals is zero, dont use this point.
            slp  = (y1-y0)/(a1-a0);
            g = slp*(a-a1) + y1;
            if ( g > 1e-40 ) { // dont use if it looks bogus
                FitData->g[ FitData->n ] = g;
                FitData->E[ FitData->n ] = f->E[j];
                //printf("i0, i1 = %d %d   a0, a1 = %g %g   y0, y1, slp = %g %g %g    a = %g, FitData->g[%d] = %g\n", i0, i1, a0, a1, y0, y1, slp, a, j, FitData->g[j]);
                ++(FitData->n);
            }
        }


    }

    if ( FitData->n > 4 ) {

        
        // interpolate/fit E
        // for now just do a linear interp.
        // no lets try a fit...
        double  in[10], out[7], x[10];
        in[0] = 1e-8;
        in[1] = in[2] = 1e-9; //Info->Praxis_Tolerance;
        in[5] = 30000.0; //(double)Info->Praxis_Max_Function_Evals;
        in[6] = 10.0; //Info->Praxis_Maximum_Step_Size;
        in[7] = 10.0; //Info->Praxis_Bad_Scale_Paramater;
        in[8] = 4.0; //(double)Info->Praxis_Max_Its_Without_Improvement;
        in[9] = 1.0; //(double)Info->Praxis_Ill_Conditioned_Problem;
        x[0] = 0.0;
        x[1] = -1.0;
        x[2] = 25.0;
        x[3] = -2.0;
        x[4] = 200.0;
        praxis( 4, x, (void *)FitData, Cost, in, out);
    /*
    printf("out[0] = %g\n", out[0]);
    printf("out[1] = %g\n", out[1]);
    printf("out[2] = %g\n", out[2]);
    printf("out[3] = %g\n", out[3]);
    printf("out[4] = %g\n", out[4]);
    printf("out[5] = %g\n", out[5]);
    printf("out[6] = %g\n", out[6]);
    printf("x[1] = %g   x[2] = %g   Cost = %g\n", x[1], x[2], out[6]);

    FILE *fp;
    printf("E = %g\n", E);
    fp = fopen("data.txt", "w");
    for (j=0; j<f->nE; ++j){
    fprintf(fp, "%g %g\n", f->E[j], FitData->g[j]);
    }
    fclose(fp);
        
    exit(0);
    */
        

    //x[2] = 200.0;
        //printf("x - %g %g %g %g\n", x[1], x[2], x[3], x[4]);
        psd = Model( x,  E );
        //psd = (double)a;

    //printf("E, a = %g %g  x = %g %g psd = %g\n", E, a, x[1], x[2], psd);
    } else {
        psd = -9e99;
    }
    
    

    LGM_ARRAY_1D_FREE( FitData->E );
    LGM_ARRAY_1D_FREE( FitData->g );
    free( FitData );


    return( psd );

}



/**
 *  Returns a pointer to a dynamically allocated Lgm_PsdToFlux structure.
 *  User must destroy this with Lgm_P2F_FreePsdToFlux() when done.
 *
 *      \param[in]      DumpDiagnostics  Boolean flag to turn on/off dumping of diagnostics.
 *      \return         A pointer to an allocated and initialized Lgm_PsdToFlux stucture.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
Lgm_PsdToFlux *Lgm_P2F_CreatePsdToFlux( int DumpDiagnostics ) {

    Lgm_PsdToFlux *p;

    /*
     * Allocate memory for a Lgm_PsdToFlux structure.
     */
    p = (Lgm_PsdToFlux *) calloc( 1, sizeof(*p) );

    /*
     * Set DumpDiagnostics flag to what we got here. This can be changed later as well.
     */
    p->DumpDiagnostics = DumpDiagnostics;

    p->Extrapolate = TRUE;

    p->Alloced1 = FALSE;
    p->Alloced2 = FALSE;


    return p;

}

/**
 * Destroy a dynamically allocated Lgm_PsdToFlux structure. (E.g. one that was
 * created by Lgm_P2F_CreatePsdToFlux().)
 *
 *      \param          p  Pointer to the allocated Lgm_PsdToFlux structure that you want to destroy.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
void Lgm_P2F_FreePsdToFlux( Lgm_PsdToFlux *p ) {

    if ( p->Alloced1 ) {
        LGM_ARRAY_1D_FREE( p->Mu );
        LGM_ARRAY_1D_FREE( p->K );
        LGM_ARRAY_2D_FREE( p->PSD_MK );
    }

    if ( p->Alloced2 ) {
        LGM_ARRAY_1D_FREE( p->E );
        LGM_ARRAY_1D_FREE( p->A );
        LGM_ARRAY_1D_FREE( p->KofA );
        LGM_ARRAY_2D_FREE( p->MuofE );
        LGM_ARRAY_2D_FREE( p->PSD_EA );
        LGM_ARRAY_2D_FREE( p->FLUX_EA );
    }

    free( p );

    return;
}


/**
 *  Set Date/Time and position in the Lgm_PsdToFlux structure.
 *      
 *     
 *      \param[in]      d   Date/Time of measurement.
 *      \param[in]      u   Position of measurment (in GSM).
 *      \param[in,out]  p   Lgm_PsdToFlux sturcture.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
void Lgm_P2F_SetDateTimeAndPos( Lgm_DateTime *d, Lgm_Vector *u, Lgm_PsdToFlux *p ) {

    p->DateTime = *d;
    p->Position = *u;

}


/**
 *     Adds (to a Lgm_PsdToFlux structure) the user-supplied arrays containing PSD[Mu][K],  Mu[], K[]
 *
 *      \param[in]      P                 2D array containing the Phase Space Density as a function of Mu and K.
 *      \param[in]      Mu                1D array containing the energy values implied by the first index of Flux[][] array.
 *      \param[in]      nMu               number of energies.
 *      \param[in]      K                 1D array containing the pitch angles values implied by the second index of Flux[][] array.
 *      \param[in]      nK                number of pitch angles.
 *      \param[in,out]  p                 Lgm_FluxToPsd sturcture.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 *
 */
void Lgm_P2F_SetPsd( double **P, double *Mu, int nMu, double *K, int nK, Lgm_PsdToFlux *p ) {

    
    int     i, j;


    /*
     * If arrays are already alloc'd, free them first
     */
    if ( p->Alloced1 ) {
        LGM_ARRAY_1D_FREE( p->Mu );
        LGM_ARRAY_1D_FREE( p->K );
        LGM_ARRAY_2D_FREE( p->PSD_MK );
    }


    /*
     * Add Psd array to p structure. Alloc arrays appropriately.
     */
    p->nMu = nMu; 
    p->nK  = nK; 
    LGM_ARRAY_1D( p->Mu, p->nMu, double );
    LGM_ARRAY_1D( p->K, p->nK, double );
    LGM_ARRAY_2D( p->PSD_MK, p->nMu, p->nK, double );
    for (i=0; i<p->nMu; i++) p->Mu[i] = Mu[i];
    for (i=0; i<p->nK; i++)  p->K[i]  = K[i];
    for (i=0; i < p->nMu; i++) {
        for (j=0; j < p->nK; j++) {
            p->PSD_MK[i][j] = P[i][j]; // PSD_MK is "PSD versus Mu and K".
        }
    }
    if ( p->DumpDiagnostics ) {
        DumpGif( "Lgm_PsdToFlux_PSD_MK", p->nK, p->nMu, p->PSD_MK );
    }


    p->Alloced1 = TRUE;
   
    return;

}




/**
 *  Computes Flux at user-supplied constant values of E
 *  and \f$\alpga\f$.
 *
 *  This routine ( Lgm_P2F_GetFluxAtConstEsAndAs() ) must operate on a
 *  pre-initialized Lgm_PsdToFlux structure.  The routine Lgm_P2F_SetPsd()
 *  is used to add PSD data/info to an Lgm_PsdToFlux structure.
 *
 *  We want Flux at constant E and \f$\alpha \f$ (i.e. we want \J$f( E, \alpha
 *  )\f$).  
 * 
 *  To perform the calculation we note that \f$f( \mu, K )\f$ is the same as
 *  \f$f( \mu(E, \alpha), K(\alpha) )\f$. Thus, for a given E and \f$\alpha\f$,
 *  we can figure out what \f$\mu\f$ and K  they correspond to and then we can
 *  just use the \f$f(\mu, K)\f$ array to compute the desired f values. Then
 *  finally convert f to J.
 *  The steps are;
 *
 *      - For each \f$\alpha\f$ compute \f$K(\alpha)\f$. This is done with the routine
 *        Lgm_KofAlpha().
 *
 *      - Then we compute \f$\mu\f$ from E and \f$\alpha\f$.
 *
 *      - Then we look up \f$f(\mu, K)\f$ from the array (interp or fit or
 *        whatever).
 *
 *      \param[in]      nE          Number of E values
 *      \param[in]      E           1-D array of E values
 *      \param[in]      nA          Number of Alpha values
 *      \param[in]      A           1-D array of Alpha values
 *      \param[in]      Extrapolate Turns on/off extrapolation capability
 *      \param[in,out]  p           A properly pre-initialized Lgm_PsdToFlux structure.
 *
 *      \author     Mike Henderson
 *      \date       2011
 *      \warning    Still working on this code. It is not finished.
 * 
 */
void Lgm_P2F_GetFluxAtConstEsAndAs( double *E, int nE, double *A, int nA, Lgm_PsdToFlux *p ) {

    int                 k, m, DoIt;
    double              SinAlphaEq, AlphaEq, p2c2;
    Lgm_MagModelInfo    *mInfo, *mInfo2;

    /*
     * Init mInfo
This is no good! How does user define mag model etc...?
I think there needs to be a Lgm_MagModelInfo struct in f
Then add a routine to set stuff up in there. Or just use the ones we have already....
For now we will just go with the defaults.
     */
    mInfo = Lgm_InitMagInfo();
//mInfo->Bfield = Lgm_B_edip;

    /*
     * If arrays are already alloc'd, free them first
     */
    if ( p->Alloced2 ) {
        LGM_ARRAY_1D_FREE( p->E );
        LGM_ARRAY_1D_FREE( p->A );
        LGM_ARRAY_1D_FREE( p->KofA );
        LGM_ARRAY_2D_FREE( p->MuofE );
        LGM_ARRAY_2D_FREE( p->PSD_EA );
        LGM_ARRAY_2D_FREE( p->FLUX_EA );
    }
    
    /*
     * Alloc arrays
     */
    p->nE = nE; 
    p->nA = nA; 
    LGM_ARRAY_1D( p->E,     p->nE, double );
    LGM_ARRAY_1D( p->A,     p->nA,  double );
    LGM_ARRAY_1D( p->KofA,  p->nA,  double );
    LGM_ARRAY_2D( p->MuofE, p->nE,  p->nA,  double );



    /*
     * Copy A's (given in the arguments) into p structure.
     * Transform the A's into K's using Lgm_KofAlpha().
     * Save the results in the p structure.
     */
    Lgm_Setup_AlphaOfK( &(p->DateTime), &(p->Position), mInfo );
    p->B = mInfo->Blocal;
    {
        #pragma omp parallel private(mInfo2,SinAlphaEq,AlphaEq)
        #pragma omp for schedule(dynamic, 1)
        for ( k=0; k<nA; k++ ){

            mInfo2 = Lgm_CopyMagInfo( mInfo );  // make a private (per-thread) copy of mInfo

            p->A[k]    = A[k]; // A is local Pitch Angle
            SinAlphaEq = sqrt( mInfo2->Bmin/mInfo2->Blocal ) * sin( RadPerDeg*p->A[k] );
            AlphaEq    = DegPerRad*asin( SinAlphaEq );
            p->KofA[k] = Lgm_KofAlpha( AlphaEq, mInfo2 );

            Lgm_FreeMagInfo( mInfo2 ); // free mInfo2

        }
    }
    Lgm_TearDown_AlphaOfK( mInfo );


    /*
     * Copy E's (given in the arguments) into p structure.
     * Transform the E's into Mu's.
     * Save the results in the p structure.
     * Note that since this conversion involves E and Alpha, the result is 2D.
assumes electrons -- generalize this...
     */
    for ( m=0; m<nE; m++ ){
        p->E[m] = E[m];
        for ( k=0; k<nA; k++ ){
            p->MuofE[m][k] = Lgm_Ek_to_Mu( p->E[m], p->A[k], p->B, LGM_Ee0 );
            //printf("f->Mu[%d], f->K[%d], f->AofK[%d], f->B, f->EofMu[%d][%d] = %g %g %g %g %g\n", m, k, k, m, k, f->Mu[m], f->K[k], f->AofK[k], f->B, f->EofMu[m][k]);
        }
    }


    /*
     * Now, from the PSD[Mu][K] array, get PSD at the Mu's and K's we just computed.
     * The result will be the same as PSD at the given E's and A's
     */
    LGM_ARRAY_2D( p->PSD_EA,  p->nE,  p->nA,  double );
    LGM_ARRAY_2D( p->FLUX_EA, p->nE,  p->nA,  double );
    for ( m=0; m<nE; m++ ){
        p2c2 = Lgm_p2c2( p->E[m], LGM_Ee0 );
        for ( k=0; k<nA; k++ ){
            DoIt = FALSE;

            if ( p->Extrapolate > 2 ){ // extrapolate above and below

                DoIt = TRUE;

            } else if ( p->Extrapolate == 2) {

                if (p->MuofE[m][k] >= p->Mu[0] ) DoIt = TRUE; // extrapolate above

            } else if ( p->Extrapolate == 1) {

                if (p->MuofE[m][k] <= p->Mu[p->nMu-1] ) DoIt = TRUE; // extrapolate below

            } else if ( p->Extrapolate == 0) {

                if ((p->MuofE[m][k] >= p->Mu[0])&&(p->MuofE[m][k] <= p->Mu[p->nMu-1])) DoIt = TRUE; // interp only

            }

            if (DoIt) {
                p->PSD_EA[m][k]  = Lgm_P2F_GetPsdAtMuAndK( p->MuofE[m][k], p->KofA[k], p->A[k], p );
                // Now do conversion from units of PSD to Flux
                p->FLUX_EA[m][k] = Lgm_PsdToDiffFlux( p->PSD_EA[m][k], p2c2 );
//if (m==2)
//printf("p->MuofE[m][k] = %g p->KofA[k], p->A[k] = %g %g       p->PSD_EA[m][k] = %g\n", p->MuofE[m][k], p->KofA[k], p->A[k], p->PSD_EA[m][k]);
            } else {
                p->PSD_EA[m][k] = 0.0;
            }

        }
    }

    if ( p->DumpDiagnostics ) {
        DumpGif( "Lgm_PsdToFlux_PSD_EA", p->nA, p->nE, p->PSD_EA );
        DumpGif( "Lgm_PsdToFlux_FLUX_EA", p->nA, p->nE, p->FLUX_EA );
    }


// FIX this... The create and destroy of this should not be in here...
    Lgm_FreeMagInfo( mInfo );

    p->Alloced2 = TRUE;

    return;

}



/**
 * The p structure should have an initialized PSD[Mu][K] array in it (i.e. as
 * added by Lgm_P2F_SetPsd()).  This routine computes psd from this array given
 * arbitrary values of Mu and K. (Alpha is also needed here, because we need to
 * convert some Mu's to to Energie's long the way).
 */
double  Lgm_P2F_GetPsdAtMuAndK( double Mu, double K, double A, Lgm_PsdToFlux *p ) {

    int         j, i, i0, i1;
    double      K0, K1, y0, y1, slp, psd, E, g;
    _FitData    *FitData;

    // if K < 0, we should return fill value.
    if ( K < 0.0 ) return(-9e99);

    FitData = (_FitData *) calloc( 1, sizeof( _FitData ) );


    /*
     * Interpolate on K first to get a 1D array of f(mu).
     */
    if ( K < p->K[0] ) {
        return(-9e99);
        i0 = 0; i1 = 1;
    } else if ( K > p->K[p->nK - 1] ) {
        return(-9e99);
        i0 = p->nK - 2; i1 = p->nK - 1;
    } else {
        for (i=1; i<p->nK; i++) {
            if ( K < p->K[i] ) {
                i0 = i-1; i1 = i;
                break;
            }
        }
    }
    //printf("i0, i1 = %d %d\n", i0, i1);


    // interpolate K
    LGM_ARRAY_1D( FitData->E, p->nMu, double );
    LGM_ARRAY_1D( FitData->g, p->nMu, double );
    FitData->n = 0;
    for (j=0; j<p->nMu; ++j){
        K0   = p->K[i0];
        K1   = p->K[i1];
        y0   = p->PSD_MK[j][i0];
        y1   = p->PSD_MK[j][i1];
        if ( (y0>0.0)&&(y1>0.0) ){
            slp  = (y1-y0)/(K1-K0);
            g = slp*(K-K1) + y1;
            if ( g > 1e-40 ) {
                FitData->g[ FitData->n ] = g;
                FitData->E[ FitData->n ] = Lgm_Mu_to_Ek( p->Mu[j], A, p->B, LGM_Ee0 );
                //printf("i0, i1 = %d %d   K0, K1 = %g %g   y0, y1, slp = %g %g %g   K = %g, FitData->E[%d] = %g FitData->g[%d] = %g\n", i0, i1, K0, K1, y0, y1, slp, K,  FitData->n, FitData->E[ FitData->n ], FitData->n , FitData->g[ FitData->n ]);
                //printf("%g %g\n", FitData->E[ FitData->n ], FitData->g[ FitData->n ]);
                ++(FitData->n);
            }
        }
    }

    if ( FitData->n >=  4 ) {

        
        // interpolate/fit E
        // for now just do a linear interp.
        // no lets try a fit...
        double  in[10], out[7], x[5];
        in[0] = 1e-8;
        in[1] = in[2] = 1e-9; //Info->Praxis_Tolerance;
        in[5] = 30000.0; //(double)Info->Praxis_Max_Function_Evals;
        in[6] = 10.0; //Info->Praxis_Maximum_Step_Size;
        in[7] = 10.0; //Info->Praxis_Bad_Scale_Paramater;
        in[8] = 4.0; //(double)Info->Praxis_Max_Its_Without_Improvement;
        in[9] = 1.0; //(double)Info->Praxis_Ill_Conditioned_Problem;
        x[0] = 0.0;
        x[1] = -1.0;
        x[2] = 25.0;
        x[3] = -2.0;
        x[4] = 200.0;
        praxis( 4, x, (void *)FitData, Cost, in, out);
    /*
    printf("out[0] = %g\n", out[0]);
    printf("out[1] = %g\n", out[1]);
    printf("out[2] = %g\n", out[2]);
    printf("out[3] = %g\n", out[3]);
    printf("out[4] = %g\n", out[4]);
    printf("out[5] = %g\n", out[5]);
    printf("out[6] = %g\n", out[6]);
    printf("x[1] = %g   x[2] = %g   Cost = %g\n", x[1], x[2], out[6]);

    FILE *fp;
    printf("E = %g\n", E);
    fp = fopen("data.txt", "w");
    for (j=0; j<f->nE; ++j){
    fprintf(fp, "%g %g\n", f->E[j], FitData->g[j]);
    }
    fclose(fp);
        
    exit(0);
    */
        

    //x[2] = 200.0;
        //printf("PSD_TO_FLUX: x - %g %g %g %g\n", x[1], x[2], x[3], x[4]);
        E = Lgm_Mu_to_Ek( Mu, A, p->B, LGM_Ee0 );
        psd = Model( x,  E );
        //psd = (double)a;

    //printf("E, a = %g %g  x = %g %g psd = %g\n", E, a, x[1], x[2], psd);
    } else {

        psd = -9e99;

    }
    
    

    LGM_ARRAY_1D_FREE( FitData->E );
    LGM_ARRAY_1D_FREE( FitData->g );
    free( FitData );


    return( psd );

}













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
void DumpGif( char *FilenameBase, int W, int H, double **Image ){

    double           Val, Min, Max, dVal;
    int              w, h;
    unsigned char   *uImage, uVal, Filename[1024];
    FILE            *fp_gif, *fp_info;

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

    sprintf( Filename, "%s.info", FilenameBase);
    fp_info = fopen( Filename, "w" );
    fprintf( fp_info, "Min: %g\n", Min );
    fprintf( fp_info, "Max: %g\n", Max );
    fclose( fp_info );



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
                dVal = (Val - Min)/(Max-Min)*255.0;
                uVal = (dVal > 255.0) ? 255 : (unsigned char)dVal;
            }
            *(uImage + W*(H-1-h) + w) = uVal;

        }
    }

    sprintf( Filename, "%s.gif", FilenameBase);
    fp_gif = fopen(Filename, "w");
    WriteGIF(fp_gif, (byte *)uImage, 0, W, H, Rainbow2_Red, Rainbow2_Grn, Rainbow2_Blu, 256, 0, "");
    fclose(fp_gif);

    free( uImage );



    // dump a colorbar image
    W = 10; H = 256;
    uImage = (unsigned char *)calloc( W*H, sizeof(unsigned char) );
    for ( w=0; w<W; w++ ){
        for ( h=0; h<H; h++ ) {
            *(uImage + W*(H-1-h) + w) = h;
        }
    }
    sprintf( Filename, "%s_Bar.gif", FilenameBase);
    fp_gif = fopen(Filename, "w");
    WriteGIF(fp_gif, (byte *)uImage, 0, W, H, Rainbow2_Red, Rainbow2_Grn, Rainbow2_Blu, 256, 0, "");
    fclose(fp_gif);
    free( uImage );

}



/**
 *  \brief
 *     Fills the given array with a geomteric sequence of values.
 *
 *  \details
 *      
 *      \param[in]      a  Starting value.
 *      \param[in]      b  Ending value.
 *      \param[in]      n  Number of values (must be 2 or more.)
 *      \param[out]     G  User supply array (or size >= n ).
 *
 *      \return         1 if successful, 0 otherwise.
 *
 *  \notes
 *      a and be must be greater than zero and n must be greater than or equal to 2.
 *
 *      \author         Mike Henderson
 *      \date           2010-2011
 */
int Lgm_GeometricSeq( double a, double b, int n, double *G ) {

    if ( ( a <= 0.0 ) || ( b <= 0.0 ) || ( n<2 ) ) return(0);

    int     j;
    double  r, *S = (double *)calloc( n, sizeof(double) );

    r = pow( b/a, 1.0/((double)(n-1)));

printf("a, b, r = %g %g %g\n", a, b, r);
    
    S[0] = a;
    for (j=1; j<n; j++) S[j] = S[j-1]*r;
    for (j=0; j<n; j++) G[j] = S[j];

    free( S );

    return(1);
}





