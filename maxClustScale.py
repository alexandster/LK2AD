#import modules
import os, numpy as np, settings as sett
from datetime import datetime

# ------------------------------------------------------------------------------------------------------------
# load array
inArrS = np.load("obs_max_S.npy")
inArrT = np.load("obs_max_T.npy")
outArr = np.load("fullGridArr.npy")

# ------------------------------------------------------------------------------------------------------------
#initialize global variables
sett.init()

# read sample points
inArr1 = np.loadtxt([grid of sample points])

# ------------------------------------------------------------------------------------------------------------
#spatial and temporal domain
mins = np.amin(inArr1, axis=0)
maxs = np.amax(inArr1, axis=0)
sett.xmin, sett.xmax, sett.ymin, sett.ymax, sett.tmin, sett.tmax = mins[0], maxs[0], mins[1], maxs[1], mins[2], maxs[2]

#number of gridpoints in each dimension
sett.xdim = int((sett.xmax-sett.xmin)/sett.xyRes) + 1
sett.ydim = int((sett.ymax-sett.ymin)/sett.xyRes) + 1
sett.tdim = int((sett.tmax-sett.tmin)/sett.tRes) + 1

# ------------------------------------------------------------------------------------------------------------
# produce map of spatial bandwidths
hs = sett.hs_binsize
iMapS = []

while hs <=sett.hs_max:
    iMapS.append(hs)
    hs += sett.hs_binsize
	
# ------------------------------------------------------------------------------------------------------------
# find scale of greatest difference between obs and simulation envelope
count = 0
for xIndex, xValue in enumerate(inArrS):
    for yIndex, yValue in enumerate(xValue):
        for tIndex, tValue in enumerate(yValue):
            maxIndex = np.argmax(abs(tValue))
            outArr[xIndex][yIndex][tIndex][3] = iMapS[maxIndex]
#--------------------------------------------------------------------------

# produce map of temporal bandwidths
ht = sett.ht_binsize
iMapT = []

while ht <=sett.ht_max:
    iMapT.append(ht)
    ht += sett.ht_binsize

# ------------------------------------------------------------------------------------------------------------
# find scale of greatest difference between obs and simulation envelope

for xIndex, xValue in enumerate(inArrT):
    for yIndex, yValue in enumerate(xValue):
        for tIndex, tValue in enumerate(yValue):
            maxIndex = np.argmax(abs(tValue))
            outArr[xIndex][yIndex][tIndex][4] = iMapT[maxIndex]

np.save("scale_obs_max", outArr)	#maximum clustering scales (hs/ht)