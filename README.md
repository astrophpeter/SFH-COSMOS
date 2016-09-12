# SFH-COSMOS

###Description of Contents

``data/``

*(download link in data folder as files to big to host on github)*

All of this analysis was performed using [ULTRA-VISTA catalog data](https://www.strw.leidenuniv.nl/galaxyevolution/ULTRAVISTA/Ultravista/K-selected.html), Galaxy Zoo Hubble Morpholgy data, Overdensity data from Darvish et al (2015), and Stellar-Mass data from Ilbert et al (2013).

* ```GalaxyZoo.fits``` Obtained from Brooke Simmons - Galaxy Zoo morpholgical data - note this does not include debiased vote fractions, in orted to select a good sample of galaxy with particular feature see Galaxy zoo data paper.

* ```Darvish2015.xml``` Obtained from the Darvish et al (2015) paper - relevant column is 'logdel' which is the overdensity values $\log(1+\delta)$. Note this overdensity was calculated using a technique called Voronoi Tessellation.

* ```UVISTA_full_v4.1.fits``` Obtaied from the ULTRAVISTA data product downloads page linked above (K-selected). This is all data product downloads stiched together. See table below detailing relevant columns names and descriptions

<center>

| Column Name        | Meaning          | Detail  |
| -------------------|:---------------:| -------:|
| LMASS_1            | Stellar Mass - $\log(mass/M_sol)$| Log (base 10) of the stellar mass of the galaxy|
| z_peak             | Best value of redshift | In all analysis the value for redhsit used is z_peak   |
| zebra stripes      | are neat         |    $1   |

</center>
