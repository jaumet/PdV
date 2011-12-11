##from __future__ import division
##from random import random
import sys

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

    '''
    print "Data:"
    print data
    print "Means: "
    print means
    '''

    ###################################
    ## Cluster num -> elements
    clusters = {}
    count = 0
    for x,d in data:
        count = count + 1
        if int(d) < means[0]:
            i = 0
        elif int(d)<means[1]:
            i = 1
        elif int(d)<means[2]:
            i = 2
        elif int(d)<means[3]:
            i = 3
        else:
            i = 4

        count = 0
        if not clusters.has_key(i): clusters[i] = []
        clusters[i].append((x,d))
    return clusters

def main():
    '''print "Cluster:"'''
    data = [i.strip().split() for i in open("votescoincidence.tsv").readlines()]
    clusters = kmeans(data, 5)
    for k,v in clusters.items(): print k,v

if __name__ == '__main__':
    main()


'''
print clusters
print "len: "
for i in clusters:
	print len(clusters[i])
'''
