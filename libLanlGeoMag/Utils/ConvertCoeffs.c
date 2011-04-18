#include <stdio.h>
#include <math.h>
#include <Lgm/Lgm_SphHarm.h>

/*
 *  These are Gauss-Normalized Jensen-Cain 1960 Coeffs - AS PUBLISHED.
 *  We need to convert them to Schmidt Semi-Normalized Coeffs for use in LanlGeoMag.
 */
static double g[][13][13] = {
  { {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {   -30411.2,    -2147.4,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {    -2403.5,     5125.3,     1338.1,        0,            0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {     3151.8,    -6213.0,     2489.8,      649.6,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {     4179.4,     4529.8,     2179.5,     -700.8,      204.4,          0,          0,          0,          0,          0,          0,          0,          0 },
    {    -1625.6,     3440.7,     1944.7,       60.8,     -277.5,      -69.7,          0,          0,          0,          0,          0,          0,          0 }, // Jensen and Cain [1960].
    {     1952.3,      485.3,     -321.2,    -2141.3,     -105.1,      -22.7,     -111.5,          0,          0,          0,          0,          0,          0 }, // See JGR, page 3569, 1962.
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 } }

  };


static double h[][13][13] = {
  { {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,     5798.9,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,    -3312.4,      157.9,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,    -1487.0,      407.5,      -21.0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,     1182.5,    -1000.6,      -43.0,     -138.5,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,       79.6,      200.0,     -459.7,     -242.1,      121.8,          0,          0,          0,          0,          0,          0,          0 }, // Jensen and Cain [1960].
    {          0,      575.8,      873.5,      340.6,       11.8,      111.6,       32.5,          0,          0,          0,          0,          0,          0 }, // See JGR, page 3569, 1962.
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 } }

  };


/*
 *  These are Gauss-Normalized Jensen-Cain 1960 Coeffs - FROM newmgd.f
 *  We need to convert them to Schmidt Semi-Normalized Coeffs for use in LanlGeoMag.
 */
static double g2[][13][13] = {
  { {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {   -30411.2,  -2147.369,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {   -2403.53,   5125.334,   1338.120,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {   3151.787,  -6213.009,   2489.813,   649.5659,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {   4179.436,   4529.837,   2179.475,  -700.8254,   204.3956,          0,          0,          0,          0,          0,          0,          0,          0 },
    {  -1625.563,   3440.676,   1944.700,   60.82110,  -277.5335,  -69.68020,          0,          0,          0,          0,          0,          0,          0 }, // Jensen and Cain [1960].
    {   1952.317,   485.3261,  -321.1724,  -2141.288,  -105.0513,  -22.68290,  -111.4714,          0,          0,          0,          0,          0,          0 }, // See JGR, page 3569, 1962.
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 } }

  };


static double h2[][13][13] = {
  { {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,   5798.905,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,  -3312.407,   157.8938,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,  -1486.969,   407.4902,  -21.03180,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,   1182.455,  -1000.577,  -43.03810,  -138.5035,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,   79.58970,   200.0440,  -459.7189,  -242.0631,   121.8065,          0,          0,          0,          0,          0,          0,          0 }, // Jensen and Cain [1960].
    {          0,   575.8303,   873.4614,   340.6041,   11.81620,   111.6230,   32.48320,          0,          0,          0,          0,          0,          0 }, // See JGR, page 3569, 1962.
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 },
    {          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0 } }

  };



main(){

    int     n, m;
    double  g_gauss, g_schmidt, Snm;
    double  h_gauss, h_schmidt;


    printf("static double SphHarm_g[][13][13] = {\n");
    for ( n=0; n<=12; n++ ){
        if ( n==0 ) printf("  { {");
        else        printf("    {");
        for ( m=0; m<=12; m++ ){
            g_gauss = g2[0][n][m];
            if ( m<=n ) {
                Lgm_GaussToSchmidtSemiNorm( n, m, g_gauss, &g_schmidt, &Snm );
            } else {
                g_schmidt = 0.0;
            }
            if ( g_gauss == 0.0 ) {
                printf("%14g,", g_schmidt );
            } else {
                printf("%14.6lf,", g_schmidt );
            }
        }
        if      ( n==5 )  printf(" }, // Jensen and Cain [1960].\n");
        else if ( n==6 )  printf(" }, // See JGR, page 3569, 1962.\n");
        else if ( n==12 ) printf(" } }\n");
        else              printf(" },\n");
    }
    printf("  };\n");

    printf("static double SphHarm_h[][13][13] = {\n");
    for ( n=0; n<=12; n++ ){
        if ( n==0 ) printf("  { {");
        else        printf("    {");
        for ( m=0; m<=12; m++ ){
            h_gauss = h2[0][n][m];
            if ( m<=n ) {
                Lgm_GaussToSchmidtSemiNorm( n, m, h_gauss, &h_schmidt, &Snm );
            } else {
                h_schmidt = 0.0;
            }
            if ( h_gauss == 0.0 ) {
                printf("%14g,", h_schmidt );
            } else {
                printf("%14.6lf,", h_schmidt );
            }
        }
        if      ( n==5 )  printf(" }, // Jensen and Cain [1960].\n");
        else if ( n==6 )  printf(" }, // See JGR, page 3569, 1962.\n");
        else if ( n==12 ) printf(" } }\n");
        else              printf(" },\n");
    }
    printf("  };\n");


}

