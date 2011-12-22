#!/usr/bin/env python
# encoding: utf-8
"""
Analyze votes from a tsv file, perform some functions, cluster the voters in
groups, possible reorder the groups, etc.

Fast prototype ;)

Authors:
    Chris Hager
    Jaume Nualart
"""

__version__ = "0.1"

import sys
import os
import pprint
from optparse import OptionParser

import kmeans
import gridgrouper

# Modes map to the column of the votes-tsv file to use
MODE_VOTE_RESULT = 4
MODE_VOTE_SPEED = 5


class Analyzer(object):
    """
    This class is able to read a tsv file with the votes, and perform various
    related functions.
    """
    def __init__(self, fn, abstention_id):
        # 'None' to count as abstention, any string to add to another vote
        self.abstention_id = abstention_id

        # Read the votes tsv file
        f = open(fn)
        self.data = [i.strip().split() for i in f.readlines()]

        # Read map.tsv and build internal representations
        f = open("data/map.tsv")
        self.map_xy = {}
        self.map_keypad = {}
        for i in f.readlines():
            seat_id, keypad_id, x, y, x_px, y_px, hid, _ = i.strip().split()
            if keypad_id == "keypadid":
                continue
            seat_id = int(seat_id)
            x = int(x)
            y = int(y)
            self.map_xy[(x, y)] = [seat_id, keypad_id, x, y, x_px, y_px, hid]
            self.map_keypad[keypad_id] = [seat_id, keypad_id, x, y, x_px, y_px, hid]

        #pprint.pprint(self.map_dict)

    def kmeans(self, sums, num_clusters=3):
        # calculate kmeans with simplified data
        data = []
        for voter in sums.keys():
            data.append([voter, sums[voter][-1]])
        return kmeans.kmeans(data, num_clusters)

    def grid_reorder(self, clusters, gridsize="31x6"):
        # prepare for gridgrouper (only count size of groups)
        groups = []
        for cluster in clusters:
            groups.append(len(clusters[cluster]))

        grid, groups = gridgrouper.build_grid(gridsize, groups)

        # Map the new seat positions to the clusters
        seats_info = {}
        group = 0
        for cluster in clusters:
            for i in xrange(len(clusters[cluster])):
                keypad, oldsum = clusters[cluster][i]
                seat = groups[group].seats[i]
                seats_info[keypad] = [seat.x, seat.y, group]
            group += 1

        return grid, groups, seats_info

    def remap_after_reorder(self, seats_info):
        """
        Map the regrouped voters back to the original map.tsv (theater seats mapping)
        """
        # Build new map: replace keypad_id and group in original map based
        # on the x/y coordinates.
        map_new = []
        for keypad_id in seats_info:
            # Extract new pos info from the clusters
            x_new, y_new, group_new = seats_info[keypad_id]

            # Extract info from original map
            seat_id, keypad_id_old, x, y, x_px, y_px, human =\
            self.map_xy[(x_new, y_new)]

            # Combine info into map_new
            map_new.append([seat_id, keypad_id, x, y, x_px, y_px,\
                            human, group_new])

        return map_new

    def read_votes_tsv(self, mode=MODE_VOTE_RESULT):
        """
        Reades the raw votes tsv file and builds the internal data structure.

        voters is a dictionary of keypad-id mapping to a dictionary of
        voting-round-id and this keypads respective votes:

            {'1': {'Judge20111210053447': '1',
               'Judge20111210053457': '2',
               'Judge20111210053509': '1',
               'Judge20111210053516': '2',
               'Judge20111210053524': '1',
               'Judge20111210053531': '2'},
              ...

        voters_simple is a dictionary of keypad-id mapping to a list of only the results of this
        keypads votations:

            {'1': ['1', '2', '1', '2', '1', '2'],
             '10': ['2', '1', '2', '2', '1', '2'],
             ...
        """
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

                # Save the respective column of the tsv file into our data structure
                value = l[mode]

                # If analizing by voting speed, we convert to float
                if mode == MODE_VOTE_SPEED:
                    value = float(value) if value else 0

                # Store the value we want to analyze
                voters[l[3]][l[0]] = value

        # Fill up absent votes and build list
        for v in voters.keys():
            for vid in votation_ids:
                if not vid in voters[v]:
                    voters[v][vid] = self.abstention_id if mode == MODE_VOTE_RESULT else 0
                if not v in voters_simple:
                    voters_simple[v] = []
                voters_simple[v].append(voters[v][vid])

        self.votation_ids = votation_ids
        return voters, voters_simple

    def voting_correlatation_sums(self, voters):
        """
        Build the sums of how many other people voted the same.
        """
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

        print "Summary: vote count per votation"
        pprint.pprint(votecounts)
        print

        # Replace votes with sum of people with same vote
        voters_sums = {}
        for voter in voters.keys():
            voters_sums[voter] = []
            for i in xrange(len(voters[voter])):
                vote = voters[voter][i]
                voters_sums[voter].append(int(votecounts[i][vote]) - 1)
            voters_sums[voter].append(sum(voters_sums[voter]))

        return voters_sums


def analyze(mode, reorder, num_groups, abstention_id=None):
    """
    Analyzes the votes, groups them with k-means and optionally reorders the seats.
    """
    # Load data from tsv
    analyzer = Analyzer("data-tmp/key.tsv", abstention_id)
    voters, voters_simple = analyzer.read_votes_tsv(mode)

    # Prepare data for k-means clustering
    if mode == MODE_VOTE_RESULT:
        data = analyzer.voting_correlatation_sums(voters_simple)

    elif mode == MODE_VOTE_SPEED:
        # build the averages of the voting speed in each round, per participant
        data = {}
        for voter in voters_simple:
            data[voter] = [sum(voters_simple[voter])/len(voters_simple[voter])]

    # Build clusters by kmeans
    means, clusters = analyzer.kmeans(data, num_clusters=num_groups)

    # Lots of output of the means
    print "means:"
    pprint.pprint(means)

    print
    print "Number of people in each cluster: "
    print [len(clusters[key]) for key in clusters]
    print

    for group_id in clusters:
        if group_id >= len(means):
            s = "> %s" % means[group_id-1]
        else:
            s = "< %s" % means[group_id]
        print "  %s people %s" % (len(clusters[group_id]), s)

    # Update the original map with the calculated group, and if reordering with
    # the new keypad-id.
    map_new = None
    if reorder:
        # Regroup and remap
        grid, groups, seats_info = analyzer.grid_reorder(clusters)
        print; grid.show()

        map_new = analyzer.remap_after_reorder(seats_info)

    else:
        # Just update the original map with the calculated group for each keypad.
        map_new = []
        for group_id in clusters:
            for keypad_id, _ in clusters[group_id]:
                # Extract info from original map
                seat_id, keypad_id_old, x, y, x_px, y_px, human =\
                        analyzer.map_keypad[keypad_id]

                # Combine info into map_new
                map_new.append([seat_id, keypad_id, x, y, x_px, y_px,\
                                human, group_id])

    print
    print "Updated Map " + \
          "(seat-id, new-keypad-id, x, y, x_px, y_px, human, group)"
    map_new.sort()
    pprint.pprint(map_new)
    return map_new

if __name__ == '__main__':
    usage = """usage: %prog [-m mode] [options]"""
    version = "%prog " + __version__
    parser = OptionParser(usage=usage, version=version)
    parser.add_option("-m", "--mode", nargs=1, choices=["results", "speed"],
        dest="mode", help="Either 'results' or 'speed'")
    parser.add_option("-n", "--num-groups", default=3, type="int",
        dest="num_groups", help="How many groups to build (default=3)")
    parser.add_option("-r", "--reorder", default=False,
        action="store_true", dest="reorder", help="Use this flag to reorder")
    parser.add_option("-o", "--out-fn", nargs=1,
        dest="out_fn", help="Output filename for new map.tsv (optional)")
    parser.add_option("-c", "--count_abstention_as", nargs=1, default=None,
        dest="vote_id", help="Count abstention to a specific vote")

    (options, args) = parser.parse_args()
    print options
    print
    #exit(0)

    if not options.mode:
        parser.error("Please specify a mode")

    elif options.mode == "results":
        map_new = analyze(mode=MODE_VOTE_RESULT, reorder=options.reorder,
                num_groups=options.num_groups, abstention_id=options.vote_id)

    elif options.mode == "speed":
        map_new = analyze(mode=MODE_VOTE_SPEED, reorder=options.reorder,
                num_groups=options.num_groups, abstention_id=options.vote_id)

    if options.out_fn:
        # Write the new map to this tsv file
        f = open(options.out_fn, "w")
        for entry in map_new:
            f.write("%s\n" % "\t".join([str(x) for x in entry]))
        f.close()
