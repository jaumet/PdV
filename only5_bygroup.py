"""
1) Get the vots of the last map
2) make lists of voters per group.
3) Chose one per group
4) Block all voters except the chosen ones
"""

import os
from random import choice
import pprint
import sys

class CheckResults(object):
    def __init__(self):
        """
        Class to access to the log map files and count votes="no" or "yes"
        """
        # variables
        self.pathlog = "C:\\PdV\\data-tmp\\log\\"
        self.srcmap = "C:\\PdV\\data\\map.tsv"
        self.mytsv = ""
        self.mytsv = self.srcmap

    def chooser(self):
        """
        1) Get the votes of the last map
        2) make lists of voters per group.
        3) Choose one per group
        4) Block all voters except the chosen ones
        """
        # 1)
        file = open(self.mytsv, "r")
        old = [i.strip().split() for i in file.readlines()]
        # 2)
        groups = [0,0,0,0,0,0]
        groups[0] = []
        groups[1] = []
        groups[2] = []
        groups[3] = []
        groups[4] = []
        groups[5] = []
        for line in old:
            #print line
            # We chose from voter that are there, that are not false and has type = null
            if line[7] != "0" and line[9] != "false" and line[8] == "null":
                if line[7] == "0":
                    groups[0].append(line[1])
                if line[7] == "1":
                    groups[1].append(line[1])
                elif line[7] == "2":
                    groups[2].append(line[1])
                elif line[7] == "3":
                    groups[3].append(line[1])
                elif line[7] == "4":
                    groups[4].append(line[1])
                elif line[7] == "5":
                    print "555555555555555"
                    groups[5].append(line[1])


        # 3) Chose one per group
        chosen = []
        #del groups[5]
        for g in groups:
            pprint.pprint(g)
            print
        for i in xrange(0,6):
            print i
            if len(groups[i])>0:
                print "-- "+str(i)
                chosen.append(choice(groups[i]))
        print "-> 5 chosen keypads:"
        pprint.pprint(chosen)

        # 4) Block all voters except the chosen ones
        mytsv = ""
        for voter in old:
            if voter[8] == "null":
                if voter[1] in chosen:
                    voter[9] = "true"
                else:
                    voter[9] = "block"

            for v in voter:
                mytsv += "%s\t" % v
            mytsv += "\n"
        mytsv = mytsv.strip()
        f = open(self.srcmap, "w")
        #print mytsv
        print "escriu a "+self.srcmap
        f.write(mytsv)
        f.close()
        return mytsv

###########################################################

# language:
# CheckResults(3, "No", 2, "block")
# meants: take from the votation ID=3, the votes = "No". Choose 2 of tem, and put type=block in each

# Getting arguments:


check = CheckResults()
newmap = check.chooser()
#print newmap



