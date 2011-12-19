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

        # Read map.tsv and build internal representation
        f = open("data/map.tsv")
        self.map_dict = {}
        for i in f.readlines():
            seat_id, keypad_id, x, y, x_px, y_px, hid, _ = i.strip().split()
            if keypad_id == "keypadid":
                continue
            seat_id = int(seat_id)
            x = int(x)
            y = int(y)
            self.map_dict[(x, y)] = [seat_id, keypad_id, x, y, x_px, y_px, hid]

        pprint.pprint(self.map_dict)

    def run(self):
        voters = self.build_voters()
        #pprint.pprint(voters)

        voters_sums = self.cross_reference(voters)
        #pprint.pprint(voters_sums)

        # calculate kmeans with simplified data
        data = []
        for voter in voters_sums.keys():
            data.append([voter, voters_sums[voter][-1]])
        clusters = kmeans.kmeans(data, 5)
        #print
        #print "Group id:(keypad zid, score):"
        #pprint.pprint(clusters)

        # prepare for gridgrouper (only count size of groups)
        groups = []
        for cluster in clusters:
            groups.append(len(clusters[cluster]))
        print
        print "Number of people in each cluster: "
        print groups

        grid, groups = gridgrouper.build_grid("31x6", groups)
        print
        grid.show()

        # Map the new seat positions to the clusters
        seats_info = {}
        group = 0
        for cluster in clusters:
            for i in xrange(len(clusters[cluster])):
                keypad, oldsum = clusters[cluster][i]
                seat = groups[group].seats[i]
                seats_info[keypad] = [seat.x, seat.y, group]
            group += 1
        #print " clusters:"
        #pprint.pprint(seats_info)

        # Build new map: replace keypad_id and group in original map based
        # on the x/y coordinates.
        map_new = []
        for keypad_id in seats_info:
            # Extract new pos info from the clusters
            x_new, y_new, group_new = seats_info[keypad_id]

            # Extract info from original map
            seat_id, keypad_id_old, x, y, x_px, y_px, human = \
                    self.map_dict[(x_new, y_new)]

            # Combine info into map_new
            map_new.append([seat_id, keypad_id, x, y, x_px, y_px, \
                    human, group_new])

        map_new.sort()

        print "Map (seat-id, new-keypad-id, x, y, x_px, y_px, human, group)"
        pprint.pprint(map_new)

    def build_voters(self):
        """
        Build a dictionary of voters
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
        """

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
