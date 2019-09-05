import os, numpy as np, settings as sett

#number of observed data points
numPts = 10000

#read multidimensional array of sample points with associated ST-density values
inArr = np.load("astkdeArr.npy") # [x,y,t,hs,ht,ks,kt]

#initialize output array
dim = inArr.shape
nRows = dim[0]*dim[1]*dim[2]
nCols = 7   #columns ID, x, y, t, STKDE, max clustering scale s, max clusteringscale t
outArr = np.zeros((nRows,nCols))

ID = 0
xIndex = 0
while xIndex < dim[0]:
    yIndex = 0
    while yIndex < dim[1]:
        tIndex = 0
        while tIndex < dim[2]:
            hs,ht = inArr[xIndex][yIndex][tIndex][3],inArr[xIndex][yIndex][tIndex][4]	#optimal spatial and temporal bandwidth
            ks,kt = inArr[xIndex][yIndex][tIndex][5],inArr[xIndex][yIndex][tIndex][6]	#spatial and temporal density

            outArr[ID][0] = ID                                      #id
            outArr[ID][1] = inArr[xIndex][yIndex][tIndex][0]        #x
            outArr[ID][2] = inArr[xIndex][yIndex][tIndex][1]        #y
            outArr[ID][3] = inArr[xIndex][yIndex][tIndex][2]        #z
            outArr[ID][4] = (1/(numPts*pow(hs,2)*ht))*(ks*kt)     #STKDE
            outArr[ID][5] = inArr[xIndex][yIndex][tIndex][3]		#max clustering scale s
            outArr[ID][6] = inArr[xIndex][yIndex][tIndex][4]		#max clustering scale t

            ID += 1
            tIndex += 1
        yIndex += 1
    xIndex += 1

# eliminate zeroes (sample points outside city limits)
outFile = open("aSTKDE.txt","w")
for i in outArr:
    if i[1] == 0 and i[2] == 0 and i[3]  == 0:
        pass
    else:
        outFile.write(str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]) + "," + str(i[6]) + "\n")
outFile.close()