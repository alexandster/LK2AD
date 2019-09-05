# settings.py

def init():
    global hs_binsize, hs_numbins, hs_max, ht_binsize, ht_numbins, ht_max, xyRes, tRes, xmin, xmax, ymin, ymax, tmin, tmax, xdim, ydim, tdim
    hs_binsize = [...]                        # spatial bin size
    hs_numbins = [...]                         # number of spatial bins
    hs_max = hs_binsize * hs_numbins        # maximum spatial bandwidth
    ht_binsize = [...]                          # temporal bin size
    ht_numbins = [...]                         # number of temporal bins
    ht_max = ht_binsize * ht_numbins        # maximum temporal bandwidth
    xyRes = [...]                            #spatial resolution
    tRes = [...]                                #temporal resolution


