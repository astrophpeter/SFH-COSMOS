# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table, Column
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter
import matplotlib.gridspec as gridspec
plt.style.use('idl.mplstyle')

dataAll = Table.read('../data/GZ+UVISTA.fits', format='fits')



#define column names.
smoothCol= 't01_smooth_or_features_a01_smooth_weighted_fraction'
featureCol = 't01_smooth_or_features_a02_features_or_disk_weighted_fraction'

###############################################################################
##################################0<z<0.5######################################
upperMask1 = 0.5 > dataAll['z_peak']
lowerMask1 = 0.0 < dataAll['z_peak']
useMask1 = dataAll['USE_1'] == 1
sMask1 = dataAll[smoothCol] >= 0.8
fMask1 = dataAll[featureCol] >= 0.7
#combine all masks and make data sub set for potting
totalMaskS1 = (upperMask1 == 1) & (lowerMask1 == 1) & (useMask1 == 1) & (sMask1 == 1)
totalMaskF1 = (upperMask1 == 1) & (lowerMask1 == 1) & (useMask1 == 1) & (fMask1 == 1)
dataSmooth1 = dataAll[totalMaskS1]
dataFeature1 = dataAll[totalMaskF1]
#get U-V and V-J data.
UminusVS1 = dataSmooth1['UmV']
VminusJS1 = dataSmooth1['VmJ']
UminusVF1 = dataFeature1['UmV']
VminusJF1 = dataFeature1['VmJ']
sampleSize1 = len(VminusJF1) + len(VminusJS1)

###############################################################################
##################################0.5<z<1.0#####################################
upperMask2 = 1.0 > dataAll['z_peak']
lowerMask2 = 0.5 < dataAll['z_peak']
useMask2 = dataAll['USE_1'] == 1
sMask2 = dataAll[smoothCol] >= 0.8
fMask2 = dataAll[featureCol] >= 0.7
#combine all masks and make data sub set for potting
totalMaskS2 = (upperMask2 == 1) & (lowerMask2 == 1) & (useMask2 == 1) & (sMask2 == 1)
totalMaskF2 = (upperMask2 == 1) & (lowerMask2 == 1) & (useMask2 == 1) & (fMask2 == 1)
dataSmooth2 = dataAll[totalMaskS2]
dataFeature2 = dataAll[totalMaskF2]
#get U-V and V-J data.
UminusVS2 = dataSmooth2['UmV']
VminusJS2 = dataSmooth2['VmJ']
UminusVF2 = dataFeature2['UmV']
VminusJF2 = dataFeature2['VmJ']
sampleSize2 = len(VminusJF2) + len(VminusJS2)

###############################################################################
##################################1.0<z<1.5#####################################
upperMask3 = 1.5 > dataAll['z_peak']
lowerMask3 = 1.0 < dataAll['z_peak']
useMask3 = dataAll['USE_1'] == 1
sMask3 = dataAll[smoothCol] >= 0.8
fMask3 = dataAll[featureCol] >= 0.7
#combine all masks and make data sub set for potting
totalMaskS3 = (upperMask3 == 1) & (lowerMask3 == 1) & (useMask3 == 1) & (sMask3 == 1)
totalMaskF3 = (upperMask3 == 1) & (lowerMask3 == 1) & (useMask3 == 1) & (fMask3 == 1)
dataSmooth3 = dataAll[totalMaskS3]
dataFeature3 = dataAll[totalMaskF3]
#get U-V and V-J data.
UminusVS3 = dataSmooth3['UmV']
VminusJS3 = dataSmooth3['VmJ']
UminusVF3 = dataFeature3['UmV']
VminusJF3 = dataFeature3['VmJ']
sampleSize3 = len(VminusJF3) + len(VminusJS3)

num_x_bins = 50
num_y_bins = 50

# Axes definitions
nullfmt = plt.NullFormatter()
left, width = 0.1, 0.4
bottom, height = 0.1, 0.4
bottom_h = left_h = left + width

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# Generate initial figure, scatter plot, and histogram quadrants


#ax.set_xlabel(r"Normal text vs. ${\rm math\, text}$")
#ax.set_ylabel(r"A B C $\alpha$ $\beta$ $\gamma$")

#
# Turn on minor ticks!!
#


plt.figure(figsize=(12,6))




gs1 = gridspec.GridSpec(2,5,width_ratios=[3,1,1,3,1],
                       height_ratios=[1,3])
axScatter = plt.subplot(gs1[5])
gs1.update(hspace=0.00,wspace=0.0)
axScatter.minorticks_on()
axScatter.set_xlabel(r'$V-J$')
axScatter.set_ylabel(r'$U-V$')
axScatter.set_xlim(-0.5, 2.)
axScatter.set_ylim(0., 2.5)
axScatter.text(-0.25, 2.20, r'$0<z<0.5$')
axScatter.text(-0.25,2.0,r'$N=$'+str(sampleSize1))
axScatter.text(-0.13,1.8,r'$p_{s}>0.8$')
axScatter.scatter([-0.21],[1.84],marker='o',color='red')
axScatter.text(-0.13,1.6,r'$p_{f}>0.7$')
axScatter.scatter([-0.21],[1.64],marker='o',color='blue')

axHistX = plt.subplot(gs1[0])
axHistX.set_xlim(-0.5, 2.)
axHistX.set_ylim(0, 400)
axHistX.xaxis.set_major_formatter( NullFormatter() )
axHistX.yaxis.set_major_formatter( NullFormatter() )

axHistY = plt.subplot(gs1[6])
axHistY.set_xlim(0, 400)
axHistY.set_ylim(0, 2.5)
axHistY.xaxis.set_major_formatter( NullFormatter() )
axHistY.yaxis.set_major_formatter( NullFormatter() )

# Remove labels from histogram edges touching scatter plot
axHistX.xaxis.set_major_formatter(nullfmt)
axHistY.yaxis.set_major_formatter(nullfmt)

# Draw scatter plot
axScatter.scatter(dataSmooth1['VmJ'],dataSmooth1['UmV'], marker='o', color = 'red', edgecolor='none', s=0.8, alpha=1)
axScatter.scatter(dataFeature1['VmJ'],dataFeature1['UmV'], marker='o', color = 'blue', edgecolor='none', s=0.8, alpha=1)
axScatter.plot([-0.5,0.693182,1.5,1.5],[1.3,1.3,2.0,2.5],color='green')
axScatter.errorbar([1.5],[0.4],yerr=[0.099],xerr=[0.1399],color='black')

# Draw x-axis histogram
axHistX.hist(dataSmooth1['VmJ'], num_x_bins, color='red', histtype='step')
axHistX.hist(dataFeature1['VmJ'], num_x_bins,color='blue', histtype='step')
# Draw y-axis histogram
axHistY.hist(dataSmooth1['UmV'], num_y_bins, color='red', histtype='step', orientation='horizontal')
axHistY.hist(dataFeature1['UmV'], num_y_bins, color='blue', histtype='step', orientation='horizontal')

gs2 = gridspec.GridSpec(2, 5,width_ratios=[3,1,1,3,1],
                       height_ratios=[1,3])
gs2.update(hspace=0.00,wspace=0.0)
axScatter = plt.subplot(gs2[8])
axScatter.minorticks_on()
axScatter.set_xlabel(r'$V-J$')
axScatter.set_ylabel(r'$U-V$')
axScatter.set_xlim(-0.5, 2.)
axScatter.set_ylim(0., 2.5)
axScatter.text(-0.25, 2.20, r'$0.5<z<1.0$')
axScatter.text(-0.25,2.0,r'$N=$'+str(sampleSize2))
axScatter.text(-0.13,1.8,r'$p_{s}>0.8$')
axScatter.scatter([-0.21],[1.84],marker='o',color='red')
axScatter.text(-0.13,1.6,r'$p_{f}>0.7$')
axScatter.scatter([-0.21],[1.64],marker='o',color='blue')

axHistX = plt.subplot(gs2[3])
axHistX.set_xlim(-0.5, 2.)
axHistX.set_ylim(0, 400)
axHistX.xaxis.set_major_formatter( NullFormatter() )
axHistX.yaxis.set_major_formatter( NullFormatter() )

axHistY = plt.subplot(gs2[9])
axHistY.set_xlim(0, 400)
axHistY.set_ylim(0, 2.5)
axHistY.xaxis.set_major_formatter( NullFormatter() )
axHistY.yaxis.set_major_formatter( NullFormatter() )

# Remove labels from histogram edges touching scatter plot
axHistX.xaxis.set_major_formatter(nullfmt)
axHistY.yaxis.set_major_formatter(nullfmt)

# Draw scatter plot
axScatter.scatter(dataSmooth2['VmJ'],dataSmooth2['UmV'], marker='o', color = 'red', edgecolor='none', s=0.8, alpha=1)
axScatter.scatter(dataFeature2['VmJ'],dataFeature2['UmV'], marker='o', color = 'blue', edgecolor='none', s=0.8, alpha=1)
axScatter.plot([-0.5,0.693182,1.5,1.5],[1.3,1.3,2.0,2.5],color='green')
axScatter.errorbar([1.5],[0.4],yerr=[0.099],xerr=[0.1399],color='black')
# Draw x-axis histogram
axHistX.hist(dataSmooth2['VmJ'], num_x_bins, color='red', histtype='step')
axHistX.hist(dataFeature2['VmJ'], num_x_bins,color='blue', histtype='step')
# Draw y-axis histogram
axHistY.hist(dataSmooth2['UmV'], num_y_bins, color='red', histtype='step', orientation='horizontal')
axHistY.hist(dataFeature2['UmV'], num_y_bins, color='blue', histtype='step', orientation='horizontal')


plt.savefig('Muzzin2013Fig9Morph.pdf')


