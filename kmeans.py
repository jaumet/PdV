##from __future__ import division
##from random import random
import sys
import pprint

def kmeans(data, clusters):
    ## Getting the means
    means =([])
    col2_lowest = 0
    col2_highest = 0
    col1 = {}
    col2 = []
    for x,y in data:
      if int(y) < col2_lowest or col2_lowest == 0: col2_lowest = int(y)
      if int(y) > col2_highest: col2_highest = int(y)
    ##print 'low', col2_lowest, 'high', col2_highest
    c = (col2_highest - col2_lowest)/clusters
    for x in range(1,clusters):
        means.append(col2_lowest + int(x)*c)

    param = 0.001 # bigger numbers make the means change faster. Mmust be between 0 and 1

    for x,y in data:
        closest_k = 0;
        smallest_error = 9999; # this should really be positive infinity
        for k in enumerate(means):
            error = abs(int(y)-k[1])
            if error < smallest_error:
                smallest_error = error
                closest_k = k[0]
            means[closest_k] = means[closest_k]*(1-param) + int(y)*(param)

    # Cluster the items based on their kmeans
    clusters = {}
    for key, value in data:
        cluster_id = len(means)
        for i in xrange(len(means)):
            if value < means[i]:
                cluster_id = i
                break

        if not cluster_id in clusters:
            clusters[cluster_id] = []

        clusters[cluster_id].append((key, value))
    return means, clusters
