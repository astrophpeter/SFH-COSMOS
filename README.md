# SFH-COSMOS

###Description of Contents

``data/``

*(download link in data folder as files to big to host on github)*

All of this analysis was performed using [ULTRA-VISTA catalog data](https://www.strw.leidenuniv.nl/galaxyevolution/ULTRAVISTA/Ultravista/K-selected.html), Galaxy Zoo Hubble (GZH) Morpholgy data, Overdensity data from Darvish et al (2015) [1].

* ```GalaxyZoo.fits``` Obtained from Brooke Simmons - GZH data - note this does not include debiased vote fractions, in orted to select a good sample of galaxy with particular feature see GZH paper [3].

* ```Darvish2015.xml``` Obtained from the Darvish et al (2015) paper [1] - relevant column is 'logdel' which is the overdensity values $\log(1+\delta)$. Note this overdensity was calculated using a technique called Voronoi Tessellation.

* ```UVISTA_full_v4.1.fits``` Obtaied from the ULTRAVISTA data product downloads page linked above (K-selected). This is all data product downloads stiched together. The paper corresponding to this data is [2]. See table below detailing relevant columns names and descriptions


| Column Name        | Meaning                           | Detail                                                 |
| -------------------|:----------------------------------|--------------------------------------------------------|
| LMASS_1            | Stellar Mass - $\log(mass/M_sol)$ | Log (base 10) of the stellar mass of the galaxy, calculated <br> using the BC03 SPS Model, using the FAST code, details on ULTRAVISTA catalog website. Note on Solar metalicity: made with a Chabrier IMF and Padova 1994 isochrones                                              |
| z_peak             | Best value of redshift            | In all analysis the value for redhsit used is z_peak   |
| SFR_IR             | SFR from IR Luminosity            | Negative values of SFR indicate -1.0*(upper limit SFR) <br> from MIPS-24um | 
| SFR_UV             | SFR form UV Luminosity            |                                                        |
| SFR_tot            | Total Star formation rate         | Sum of UV and IR SFRs, **we dont include SFR_tot where <br> SFR_IR < 0**, because Negative values of SFR indicate -1.0*(upper limit SFR) from MIPS-24um                                     | 
| VmJ                | V - J rest frame colour           | Calculated using the EAZY code. Note no errors, this is addressed later |
| UmV                | U - V rest frame colour           | Calcualted using the EAZY code. Note no errors, this is addressed later |
| USE_1              | Flag                              | This selects galaxies with good photometry S/N > 5.    |

The catalog also contains apeture fluxes for many bands with errors. Other data files are combinated of the above files, and are named apropriately. They were matched equally with TOPCAT by ra and dec with error +- 3.0.



``muzzing2013Fig9/``

* ``idl.mplstyle`` Makes the python plots look waaaay better :)

*  ``Muzzin2013Fig9Morph.pdf`` This is a recreated version of Figure 9 from Muzzing et al (2013) [2]. With GZH morphology overlaid. We colour galaxies with P_{feature} > 0.7 in Blue and and galaxies with P_{smooth} > 0.8 in red. The dividing green line separates Star-forming and Quiescent galaxies, this line is taken from a follow-up paper by the same author [citation needed]. We only include the first two redshift bins as for z > 1 we dont have a significant volume of GZH classifications.

*  ``Muzzin2013Fig9Morph.py`` Generating code for ``Muzzin2013Fig9Morph.pdf``.

* ``Muzzin2013Fig9Mass.pdf`` Version of Muzzin et al (2013) [2] but with galaxies split my High / Low Stellar mass. Where High Low mas <>  log(M/M_sol) <> 10 define by Kauffman et al 2003 [5].

* ``Muzzin2013Fig9Mass.py`` Generating code for ``Muzzin2013Fig9Mass.pdf``.





## Refernces
[1] Darvish, Behnam, et al. "A comparative study of density field estimation for galaxies: New insights into the evolution of galaxies with environment in cosmos out to Z∼ 3." The Astrophysical Journal 805.2 (2015): 121. DOI:
[10.1088/0004-637X/805/2/121](10.1088/0004-637X/805/2/121)

[2] Muzzin, Adam, et al. "A PUBLIC Ks-SELECTED CATALOG IN THE COSMOS/ULTRAVISTA FIELD: PHOTOMETRY, PHOTOMETRIC REDSHIFTS, AND STELLAR POPULATION PARAMETERS. The Astrophysical Journal Supplement Series 206.1 (2013): 8. DOI: [10.1088/0067-0049/206/1/8](10.1088/0067-0049/206/1/8)

[3] Galaxy Zoo: Morphological Classifications for 120,000 Galaxies in HST Legacy Imaging Paper current being written can be found in this [repo](https://github.com/willettk/gzhubble/blob/master/writeup/gz_hubble_data.pdf)

[4] Muzzin follow up paper.

[5] Kauffmann, Guinevere, et al. "The dependence of star formation history and internal structure on stellar mass for 105 low-redshift galaxies." Monthly Notices of the Royal Astronomical Society 341.1 (2003): 54-69. DOI:
[10.1046/j.1365-8711.2003.06292.x](10.1046/j.1365-8711.2003.06292.x)



