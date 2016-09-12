# SFH-COSMOS

###Description of Contents

``data/``

*(download link in data folder as files to big to host on github)*

All of this analysis was performed using [ULTRA-VISTA catalog data](https://www.strw.leidenuniv.nl/galaxyevolution/ULTRAVISTA/Ultravista/K-selected.html), Galaxy Zoo Hubble Morpholgy data, Overdensity data from Darvish et al (2015) [1].

* ```GalaxyZoo.fits``` Obtained from Brooke Simmons - Galaxy Zoo morpholgical data - note this does not include debiased vote fractions, in orted to select a good sample of galaxy with particular feature see Galaxy zoo data paper.

* ```Darvish2015.xml``` Obtained from the Darvish et al (2015) paper [1] - relevant column is 'logdel' which is the overdensity values $\log(1+\delta)$. Note this overdensity was calculated using a technique called Voronoi Tessellation.

* ```UVISTA_full_v4.1.fits``` Obtaied from the ULTRAVISTA data product downloads page linked above (K-selected). This is all data product downloads stiched together. See table below detailing relevant columns names and descriptions

<center>

| Column Name        | Meaning                           | Detail                                                 |
| -------------------|:----------------------------------|--------------------------------------------------------|
| LMASS_1            | Stellar Mass - $\log(mass/M_sol)$ | Log (base 10) of the stellar mass of the galaxy, calculated <br> using the BC03 SPS Model, using the FAST code, details on ULTRAVISTA catalog website.                                               |
| z_peak             | Best value of redshift            | In all analysis the value for redhsit used is z_peak   |
| SFR_IR             | SFR from IR Luminosity            | Negative values of SFR indicate -1.0*(upper limit SFR) <br> from MIPS-24um | 
| SFR_UV             | SFR form UV Luminosity            |                                                        |
| SFR_tot            | Total Star formation rate         | Sum of UV and IR SFRs, **we dont include SFR_tot where <br> SFR_IR < 0**, because Negative values of SFR indicate -1.0*(upper limit SFR) from MIPS-24um                                     | 
| VmJ                | V - J rest frame colour           | Calculated using the EAZY code. Note no errors, this is addressed later |
| UmV                | U - V rest frame colour           | Calcualted using the EAZY code. Note no errors, this is addressed later |
| USE_1              | Flag                              | This selects galaxies with good photometry S/N > 5.    |

The catalog also contains apeture fluxes for many bands with errors. Other data files are combinated of the above files, and are named apropriately. They were matched equally with TOPCAT by ra and dec with error +- 3.0.

</center>


## Refernces
[1] Darvish, Behnam, et al. "A comparative study of density field estimation for galaxies: New insights into the evolution of galaxies with environment in cosmos out to Z∼ 3." The Astrophysical Journal 805.2 (2015): 121. DOI: 
[10.1088/0004-637X/805/2/121](
10.1088/0004-637X/805/2/121)



