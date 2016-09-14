
#!/usr/bin/env python


###############################################################################
# Peter Mcgill 07.2016                                                        #
# Code to plot figure 1 of Darvish et al 2016 figure 1 (left), cna be modified#
# to plot meadian / mean sfr and ssfr.                                        #
###############################################################################

import math
import numpy
import matplotlib.pyplot as plt
from astropy.table import Table, Column
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter


#extract data
dataAll = Table.read('../data/GZ+Darvish+UVISTA+clean.fits')

#define column names.
smoothCol= 't01_smooth_or_features_a01_smooth_weighted_fraction'
featureCol = 't01_smooth_or_features_a02_features_or_disk_weighted_fraction'


#remove SFRs upper limit values
sfrmask = dataAll['SFR_IR'] > 0
dataAll = dataAll[sfrmask]

#test data
dataTest = Table()
#red shift splits
zmaxes = [0.5,0.8,1.1,1.5,2.0,3.1]
zmins = [0.1,0.5,0.8,1.1,1.5,2.0]

#visial parameters
colours = ['black','red', 'green','blue','pink','m']
markers = ['s','s','^','v','*','*']
markers2 = ['o','o']
#middle of bins for lodgel
logdeldata = numpy.arange(-0.5,1.9,0.2)





#define axes.
#ax1=plt.subplot(321)
#ax2=plt.subplot(322)
ax3=plt.subplot(121)
ax4=plt.subplot(122)
#ax5=plt.subplot(223)
#ax6=plt.subplot(224)
myxlim= [-1,1.5]
myylimsfr= [-1,1.1]
myylimssfr = [-11,-9]
###############################################################################
################################ All ##########################################


# iterate over z splits
#for j in range(0,2):
#    medlsfr = []
#    medlssfr = []
#    lowerz = dataAll['z_peak'] > zmins[j]
#    upperz = dataAll['z_peak'] < zmaxes[j]
#    #use = dataAll['USE_1'] == 1
#    zmask = (lowerz == 1) & (upperz == 1)
#    dataz1 = dataAll[zmask]

#    # for each z find median in logdel bin of width 0.2
#    for i in range(0,12):
#        logdelHigh = dataz1['logdel'] > -0.6 + (i*0.2)
#        logdelLow = dataz1['logdel'] < -0.4 + (i*0.2)
#        logdelmask1 = (logdelHigh == 1) & (logdelLow == 1)
#        dataFinal = dataz1[logdelmask1]
#        medlsfr.append(numpy.median(numpy.log10(dataFinal['SFR_tot'])))
#        medlssfr.append(numpy.median(numpy.log10(dataFinal['SFR_tot'])-dataFinal['LMASS_1']))

    # plot
#    ax1.scatter(logdeldata,medlsfr,color=colours[j],marker=markers[j],s=40)
#    ax1.plot(logdeldata,medlsfr,color=colours[j],label=str(zmins[j]) + '<z<' + str(zmaxes[j]))
#    ax1.set_xlabel(r'$\log(1+\delta)$')
#    ax1.set_ylabel(r'$\log(SFR)(M_{sol}yr^{-1}$)')
#    ax1.legend(frameon=False)

#    ax2.scatter(logdeldata,medlssfr,color=colours[j],marker=markers[j],s=40)
#    ax2.plot(logdeldata,medlssfr,color=colours[j],label=str(zmins[j]) + '<z<' + str(zmaxes[j]))
#    ax2.set_xlabel(r'$\log(1+\delta)$')
#    ax2.set_ylabel(r'$\log(sSFR)(yr^{-1}$)')
    #ax2.legend(frameon=False)


###############################################################################
###################################### feature ################################

#pick featured galaxies accrond to threshold specified by GZH,
fmask = dataAll[featureCol] >= 0.7
dataAllf = dataAll[fmask]


#iterate over z splits
for j in range(0,2):
    medlsfr = []
    medlssfr = []
    lowerz = dataAllf['z_peak'] > zmins[j]
    upperz = dataAllf['z_peak'] < zmaxes[j]
    #use = dataAll['USE_1'] == 1
    zmask = (lowerz == 1) & (upperz == 1)
    dataz1f = dataAllf[zmask]

    # for each z find median in logdel bin of width 0.2
    for i in range(0,12):
        logdelHigh = dataz1f['logdel'] > -0.6 + (i*0.2)
        logdelLow = dataz1f['logdel'] < -0.4 + (i*0.2)
        logdelmask1 = (logdelHigh == 1) & (logdelLow == 1)
        dataFinalf = dataz1f[logdelmask1]
        medlsfr.append(numpy.median(numpy.log10(dataFinalf['SFR_tot'])))
        medlssfr.append(numpy.median(numpy.log10(dataFinalf['SFR_tot'])-dataFinalf['LMASS_1']))

    # plot
    ax3.scatter(logdeldata,medlsfr,color=colours[j],marker=markers[j],s=40)
    ax3.plot(logdeldata,medlsfr,color=colours[j],label=str(zmins[j]) + '<z<' + str(zmaxes[j]))
    ax3.set_xlim(myxlim)
    ax3.set_ylim(myylimsfr)
    ax3.set_xlabel(r'$\log(1+\delta)$')
    ax3.set_ylabel(r'$\log(SFR)(M_{sol}yr^{-1}$)')
    #ax3.legend(frameon=False)

    ax4.scatter(logdeldata,medlssfr,color=colours[j],marker=markers[j],s=40)
    ax4.plot(logdeldata,medlssfr,color=colours[j],label=str(zmins[j]) + '<z<' + str(zmaxes[j]))
    ax4.set_xlim(myxlim)
    ax4.set_ylim(myylimssfr)
    #ax4.set_xlabel(r'$\log(1+\delta)$')
    ax4.set_ylabel(r'$\log(sSFR)(yr^{-1}$)')
    ax4.legend(frameon=False,loc=3)


###############################################################################
###################################### Smooth ################################

#pick featured galaxies accrond to threshold specified by GZH,
smask = dataAll[smoothCol] >= 0.8
dataAlls = dataAll[smask]


#iterate over z splits
for j in range(0,2):
    medlsfr = []
    medlssfr = []
    lowerz = dataAlls['z_peak'] > zmins[j]
    upperz = dataAlls['z_peak'] < zmaxes[j]
    #use = dataAll['USE_1'] == 1
    zmask = (lowerz == 1) & (upperz == 1)
    dataz1s = dataAlls[zmask]

    # for each z find median in logdel bin of width 0.2
    for i in range(0,12):
        logdelHigh = dataz1s['logdel'] > -0.6 + (i*0.2)
        logdelLow = dataz1s['logdel'] < -0.4 + (i*0.2)
        logdelmask1 = (logdelHigh == 1) & (logdelLow == 1)
        dataFinals = dataz1s[logdelmask1]
        medlsfr.append(numpy.median(numpy.log10(dataFinals['SFR_tot'])))
        medlssfr.append(numpy.median(numpy.log10(dataFinals['SFR_tot'])-dataFinals['LMASS_1']))

    # plot
    ax3.scatter(logdeldata,medlsfr,color=colours[j],marker=markers2[j],s=40)
    ax3.plot(logdeldata,medlsfr,color=colours[j],label=str(zmins[j]) + '<z<' + str(zmaxes[j]))
    ax3.set_xlim(myxlim)
    ax3.set_ylim(myylimsfr)
    #ax5.set_xlabel(r'$\log(1+\delta)$')
    #ax5.set_ylabel(r'$\log(SFR)(M_{sol}yr^{-1}$)')
    #ax5.legend(frameon=False)

    ax4.scatter(logdeldata,medlssfr,color=colours[j],marker=markers2[j],s=40)
    ax4.plot(logdeldata,medlssfr,color=colours[j],label=str(zmins[j]) + '<z<' + str(zmaxes[j]))
    ax4.set_xlim(myxlim)
    ax4.set_ylim(myylimssfr)
    #ax6.set_xlabel(r'$\log(1+\delta)$')
    #ax6.set_ylabel(r'$\log(sSFR)(yr^{-1}$)')
    #ax4.legend(frameon=False,loc=3)


plt.figtext(0.50,0.02,r'Circle: $f_{smooth}\geq 0.8$, Square: $f_{feature}\geq 0.7$',fontdict={'fontsize':18})
plt.subplots_adjust(wspace=0.25,hspace=0.25)
#plt.title(r'All (Darvish + UVISTA)')
#plt.xlabel(r'$\log(1+\delta)$')
#plt.ylabel(r'$\log(sSFR)(yr^{-1}$)')
plt.savefig('Darvish2016Fig1AllMorph.pdf')
