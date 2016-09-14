###############################################################################
# Peter Mcgill 13.07.16                                                       #
# code to plot mezzin et al 2013 split by bar/ no bar morphology as specified #
# by GZH paper table 11 has thresholds.                                       #
###############################################################################


import matplotlib.pyplot as plt
import numpy
from astropy.table import Table, Column
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter


dataAll = Table.read('../data/GZ+UVISTA.fits', format='fits')

#define column names.
featureCol = 't01_smooth_or_features_a02_features_or_disk_weighted_fraction'
edgeonnoCol ='t02_edgeon_a05_no_weighted_fraction'
clumpynoCol = 't14_clumpy_a40_no_weighted_fraction'
barCol ='t03_bar_a06_bar_weighted_fraction'

###############################################################################
##################################0<z<0.5######################################
upperMask1 = 0.5 > dataAll['z_peak']
lowerMask1 = 0.0 < dataAll['z_peak']
useMask1 = dataAll['USE_1'] == 1

#sampled by bar fractoin and all previous tasks specified by GZH paper table
# 11.
fMask = dataAll[featureCol] >= 0.23
cMask = dataAll[clumpynoCol] >= 0.30
eMask = dataAll[edgeonnoCol] >= 0.25
bMask = dataAll[barCol] >= 0.8
totalBarMask = (fMask==1) & (cMask==1) & (eMask==1) & (bMask==1)

#combine all masks and make data sub set for potting
totalMaskB1 = (upperMask1 == 1) & (lowerMask1 == 1) & (useMask1 == 1) & (totalBarMask==1)
totalMaskNB1 = (upperMask1 == 1) & (lowerMask1 == 1) & (useMask1 == 1) & (totalBarMask==0)

#high and low mass data.
dataB1 = dataAll[totalMaskB1]
dataNB1 = dataAll[totalMaskNB1]

#get U-V and V-J data.
UminusVB1 = dataB1['UmV']
VminusJB1 = dataB1['VmJ']

UminusVNB1 = dataNB1['UmV']
VminusJNB1 = dataNB1['VmJ']

sampleSize1 = len(VminusJB1) + len(VminusJNB1)

###############################################################################
##################################0.5<z<1.0######################################
upperMask2 = 1.0 > dataAll['z_peak']
lowerMask2 = 0.5 < dataAll['z_peak']
useMask2 = dataAll['USE_1'] == 1

#sampled by bar fractoin and all previous tasks specified by GZH paper table
# 11.
fMask = dataAll[featureCol] >= 0.23
cMask = dataAll[clumpynoCol] >= 0.30
eMask = dataAll[edgeonnoCol] >= 0.25
bMask = dataAll[barCol] >= 0.8
totalBarMask = (fMask==1) & (cMask==1) & (eMask==1) & (bMask==1)

#combine all masks and make data sub set for potting
totalMaskB2 = (upperMask2 == 1) & (lowerMask2 == 1) & (useMask1 == 1) & (totalBarMask==1)
totalMaskNB2 = (upperMask2 == 1) & (lowerMask2 == 1) & (useMask2 == 1) & (totalBarMask==0)

#high and low mass data.
dataB2 = dataAll[totalMaskB2]
dataNB2 = dataAll[totalMaskNB2]

#get U-V and V-J data.
UminusVB2 = dataB2['UmV']
VminusJB2 = dataB2['VmJ']

UminusVNB2 = dataNB2['UmV']
VminusJNB2 = dataNB2['VmJ']

sampleSize2 = len(VminusJB2) + len(VminusJNB2)

###############################################################################
##################################1.0<z<1.5######################################
upperMask3 = 1.5 > dataAll['z_peak']
lowerMask3 = 1.0 < dataAll['z_peak']
useMask3 = dataAll['USE_1'] == 1

#sampled by bar fractoin and all previous tasks specified by GZH paper table
# 11.
fMask = dataAll[featureCol] >= 0.23
cMask = dataAll[clumpynoCol] >= 0.30
eMask = dataAll[edgeonnoCol] >= 0.25
bMask = dataAll[barCol] >= 0.8
totalBarMask = (fMask==1) & (cMask==1) & (eMask==1) & (bMask==1)

#combine all masks and make data sub set for potting
totalMaskB3 = (upperMask3 == 1) & (lowerMask3 == 1) & (useMask3 == 1) & (totalBarMask==1)
totalMaskNB3 = (upperMask3 == 1) & (lowerMask3 == 1) & (useMask3 == 1) & (totalBarMask==0)

#high and low mass data.
dataB3 = dataAll[totalMaskB3]
dataNB3 = dataAll[totalMaskNB3]

#get U-V and V-J data.
UminusVB3 = dataB3['UmV']
VminusJB3 = dataB3['VmJ']

UminusVNB3 = dataNB3['UmV']
VminusJNB3 = dataNB3['VmJ']

sampleSize3 = len(VminusJB3) + len(VminusJNB3)

######################Plots####################################################
myxlim= [-0.5,2.0]
myylim= [0,2.5]
majorLocator   = MultipleLocator(0.5)
#majorFormatter = FormatStrFormatter('%d')

ax=plt.subplot(131)
ax.text(-0.25, 2.25, r'$0<z<0.5$', fontsize=10)
ax.text(-0.25,2.10,r'N='+ str(sampleSize1),fontsize=10)
ax.scatter(VminusJB1,UminusVB1,s=0.9,color='black',label=r'$f_{smooth}\geq 0.8$')
ax.scatter(VminusJNB1,UminusVNB1,s=0.1,color='red',label=r'$f_{feature}\geq 0.7$')
ax.set_xlabel(r'$V-J$')
ax.set_ylabel(r'$U-V$')
ax.set_xlim(myxlim)
ax.set_ylim(myylim)


ax=plt.subplot(132)
ax.text(-0.25, 2.25, r'$0<z<0.5$', fontsize=10)
ax.text(-0.25,2.10,r'N='+ str(sampleSize2),fontsize=10)
ax.scatter(VminusJB2,UminusVB2,s=0.9,color='black',label=r'$f_{smooth}\geq 0.8$')
ax.scatter(VminusJNB2,UminusVNB2,s=0.1,color='red',label=r'$f_{feature}\geq 0.7$')
ax.set_xlim(myxlim)
ax.set_ylim(myylim)
ax.xaxis.set_major_formatter( NullFormatter() )
ax.yaxis.set_major_formatter( NullFormatter() )

ax=plt.subplot(133)
ax.text(-0.25, 2.25, r'$0<z<0.5$', fontsize=10)
ax.text(-0.25,2.10,r'N='+ str(sampleSize3),fontsize=10)
ax.scatter(VminusJB3,UminusVB3,s=0.9,color='black',label=r'$f_{smooth}\geq 0.8$')
ax.scatter(VminusJNB3,UminusVNB3,s=0.1,color='red',label=r'$f_{feature}\geq 0.7$')

ax.set_xlim(myxlim)
ax.set_ylim(myylim)
ax.xaxis.set_major_formatter( NullFormatter() )
ax.yaxis.set_major_formatter( NullFormatter() )

plt.figtext(0.30,0.02,r'Red: Not Bar, Black: Bar (as specified by GZH paper Table 11)',fontdict={'fontsize':18})

plt.subplots_adjust(wspace=0,hspace=0)
plt.savefig('Muzzin2013Fig9bar.pdf')
