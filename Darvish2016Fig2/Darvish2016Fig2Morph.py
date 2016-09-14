###############################################################################
# Peter McgiLL 07/16                                                          #
# code to plot Figure 2 from Darvish et al 2016 out to z - 0.8, using GZ +    #
# uvista data, split by morphology                                            #
###############################################################################


import math
import numpy
import matplotlib.pyplot as plt
from astropy.table import Table, Column
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter


#define column names.
smoothCol= 't01_smooth_or_features_a01_smooth_weighted_fraction'
featureCol = 't01_smooth_or_features_a02_features_or_disk_weighted_fraction'

#extract data
dataAll = Table.read('../data/GZ+Darvish+UVISTA+clean.fits')

#remove SFRs upper limit values
sfrmask = dataAll['SFR_IR'] > 0
dataAll = dataAll[sfrmask]

#mass limits
masslower = [9.13,9.5,9.8,10.2,10.7]
massupper = [9.5,9.8,10.2,10.7,1000]

#plot parameters
colours = ['red','green','blue','black','m']
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

#middle of bins for lodgel
logdeldata = numpy.arange(-0.5,1.9,0.2)

################################0.1 < z < 0.5 #################################
###############################################################################

################## Smooth #####################################################

#pick featured galaxies accrond to threshold specified by GZH,
smask = dataAll[smoothCol] >= 0.8
dataAlls = dataAll[smask]

#set red shift
lowerz = dataAlls['z_peak'] > 0.1
upperz = dataAlls['z_peak'] < 0.5
zmask = (lowerz == 1) & (upperz == 1)
dataz = dataAlls[zmask]

#iterate over mass splits splits
for j in range(0,5):
    medlsfr = []
    medlssfr = []

    lowerm = dataz['LMASS_1'] > masslower[j]
    upperm = dataz['LMASS_1'] < massupper[j]
    #use = dataAll['USE_1'] == 1
    mmask = (lowerm == 1) & (upperm == 1)
    datam = dataz[mmask]

    # for each m find median in logdel bin of width 0.2
    for i in range(0,12):
        logdelHigh = datam['logdel'] > -0.6 + (i*0.2)
        logdelLow = datam['logdel'] < -0.4 + (i*0.2)
        logdelmask1 = (logdelHigh == 1) & (logdelLow == 1)
        dataFinal = datam[logdelmask1]
        medlsfr.append(numpy.median(numpy.log10(dataFinal['SFR_tot'])))

    ax1.scatter(logdeldata,medlsfr,color=colours[j],marker='o',s=40)
    ax1.plot(logdeldata,medlsfr,color=colours[j],label=str(masslower[j]) + '<M<' + str(massupper[j]))

ax1.set_xlabel(r'$\log(1+\delta)$')
ax1.set_ylabel(r'$\log(SFR)(M_{sol}yr^{-1})$')
ax1.set_title(r'$0.1<z<0.5$')
ax1.legend(frameon=False,loc=3)

################## feature #####################################################

#pick featured galaxies accrond to threshold specified by GZH,
fmask = dataAll[featureCol] >= 0.7
dataAllf = dataAll[fmask]

#set red shift
lowerz = dataAllf['z_peak'] > 0.1
upperz = dataAllf['z_peak'] < 0.5
zmask = (lowerz == 1) & (upperz == 1)
dataz = dataAllf[zmask]

#iterate over mass splits splits
for j in range(0,5):
    medlsfr = []
    medlssfr = []

    lowerm = dataz['LMASS_1'] > masslower[j]
    upperm = dataz['LMASS_1'] < massupper[j]
    #use = dataAll['USE_1'] == 1
    mmask = (lowerm == 1) & (upperm == 1)
    datam = dataz[mmask]

    # for each m find median in logdel bin of width 0.2
    for i in range(0,12):
        logdelHigh = datam['logdel'] > -0.6 + (i*0.2)
        logdelLow = datam['logdel'] < -0.4 + (i*0.2)
        logdelmask1 = (logdelHigh == 1) & (logdelLow == 1)
        dataFinal = datam[logdelmask1]
        medlsfr.append(numpy.median(numpy.log10(dataFinal['SFR_tot'])))

    ax1.scatter(logdeldata,medlsfr,color=colours[j],marker='s',s=40)
    ax1.plot(logdeldata,medlsfr,color=colours[j],label=str(masslower[j]) + '<M<' + str(massupper[j]))

ax1.set_xlabel(r'$\log(1+\delta)$')
ax1.set_ylabel(r'$\log(SFR)(M_{sol}yr^{-1})$')
ax1.set_title(r'$0.1<z<0.5$')
#ax1.legend(frameon=False,loc=3)


################################0.5 < z < 0.8 #################################
###############################################################################

################## Smooth #####################################################

#pick featured galaxies accrond to threshold specified by GZH,
smask = dataAll[smoothCol] >= 0.8
dataAlls = dataAll[smask]

#set red shift
lowerz = dataAlls['z_peak'] > 0.5
upperz = dataAlls['z_peak'] < 0.8
zmask = (lowerz == 1) & (upperz == 1)
dataz = dataAlls[zmask]

#iterate over mass splits splits
for j in range(0,5):
    medlsfr = []
    medlssfr = []

    lowerm = dataz['LMASS_1'] > masslower[j]
    upperm = dataz['LMASS_1'] < massupper[j]
    #use = dataAll['USE_1'] == 1
    mmask = (lowerm == 1) & (upperm == 1)
    datam = dataz[mmask]

    # for each m find median in logdel bin of width 0.2
    for i in range(0,12):
        logdelHigh = datam['logdel'] > -0.6 + (i*0.2)
        logdelLow = datam['logdel'] < -0.4 + (i*0.2)
        logdelmask1 = (logdelHigh == 1) & (logdelLow == 1)
        dataFinal = datam[logdelmask1]
        medlsfr.append(numpy.median(numpy.log10(dataFinal['SFR_tot'])))

    ax2.scatter(logdeldata,medlsfr,color=colours[j],marker='o',s=40)
    ax2.plot(logdeldata,medlsfr,color=colours[j],label=str(masslower[j]) + '<M<' + str(massupper[j]))

#ax2.set_xlabel(r'$\log(1+\delta)$')
ax2.set_ylabel(r'$\log(SFR)(M_{sol}yr^{-1})$')
ax2.set_title(r'$0.1<z<0.5$')
#ax2.legend(frameon=False,loc=3)

################## feature #####################################################

#pick featured galaxies accrond to threshold specified by GZH,
fmask = dataAll[featureCol] >= 0.7
dataAllf = dataAll[fmask]

#set red shift
lowerz = dataAllf['z_peak'] > 0.5
upperz = dataAllf['z_peak'] < 0.8
zmask = (lowerz == 1) & (upperz == 1)
dataz = dataAllf[zmask]

#iterate over mass splits splits
for j in range(0,5):
    medlsfr = []
    medlssfr = []

    lowerm = dataz['LMASS_1'] > masslower[j]
    upperm = dataz['LMASS_1'] < massupper[j]
    #use = dataAll['USE_1'] == 1
    mmask = (lowerm == 1) & (upperm == 1)
    datam = dataz[mmask]

    # for each m find median in logdel bin of width 0.2
    for i in range(0,12):
        logdelHigh = datam['logdel'] > -0.6 + (i*0.2)
        logdelLow = datam['logdel'] < -0.4 + (i*0.2)
        logdelmask1 = (logdelHigh == 1) & (logdelLow == 1)
        dataFinal = datam[logdelmask1]
        medlsfr.append(numpy.median(numpy.log10(dataFinal['SFR_tot'])))

    ax2.scatter(logdeldata,medlsfr,color=colours[j],marker='s',s=40)
    ax2.plot(logdeldata,medlsfr,color=colours[j],label=str(masslower[j]) + '<M<' + str(massupper[j]))

#ax2.set_xlabel(r'$\log(1+\delta)$')
ax2.set_ylabel(r'$\log(SFR)(M_{sol}yr^{-1})$')
ax2.set_title(r'$0.5<z<0.8$')

plt.figtext(0.5,0.01,r'Circle: $f_{smooth}\geq 0.8$, Square: $f_{feature}\geq 0.7$',fontdict={'fontsize':15})

plt.savefig('Darvish2016Fig2Morph.pdf')
