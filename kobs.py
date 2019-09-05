#import modules
import sys
import numpy as np
import settings as sett
import helperFunctions as hFunc

# ------------------------------------------------------------------------------------------------------------
#initialize global variables
sett.init()

#------------------------------------------------------------------------------------------------------------
#

#------------------------------------------------------------------------------------------------------------
#read sample points
inArr1 = np.loadtxt([grid of sample points])

#read data points
inArr2 = np.load([numpy array of data points])

#------------------------------------------------------------------------------------------------------------
#spatial and temporal domain
mins = np.amin(inArr1, axis=0)
maxs = np.amax(inArr1, axis=0)
sett.xmin, sett.xmax, sett.ymin, sett.ymax, sett.tmin, sett.tmax = mins[0], maxs[0], mins[1], maxs[1], mins[2], maxs[2]

#number of gridpoints in each dimension
sett.xdim = int((sett.xmax-sett.xmin)/sett.xyRes) + 1
sett.ydim = int((sett.ymax-sett.ymin)/sett.xyRes) + 1
sett.tdim = int((sett.tmax-sett.tmin)/sett.tRes) + 1

#initialize multidimensional array containing full grid
fullGridArr = np.zeros((sett.xdim, sett.ydim, sett.tdim, 7))                                #stores coordinates
binGridArrSpace = np.zeros((sett.xdim, sett.ydim, sett.tdim, sett.hs_numbins))  #stores counts spatial
binGridArrTime = np.zeros((sett.xdim, sett.ydim, sett.tdim, sett.ht_numbins))  #stores counts temporal

# ------------------------------------------------------------------------------------------------------------
#for each grid point in inArr1, compute s/t index and store coordinates in full grid - outArr
for i in inArr1:

    indices = hFunc.coordToIndex(i[0],i[1],i[2])
    xIndex, yIndex, tIndex = indices[0]-1, indices[1]-1, indices[2]-1

    fullGridArr[xIndex][yIndex][tIndex][0] = i[0]    # x-coord
    fullGridArr[xIndex][yIndex][tIndex][1] = i[1]    # y-coord
    fullGridArr[xIndex][yIndex][tIndex][2] = i[2]    # t-coord

# ------------------------------------------------------------------------------------------------------------
# compute ST k-function

# for each data point
for i in inArr2:
    #create list of neighbors: x,y,t coords witin hs_max, ht_max of data point
    x,y,t = i[0],i[1],i[2]
    nGridPts = hFunc.xytWithin(x,y,t)   #list of indexes for inArr1

    #for each neighbor, check whether within hs and ht
    for j in nGridPts:
        #retrieve grid point coordinates
        iX, iY, iT = j[0],j[1],j[2]     #indexes
        xC,yC,tC = fullGridArr[iX][iY][iT][0], fullGridArr[iX][iY][iT][1], fullGridArr[iX][iY][iT][2]   #coordinates

        #compute space-time distance
        stDist = hFunc.dist([x,y,t],[xC,yC,tC])
        sDist, tDist = stDist[0], stDist[1]

        #if st-distance smaller than st-bandwidths
        if sDist <= sett.hs_max and tDist <= sett.ht_max:

            # compute bin
            bwCount_s = int(sDist / sett.hs_binsize)
            bwCount_t = int(tDist/ sett.ht_binsize)
						
            for k in range(0, bwCount_s+1):
                binGridArrSpace[iX][iY][iT][k] += 1
            for i in range(0,bwCount_t):
                binGridArrTime[iX][iY][iT][i] += 1

np.save("obs/binGridArrSpace", binGridArrSpace)
np.save("obs/binGridArrTime", binGridArrTime)
np.save("obs/fullGridArr", fullGridArr)