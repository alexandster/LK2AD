#import modules
import os, numpy as np
from datetime import datetime

#number of simulations
numSim = 99

#read observed local k function
obsArrS = np.load([binGridArrSpace.npy])
obsArrT = np.load([binGridArrTime.npy])

#initialize zero array and infinity array
maxArrS = np.zeros(obsArrS.shape)
maxArrT = np.zeros(obsArrT.shape)

#find simulation envelopes
i = 0

while i<numSim:

    simArrS = np.load("sim/binGridArrSpace" + str(i) + ".npy")
    simArrT = np.load("sim/binGridArrTime" + str(i) + ".npy")

    maxArrS_1 = np.amax(np.stack([maxArrS, simArrS]),axis=0)
    maxArrS = maxArrS_1
	
    maxArrT_1 = np.amax(np.stack([maxArrT, simArrT]),axis=0)
    maxArrT = maxArrT_1

    i += 1

#compute differences between observed local k function and simulation envelopes
np.save('obs_max_S', np.subtract(obsArrS,maxArrS))	#difference between observed and upper envelope space
np.save('obs_max_T', np.subtract(obsArrT,maxArrT))	#difference between observed and upper envelope time

np.save('maxArr_S', maxArrS)	#upper envelope space
np.save('maxArr_T', maxArrT)	#upper envelope time
