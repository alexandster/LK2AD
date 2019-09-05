import os, numpy as np, settings as sett, helperFunctions as hf

#load arrays
inArr = np.load("scale_obs_max.npy")                     # multidimensional array of grid points, optimal scales: x,y,t,hs,ht
daArr = np.load([numpy array of data points])         # data points
grArr = np.loadtxt([grid of sample points])		# sample points

#initialize global variables
sett.init()

#spatial and temporal domain
xdim = grArr[:,0]
ydim = grArr[:,1]
tdim = grArr[:,2]
sett.xmin, sett.xmax, sett.ymin, sett.ymax, sett.tmin, sett.tmax = min(xdim), max(xdim), min(ydim), max(ydim), min(tdim), max(tdim)

# for each data point
for i in daArr:
    #create list of neighbors: x,y,t coords witin hs_max, ht_max of data point
    x,y,t = i[0],i[1],i[2]
    nGridPts = hf.xytWithin(x,y,t)

    #for each neighbor, check whether within hs and ht (specific to neighbor, hence ADAPTIVE)
    for j in nGridPts:
        #access coordinates, hs, ht
        tempArr = inArr[j[0]][j[1]][j[2]]
        xC,yC,tC,hs,ht = tempArr[0],tempArr[1],tempArr[2],tempArr[3],tempArr[4]

        #compute space-time distance
        sDist = pow(pow(x-xC,2)+pow(y-yC,2),0.5)
        tDist = abs(t-tC)

        #if st-disntance smaller than st-bandwidths
        if sDist <= hs and tDist <= ht:
		
            #compute density contribution
            STKDE = hf.densityF(x, y, t, xC, yC, tC, hs, ht)

            inArr[j[0]][j[1]][j[2]][5] += STKDE[0]
            inArr[j[0]][j[1]][j[2]][6] += STKDE[1]
			
np.save("astkdeArr",inArr)



