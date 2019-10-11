# LK2AD
local space-time Ripley's K function parameterizes adaptive kernel density estimation

Required modules: 
numpy

Relevant Literature: 
Hohl, A., Zheng, M., Tang, W., Delmelle, E., & Casas, I. (2017). Spatiotemporal Point Pattern Analysis Using Ripley’s K Function. In: Karimi, H. A. & Karimi, B. (Eds.) Geospatial Data Science: Techniques and Applications. Taylor & Francis.

Alexander Hohl and Peilin Chen. 2019. Spatiotemporal Simulation: Local Ripley’s K Function Parameterizes Adaptive Kernel Density Estimation. In Proceedings of Geosim’19: 2nd ACM SIGSPATIAL International Workshop on Geospatial Simulation, Chicago, IL, USA, November 5, 2019 (GeoSim’19), 8 pages.
https://doi.org/10.1145/3356470.3365528


scripts:

helperFunctions.py - contains utility functions, such as for computing STKDE
settings.py - contains parameter settings relevant for all executing scripts

Execute in order

1. kobs.py - Computes observed local space-time k function.
2. ksim.py - Computes local space-time k function from n simulated datasets. Can be executed in parallel.
3. results_collect.py - Gathers results from observed and simulated local k functions, computes simulation envelopes, and differences between observed and simulated.
4. maxClustScale.py - Finds optimal bandwidths
5. aSTKDE.py - computes adaptive space-time kernel density estimation using optimal bandwidths determined previousely.
6. unroll_aSTKDE.py - Out 
