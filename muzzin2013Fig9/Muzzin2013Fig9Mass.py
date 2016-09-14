#!/usr/bin/env python

###############################################################################
# Peter mcgill
# code to plot muzzin et al 2013 fig 9 split by mass accordin to kauffman et al
# 2003. <> log(M/M_sol) <> 10. -> lmass_1 in data table.
###############################################################################




import matplotlib.pyplot as plt
import numpy
#from latexify import latexify
from astropy.table import Table, Column
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter


dataAll = Table.read('../data/GZ+UVISTA.fits', format='fits')



###############################################################################
##################################0<z<0.5######################################
upperMask1 = 0.5 > dataAll['z_peak']
lowerMask1 = 0.0 < dataAll['z_peak']
useMask1 = dataAll['USE_1'] == 1

#select by lmass < 11 >11 (lmass = log (StellaMass/SOlMass)) split accordin to
# kauffman et al 2003.
lowMassMask1 = dataAll['LMASS_1'] < 10
highMassMask1 = dataAll['LMASS_1'] > 10

#combine all masks and make data sub set for potting
totalMaskHM1 = (upperMask1 == 1) & (lowerMask1 == 1) & (useMask1 == 1) & (highMassMask1==1)
totalMaskLM1 = (upperMask1 == 1) & (lowerMask1 == 1) & (useMask1 == 1) & (lowMassMask1==1)

#high and low mass data.
dataHM1 = dataAll[totalMaskHM1]
dataLM1 = dataAll[totalMaskLM1]

#get U-V and V-J data.
UminusVHM1 = dataHM1['UmV']
VminusJHM1 = dataHM1['VmJ']

UminusVLM1 = dataLM1['UmV']
VminusJLM1 = dataLM1['VmJ']

sampleSize1 = len(VminusJHM1) + len(VminusJLM1)

###############################################################################
##################################0.5<z<1.0######################################
upperMask2 = 1.0 > dataAll['z_peak']
lowerMask2 = 0.5 < dataAll['z_peak']
useMask2 = dataAll['USE_1'] == 1

#select by lmass < 11 >11 (lmass = log (StellaMass/SOlMass)) split accordin to
# kauffman et al 2003.
lowMassMask2 = dataAll['LMASS_1'] < 10
highMassMask2 = dataAll['LMASS_1'] > 10

#combine all masks and make data sub set for potting
totalMaskHM2 = (upperMask2 == 1) & (lowerMask2 == 1) & (useMask2 == 1) & (highMassMask2==1)
totalMaskLM2 = (upperMask2 == 1) & (lowerMask2 == 1) & (useMask2 == 1) & (lowMassMask2==1)

#high and low mass data.
dataHM2 = dataAll[totalMaskHM2]
dataLM2 = dataAll[totalMaskLM2]

#get U-V and V-J data.
UminusVHM2 = dataHM2['UmV']
VminusJHM2 = dataHM2['VmJ']

UminusVLM2 = dataLM2['UmV']
VminusJLM2 = dataLM2['VmJ']

sampleSize2 = len(VminusJHM2) + len(VminusJLM2)

###############################################################################
##################################1.0<z<1.5#####################################
upperMask3 = 1.5 > dataAll['z_peak']
lowerMask3 = 1.0 < dataAll['z_peak']
useMask3 = dataAll['USE_1'] == 1

#select by lmass < 11 >11 (lmass = log (StellaMass/SOlMass)) split accordin to
# kauffman et al 2003.
lowMassMask3 = dataAll['LMASS_1'] < 10
highMassMask3 = dataAll['LMASS_1'] > 10

#combine all masks and make data sub set for potting
totalMaskHM3 = (upperMask3 == 1) & (lowerMask3 == 1) & (useMask3 == 1) & (highMassMask3==1)
totalMaskLM3 = (upperMask3 == 1) & (lowerMask3 == 1) & (useMask3 == 1) & (lowMassMask3==1)

#high and low mass data.
dataHM3 = dataAll[totalMaskHM3]
dataLM3 = dataAll[totalMaskLM3]

#get U-V and V-J data.
UminusVHM3 = dataHM3['UmV']
VminusJHM3 = dataHM3['VmJ']

UminusVLM3 = dataLM3['UmV']
VminusJLM3 = dataLM3['VmJ']

sampleSize3 = len(VminusJHM3) + len(VminusJLM3)

###############################Plots###########################################


myxlim= [-0.5,2.0]
myylim= [0,2.5]
majorLocator   = MultipleLocator(0.5)

ax=plt.subplot(131)
ax.text(-0.25, 2.25, r'$0<z<0.5$', fontsize=10)
ax.text(-0.25,2.10,r'N='+ str(sampleSize1),fontsize=10)
ax.scatter(VminusJHM1,UminusVHM1,s=0.01,color='green')
ax.scatter(VminusJLM1,UminusVLM1,s=0.01,color='orange')
ax.set_xlim(myxlim)
ax.set_ylim(myylim)
ax.set_xlabel(r'$V-J$')
ax.set_ylabel(r'$U-V$')

ax=plt.subplot(132)
ax.text(-0.25, 2.25, r'$0.5<z<0.1$', fontsize=10)
ax.text(-0.25,2.10,r'N='+ str(sampleSize2),fontsize=10)
ax.scatter(VminusJHM2,UminusVHM2,s=0.01,color='green')
ax.scatter(VminusJLM2,UminusVLM2,s=0.01,color='orange')
ax.set_xlim(myxlim)
ax.set_ylim(myylim)
ax.xaxis.set_major_formatter( NullFormatter() )
ax.yaxis.set_major_formatter( NullFormatter() )

ax=plt.subplot(133)
ax.text(-0.25, 2.25, r'$1.0<z<1.5$', fontsize=10)
ax.text(-0.25,2.10,r'N='+ str(sampleSize3),fontsize=10)
ax.scatter(VminusJHM3,UminusVHM3,s=0.01,color='green')
ax.scatter(VminusJLM3,UminusVLM3,s=0.01,color='orange')
ax.set_xlim(myxlim)
ax.set_ylim(myylim)
ax.xaxis.set_major_formatter( NullFormatter() )
ax.yaxis.set_major_formatter( NullFormatter() )

plt.subplots_adjust(wspace=0,hspace=0)

plt.figtext(0.40,0.02,r'Green: $\log(M/M_{sol})>10$, Orange: $\log(M/M_{sol})<10$' ,fontdict={'fontsize':18})

plt.savefig('Muzzin2013Fig9Mass.pdf')
