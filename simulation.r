#install packages
#install.packages("maptools")
#install.packages("rgeos")
#install.packages("spatstat")

#load packages
library(maptools)
library(spatstat)

#number of simulations
nSim <- 99

#number of observed points
nPts <- 10000
minT <- minimum observed temporal coordinate
maxT <- maximum observed temporal coordinate

#initialize matrix
mat1 <- matrix(nrow = 0, ncol =4)
mat2 <- matrix(nrow = 0, ncol =4)

#coordinate reference system
crs1 <- CRS([spatial reference information])

#boundary polygon
bds <- readShapePoly([boundary of study area], proj4string=crs1)

#observed points
obs <- read.table([array of data points])

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#CSR with a temporal trend: randomize cases for each day. Timestamps are directly taken from original dataset. In other words: the temporal intensity of the point process is dictated by the original dengue fever dataset.
for (simNum in 0:nSim) {
pts1 <- rpoint(nPts, win = bds)
tempMat1 <- cbind(pts$x,pts$y,dengue$V3,replicate(nPts,simNum))
mat1 <- rbind(mat1,tempMat1)
}
write.table(mat1, paste("sim_CSR_tTrend.txt", sep = ","))
#-----------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------------------------
#CSTR
for (simNum in 0:nSim) {
  pts2 <- rpoint(nPts, win = bds)
  tempMat2 <- cbind(pts$x,pts$y,sample(minT:maxT,nPts,replace=T),replicate(nPts,simNum))
  mat2 <- rbind(mat2,tempMat2)
}
write.table(mat2, paste("sim_CSTR.txt", sep = ","))
#-----------------------------------------------------------------------------------------------------------------------------------------------------

