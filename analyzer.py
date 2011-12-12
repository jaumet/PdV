#!/usr/bin/env python
# encoding: utf-8
"""
jaume notes:         first_argument = sys.argv[1]
"""
import sys
import os
import pprint
import kmeans
import gridgrouper

class Analyzer(object):
    def __init__(self, fn):
        f = open(fn)
        self.data = [i.strip().split() for i in f.readlines()]

    def run(self):
        voters = self.build_voters()
        #pprint.pprint(voters)

        voters_sums = self.cross_reference(voters)
        #pprint.pprint(voters_sums)

        # kmeans with simplified data
        data = []
        for voter in voters_sums.keys():
            data.append([voter, voters_sums[voter][-1]])
        clusters = kmeans.kmeans(data, 5)
        pprint.pprint(clusters)

        # prepare for gridgrouper (only count size of groups)
        groups = []
        for cluster in clusters:
            groups.append(len(clusters[cluster]))
        print
        print groups

        grid, groups = gridgrouper.build_grid("10x10", groups)
        print
        grid.show()

        # Map the new seat positions to the cluster
        clusters_sorted = {}
        group = 0
        for cluster in clusters:
            clusters_sorted[cluster] = []
            for i in xrange(len(clusters[cluster])):
                keypad, oldsum = clusters[cluster][i]
                #clusters_sorted[cluster].append((keypad, oldsum, str(groups[group].seats[i])))
                xx = str(groups[group].seats[i])
                clusters_sorted[cluster].append((keypad, xx[5:-2].split(", ")))

            group += 1
        # Here I need to math x, y positions with seat-number
        print " clusters:"
        pprint.pprint(clusters_sorted)

    def build_voters(self):
        voters = {}
        voters_simple = {}
        votation_ids = []
        for l in self.data[1:]:
            if l[1] != "Sign":
                # Build the list of votation ids
                if l[0] not in votation_ids:
                    votation_ids.append(l[0])
                # Add vote of this voter. If not yet exists, create empty
                if l[3] not in voters:
                    voters[l[3]] = {}
                voters[l[3]][l[0]] = l[4]  # col 4 is the vote

        # Fill up absent votes and build list
        for v in voters.keys():
            for vid in votation_ids:
                if not vid in voters[v]:
                    voters[v][vid] = None
                if not v in voters_simple:
                    voters_simple[v] = []
                voters_simple[v].append(voters[v][vid])

        self.votation_ids = votation_ids
        return voters_simple

    def cross_reference(self, voters):
        votecounts = []
        for i in xrange(len(self.votation_ids)):
            # For each votation, sum up all votes we can find
            c = {}
            for voter in voters.keys():
                vote = voters[voter][i]
                if not vote in c:
                    c[vote] = 1
                else:
                    c[vote] += 1
            votecounts.append(c)

        pprint.pprint(votecounts)

        # Replace votes with sum of people with same vote
        voters_sums = {}
        for voter in voters.keys():
            voters_sums[voter] = []
            for i in xrange(len(voters[voter])):
                vote = voters[voter][i]
                voters_sums[voter].append(int(votecounts[i][vote]) - 1)
            voters_sums[voter].append(sum(voters_sums[voter]))

        return voters_sums

def main():
    analyzer = Analyzer("data-tmp/key.tsv")
    analyzer.run()

if __name__ == '__main__':
    main()
