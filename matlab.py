import scipy.io as spio
import matplotlib.pyplot as plt
import os

import numpy as np

#load in a matlab file in the same folder
mat = spio.loadmat('xrd_data.mat', squeeze_me=True)
#extracting data from matlab file
angles = mat['angles']
datavector = mat['datavector']
four_peaks_locs = mat['four_peaks_locs']
four_peaks_height = mat['four_peaks_height']
sample_number = mat['sample_number']

#setting up plot text
plot_title = 'Omega/2Theta Scan of Sample #' + sample_number
SLn1_text = "SL-1: " + str(round(four_peaks_locs[0], 4))
SL_text = 'SL-0: ' + str(round(four_peaks_locs[1], 4))
Sub_text = 'Substrate: ' + str(round(four_peaks_locs[2], 4))
SLp1_text = 'SL+1: ' + str(round(four_peaks_locs[3], 4))

# creating chart with matplotlib
fig, ax = plt.subplots(1)
ax.semilogy(angles, datavector) #main plot
#lowest value is 4, highest is the largest peak
# but we want some white space, so extend the ylim
ax.set(xlim=(angles[0] + 1, angles[7000] - 1), ylim=(4, four_peaks_height[0]*100),
       xlabel='Omega/2Theta', ylabel='Intensity', title=plot_title)

# drawing arrows from text to peak
# located near the peak in terms oy y coord but a little higher, but x coord is standardized to either 0, 1/4, 3/4, 1 of the x axis 
ax.annotate(SLn1_text, xy=(four_peaks_locs[0], four_peaks_height[0]), xytext=(angles[0] + 1.1, four_peaks_height[0]*50),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=-45,angleB=0"))
ax.annotate(SL_text, xy=(four_peaks_locs[1], four_peaks_height[1]), xytext=(angles[2333], four_peaks_height[0]*50),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=-65,angleB=0"))
ax.annotate(Sub_text, xy=(four_peaks_locs[2], four_peaks_height[2]), xytext=(angles[3700], four_peaks_height[0]*50),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=-120,angleB=0"))
ax.annotate(SLp1_text, xy=(four_peaks_locs[3], four_peaks_height[3]), xytext=(angles[7000] - 1.5,
            four_peaks_height[0]*50), arrowprops=dict(arrowstyle="->",
                                                      connectionstyle="angle3,angleA=-120,angleB=0"))
#formatting chart to be prettier
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.patch.set_facecolor('white')
ax.tick_params(axis='x', which='both', top=False)
ax.tick_params(axis='y', which='both', right=False)

#show chart
plt.show()
