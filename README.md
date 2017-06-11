# SFH-COSMOS

### Description of Contents

``data/``

*(download link in data folder as files to big to host on github)*

All of this analysis was performed using [ULTRA-VISTA catalog data](https://www.strw.leidenuniv.nl/galaxyevolution/ULTRAVISTA/Ultravista/K-selected.html), Galaxy Zoo Hubble (GZH) Morpholgy data, Overdensity data from Darvish et al (2015) [1].

* ```GalaxyZoo.fits``` Obtained from Brooke Simmons - GZH data - note this does not include debiased vote fractions, in order to select a good sample of galaxy with particular feature see GZH paper [3].

* ```Darvish2015.xml``` Obtained from the Darvish et al (2015) paper [1] - relevant column is 'logdel' which is the overdensity values $\log(1+\delta)$. Note this overdensity was calculated using a technique called Voronoi Tessellation.

* ```UVISTA_full_v4.1.fits``` Obtaited from the ULTRAVISTA data product downloads page linked above (K-selected). This is all data product downloads stitched together. The paper corresponding to this data is [2]. See table below detailing relevant columns names and descriptions


| Column Name        | Meaning                           | Detail                                                 |
| -------------------|:----------------------------------|--------------------------------------------------------|
| LMASS_1            | Stellar Mass - $\log(mass/M_sol)$ | Log (base 10) of the stellar mass of the galaxy, calculated <br> using the BC03 SPS Model, using the FAST code, details on ULTRAVISTA catalog website. Note on Solar metalicity: made with a Chabrier IMF and Padova 1994 isochrones                                              |
| z_peak             | Best value of redshift            | In all analysis the value for redshift used is z_peak   |
| SFR_IR             | SFR from IR Luminosity            | Negative values of SFR indicate -1.0*(upper limit SFR) <br> from MIPS-24um | 
| SFR_UV             | SFR form UV Luminosity            |                                                        |
| SFR_tot            | Total Star formation rate         | Sum of UV and IR SFRs, **we don't include SFR_tot where <br> SFR_IR < 0**, because negative values of SFR indicate -1.0*(upper limit SFR) from MIPS-24um (Sum method in [2])                                    | 
| VmJ                | V - J rest frame colour           | Calculated using the EAZY code. Note no errors, this is addressed later |
| UmV                | U - V rest frame colour           | Calculated using the EAZY code. Note no errors, this is addressed later |
| USE_1              | Flag                              | This selects galaxies with good photometry S/N > 5.    |

The catalog also contains apeture fluxes for many bands with errors. Other data files are combined of the above files, and are named appropriately. They were matched equally with TOPCAT by RA and Dec with error +- 3.0.



``muzzing2013Fig9/``

* ``idl.mplstyle`` Makes the python plots look waaaay better :)

*  ``Muzzin2013Fig9Morph.pdf`` This is a recreated version of Figure 9 from Muzzing et al (2013) [2]. With GZH morphology overlaid. We colour galaxies with P_{feature} > 0.7 in blue and and galaxies with P_{smooth} > 0.8 in red. The dividing green line separates star-forming and quiescent galaxies, this line is taken from a follow-up paper by the same author [4]. We only include the first two redshift bins as for z > 1 we don't have a significant volume of GZH classifications.

*  ``Muzzin2013Fig9Morph.py`` Generating code for ``Muzzin2013Fig9Morph.pdf``.

* ``Muzzin2013Fig9Mass.pdf`` Version of Muzzin et al (2013) [2] but with galaxies split my high / low stellar mass. Where high low mass <>  log(M/M_sol) <> 10 define by Kauffman et al 2003 [5].

* ``Muzzin2013Fig9Mass.py`` Generating code for ``Muzzin2013Fig9Mass.pdf``.

* ``Muzzin2013Fig9bar.pdf`` Version of Muzzin et al (2013) Fig 9 but split by bar / not bar galaxies coloured by red and black respectively. A sample of bar galaxies was chosen using Table 11 in [4] - P_{feature} > 0.23 -> P_{clumpy,n0} > 0.3 -> P_{edgeon, no} > 0.25 -> P_{bar} > 0.7. 

* ``Muzzin2013Fig9bar.py`` Generating code for ``Muzzin2013Fig9bar.pdf``.

``Darvish2016Fig1/``

* ``Darvish2016Fig1AllMorph.pdf`` This is a version of Figure 1 from Darvish et al (2016) [6] using all galaxies (SF+Quiescent), with GZH Hubble smooth/feature morphology overlaid. ONly first two redshift bins plotted dues to lack of data points at higher redshifts.

* ``Darvish2016Fig1AllMorph.py`` Generating code for ``Darvish2016Fig1AllMorph.pdf``

* ``Darvish2016Fig1SFMorph.pdf`` This is a version of Figure 1 from Darvish et al (2016) [6] using star forming galaxies only, with GZH Hubble smooth/feature morphology overlaid. Only first two redshift bins plotted due to lack of data points at higher redshifts.

* ``Darvish2016Fig1SFMorph.py`` Generating code for ``Darvish2016Fig1SFMorph.pdf``.

``Darvish2016Fig2/``

* ``Darvish2016Fig2.pdf`` This is a version of Figure 2 from Darvish et al (2016) [6], with GZH morphology overlaid. Binned by stellar mass. (LMASS_1).

* ``Darvish2016Fig2.py`` Generating code for ``Darvish2016Fig2.pdf``.


``starpy/``

All analysis in this section was done with a modified version of starpy. The only place this code was changed was the filter specific part. Where filters where replaced with the corrected filters for the COSMOS survey. Found in Miaz et al (2006) [8]. This code was run on the Glamdring computer cluster, and the output saved to my account. The way starpy is run is exactly the same as the original code which can be found [here](https://github.com/rjsmethurst/starpy).

All required modules are installed correctly on my glamdring account.

To run this code for many galaxies on glamdring you will need to create a ``params.txt`` file and save it in the same directory as ``starpy.py``. ``params.txt`` should have the following format:

```
python3 starpy.py VmJ(1) err_VmJ(1) UmV(1) err_UmV(1) z(1) ID(1) ra(1) dec(1)
python3 starpy.py VmJ(2) err_VmJ(2) UmV(2) err_UmV(2) z(2) ID(2) ra(2) dec(2)
.           .               .           .         .         .    .     .     .
.           .               .           .         .         .    .     .     .
.           .               .           .         .         .    .     .     .
```

The VmJ values have a standard error of 0.139951, and the UmV error have a value of 0.099356. These values were calculated in the following way. Noticing that the errors in aperture flux for U,V and J bands are relatively small in ```UVISTA_full_v4.1.fits```, the main source of error comes from the calculation of rest frame colours using the EAZY code. We calculate errors using the error template function for the EAZY code found in Brammer et al (2006)[7], Figure 3. We used the effective mid point wavelengths of the U, V and J bands (365, 551, 1220nm) to find the error in flux using Fig 3 of [7], this was then propagated to find the error in magnitude resulting in the above values.

ID is the row number in the main GZ+UVISTA.fits table and is used to match output to Galaxy Zoo morphology to weight output.

Running the multirun smethhurst command in this directory with a queue and number of nodes specfied will run starpy for each of the set of params in params.txt deleting rows in param.txt when the have been computed and output saved. An example of a run command is below

```
addqueuecmb "mulit-run" 2 /usr/local/shared/bin/multirunsmethurst
```
adds a job to th cmb queue using 2 cores, running all the sets of parameters found in ``params.txt``.

I've run this over the whole COSMOS sample that we have GZH morphologies for. Saved on my glamdring account is the following output. Walker positions named as:

```
samples_...
```

and corresponding logrithmic probabilities named as 

```
lnprob_...
```

* ``process.py`` combines all the starpyoutput on glamdring. Drops walker postions with probabilty < 0.2 and also weights by the logrithmic probabilty. Can be modified to weight by GZH morpholgy, split by redshift and by enviroment. Outputs a final 2-d array to by plotted on a 2D-hist showing weight walker postions. This code is run out the glamdring and final output copied across.

* ``plot.py`` plots the 2D-hist of and marginal 1D histograms of the final combined starpy output produced by ``process.py``. Plots are smoothed. Needs corner.py installed see [here](https://github.com/dfm/corner.py). This code is run off the glamdring.

* ``process-out/`` output from ``process.py``. for galaxies weighted by GZH morphology, and split by overdensity for two redshift bins.

* ``plots/`` Corresponding plots for all the output in ``process-out/``, again 2D-hists are smoothed.

## Summary of Main Results

* Star-forming population is nearly completely abscent of featured galaxies. (See Muzzin Fig9)

* Across over density star formation rate is lower and approx constant for smooth galaxies, whereas specific star formation rate is lower for featured galaxies. In contradiction to Darvish et al (2016) which suggest decline across over density. Higher redshift high SFR and sSFR. (See Darvish2016Fig1)

* When binned by stellar mass, smooth galaxies have a lower SFR across over-density. Over both redshift bins. Higher redshift has higher SFR generally across stellar mass bins. (See Darvish2016Fig1)

* SHF isn't dependant on smooth / featured morphology. Even for red type galaxies only. Red type were selected by plotting distribution of VmJ colour and dividing bimodal population by eye VmJ < 0.95. (see starpyplots)

* SHF is dependant on enviroment. For low bin redshift (0-0.5) Med-High over-densities mean lower tq. Larger hump in tq. Low over-density no hump in tq.

## Current Issues and To-do list

* Colour Degeneracy plots don't match starpy output, why?

### Screen shots of the ipython notebook for my U-V , V-J lookup tables.

![alt text](https://github.com/petermcgill94/SFH-COSMOS/blob/master/Screen%20Shot%202016-08-11%20at%2015.22.02.png)

![alt text](https://github.com/petermcgill94/SFH-COSMOS/blob/master/Screen%20Shot%202016-08-11%20at%2015.22.37.png)

![alt text](https://github.com/petermcgill94/SFH-COSMOS/blob/master/screen_shot_2016-08-11_at_15.22.42_720.png)

### Example Starpy output plot

![alt text](https://github.com/petermcgill94/SFH-COSMOS/blob/master/examplestarpy.png)

* Possible fixes - axes error, I'm not forcing (0,0) to be at bottom left - will investigate today.
* I'm having to do a lot of smoothing to get rid of the vertical lines in the plot above is that a problem, why might this be happening?
* All my UVJ Colours have a constant error from the.EAZY code used to claculate the rest frame colours, the justification for this was that EAZY code error >> aperture flux for U,V and J bands in the data tables, might this be an issue?

### Other issues
* Intersection of galaxies with enviroment and GZ morphology data is small, possibly use GZ morphology as a tracer for over density?
* Better way of splitting galxies by enviroment thant just dividing them in to arbitrary bins.


## References
[1] Darvish, Behnam, et al. "A comparative study of density field estimation for galaxies: New insights into the evolution of galaxies with environment in cosmos out to Z∼ 3." The Astrophysical Journal 805.2 (2015): 121. DOI:
[10.1088/0004-637X/805/2/121](10.1088/0004-637X/805/2/121)

[2] Muzzin, Adam, et al. "A PUBLIC Ks-SELECTED CATALOG IN THE COSMOS/ULTRAVISTA FIELD: PHOTOMETRY, PHOTOMETRIC REDSHIFTS, AND STELLAR POPULATION PARAMETERS. The Astrophysical Journal Supplement Series 206.1 (2013): 8. DOI: [10.1088/0067-0049/206/1/8](10.1088/0067-0049/206/1/8)

[3] Galaxy Zoo: Morphological Classifications for 120,000 Galaxies in HST Legacy Imaging Paper current being written can be found in this [repo](https://github.com/willettk/gzhubble/blob/master/writeup/gz_hubble_data.pdf)

[4] Muzzin, Adam, et al. "THE EVOLUTION OF THE STELLAR MASS FUNCTIONS OF STAR-FORMING AND QUIESCENT GALAXIES TO z= 4 FROM THE COSMOS/UltraVISTA SURVEYBased on data products from observations made with ESO Telescopes at the La Silla Paranal Observatory under ESO programme ID 179. A-2005 and on data products produced by TERAPIX and the Cambridge Astronomy Survey Unit on behalf of the UltraVISTA consortium." The Astrophysical Journal 777.1 (2013): 18. DOI: [10.1088/0004-637X/777/1/18](10.1088/0004-637X/777/1/18)

[5] Kauffmann, Guinevere, et al. "The dependence of star formation history and internal structure on stellar mass for 105 low-redshift galaxies." Monthly Notices of the Royal Astronomical Society 341.1 (2003): 54-69. DOI:
[10.1046/j.1365-8711.2003.06292.x](10.1046/j.1365-8711.2003.06292.x)

[6] Darvish, Behnam, et al. "Effects of Local Environment and Stellar Mass on Galaxy Quenching out to z~ 3." arXiv preprint arXiv:1605.03182 (2016). DOI: [10.3847/0004-637X/825/2/113](10.3847/0004-637X/825/2/113)

[7] Brammer, Gabriel B., Pieter G. van Dokkum, and Paolo Coppi. "EAZY: A fast, public photometric redshift code." The Astrophysical Journal 686.2 (2008): 1503. DOI [10.1086/591786](10.1086/591786)

[8] Apellaniz, J. Maiz. "A recalibration of optical photometry: Tycho-2, Strömgren, and Johnson systems." The Astronomical Journal 131.2 (2006): 1184. DOI: [10.1086/499158](10.1086/499158)
