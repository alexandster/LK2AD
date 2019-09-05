import settings as sett
import numpy as np
import math

# ------------------------------------------------------------------------------------------------------------
#initialize global variables
sett.init()

# ST Kernel density estimation
#--------------------------------------------------------------------------------------
def densityF(x, y, t, xi, yi, ti, hs, ht):
    u = (x-xi) / hs
    v = (y-yi) / hs
    w = (t-ti) / ht
    Ks = (2/math.pi)*(1 - pow(u, 2) - pow(v, 2))
    Kt = 0.75*(1 - pow(w, 2))
    STKDE = [Ks,Kt]
    return STKDE
#--------------------------------------------------------------------------------------

# function to convert coordinates to index for inArr
#--------------------------------------------------------------------------------------
def coordToIndex(x,y,t):
    xIndex = int((x-sett.xmin) / sett.xyRes)
    yIndex = int((y-sett.ymin) / sett.xyRes)
    tIndex = int((t-sett.tmin) / sett.tRes)
    return [xIndex, yIndex, tIndex]
#--------------------------------------------------------------------------------------

# function to create list of x,y,t coords witin hs, ht of data point
#--------------------------------------------------------------------------------------
def xytWithin(x,y,t):

    #minimum coords of neighborhood around data point
    xLo = x - sett.hs_max
    xHi = x + sett.hs_max
    yLo = y - sett.hs_max
    yHi = y + sett.hs_max
    tLo = t - sett.ht_max
    tHi = t + sett.ht_max

    #difference between xmin, ymin, tmin and closest grid point
    xminDiff = xLo % sett.xyRes
    xmaxDiff = xHi % sett.xyRes
    yminDiff = yLo % sett.xyRes
    ymaxDiff = yHi % sett.xyRes
    tminDiff = tLo % sett.tRes
    tmaxDiff = tHi % sett.tRes

    #first
    xminP = max(xLo - xminDiff + sett.xyRes, sett.xmin)
    xmaxP = min(xHi - xmaxDiff + sett.xyRes, sett.xmax)
    yminP = max(yLo - yminDiff + sett.xyRes, sett.ymin)
    ymaxP = min(yHi - ymaxDiff + sett.xyRes, sett.ymax)
    tminP = max(tLo - tminDiff + sett.tRes, sett.tmin)
    tmaxP = min(tHi - tmaxDiff + sett.tRes, sett.tmax)
    
    #grids
    xytGrid = []
    for i in np.arange(int(xminP),int(xmaxP),sett.xyRes):
        for j in np.arange(int(yminP),int(ymaxP),sett.xyRes):
            for k in np.arange(int(tminP), int(tmaxP), sett.tRes):
                xytGrid.append(coordToIndex(i,j,k))
    return xytGrid
# --------------------------------------------------------------------------------------

#distance function
#------------------------------------------------------------------------------------------------------------
def dist(p1,p2):
    return [pow(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2),0.5), abs(p1[2] - p2[2])]

#------------------------------------------------------------------------------------------------------------
