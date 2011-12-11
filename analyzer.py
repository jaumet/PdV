#!/usr/bin/env python
# encoding: utf-8
"""

"""
import sys
import os
import pprint

class Analyzer(object):
    def __init__(self, fn):
        f = open(fn)
        self.data = [i.strip().split() for i in f.readlines()]

    def run(self):
        voters = self.build_voters()
        pprint.pprint(voters)

    def build_voters(self):
        voters = {}
        voters_simple = {}
        voting_ids = []
        for l in self.data[1:]:
            if l[1] != "Sign":
                # Build the list of votation ids
                if l[0] not in voting_ids:
                    voting_ids.append(l[0])
                # Add vote of this voter. If not yet exists, create empty
                if l[3] not in voters:
                    voters[l[3]] = {}
                voters[l[3]][l[0]] = l[4]

        # Fill up absent votes and build list too
        for v in voters.keys():
            for vid in voting_ids:
                if not vid in voters[v]:
                    voters[v][vid] = None
                if not v in voters_simple:
                    voters_simple[v] = []
                voters_simple[v].append(voters[v][vid])

        return voters_simple

def main():
    analyzer = Analyzer("data-tmp/key.tsv")
    analyzer.run()

if __name__ == '__main__':
    main()
