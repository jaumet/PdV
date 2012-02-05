"""
Votation_results
redenir arguments per aquesta accio

(Vots="No" from ID=30) -> type=block
"""

import os
import random
import pprint
import sys

class CheckResults(object):
    def __init__(self, id, vote, number, action):
        """
        Class to access to the log map files snd count votes="No" or "Si"
        """
        # arguments
        self.id = id
        self.vote = vote
        self.action = action
        self.number = number

        # variables
        self.pathlog = "C:\\PdV\\data-tmp\\log\\"
        self.srcmap = "C:\\PdV\\data\\map.tsv"
        self.mytsv = ""

    def get_filename_from_ID(self):
        """
        get the map-log for the name starting by "map-[ID]-"
        """
        for filename in os.listdir(self.pathlog):
            name = "map-"+str(self.id)+"-"
            if name in filename:
                print  "--->"+filename
                self.mytsv = filename
        return self.mytsv

    def chooser(self, mapold, vote, number, type, action):
        """
        1) Getting the oldmap data. 2) choosing [number] random keypads (if needed). 3) writing action in current map.tsv
        """
        # 1)
        file = open(self.pathlog+mapold, "r")
        old = [i.strip().split() for i in file.readlines()]
        negatives = []
        for line in old:
            if line[9] == vote:
                negatives.append(line[1])
        print "list of negatives votes:"
        print negatives

        # 2)
        if number>0:
            chosen = []
            c = 0
            for x in range(int(number)):
                chosen.append(random.choice(negatives))
                negatives.remove(chosen[c])
                c += 1
            print "Chosen keypads:"
            print chosen
            print "numer:"
            print number

        # 3)
        f = open(self.srcmap)
        last = [i.strip().split() for i in f.readlines()]
        for line in last:
            if line[1] in negatives:
                if line[8] == "W-" or line[8] == "M-":
                    line[8] = line[8]+type
                else:
                    line[8] = type

        mytsv = ""
        for line1 in last:
            for l in line1:
                mytsv += "%s\t" % l
            mytsv += "\n"
        mytsv = mytsv.strip()
        f = open(self.srcmap, "w")
        f.write(mytsv)
        f.close()
        return mytsv

###########################################################

# language:
# CheckResults(3, "No", 2, "block")
# meants: take from the votation ID=3, the votes = "No". Choose 2 of tem, and put type=block in each

# Getting arguments:
usage = """
	Usage:
		python check_old_results.py [screenID] [vote=yes/no/abs/block/false] [random number|0] [action=block]
		This does: take the map-205.tsv, get the keypads who have action = [vote]. form them takes X random ones. FInally
		writes [action] in the current map
		"""


#noinspection PyBroadException
try:
    id = sys.argv[1]
    vote = sys.argv[2]
    number = sys.argv[3]
    type = sys.argv[4]
    action = sys.argv[5]
except:
    print usage
    sys.exit(1)
else:
    print "id= "+id+" | vote= "+vote

check = CheckResults(id, vote, number, action)
newmap = check.chooser(check.get_filename_from_ID(), vote, number, type, action)
#print newmap
print "We got the votation id="+str(id)
print "We selected the votes="+vote
if number>0:
    print "Then we took "+str(number)+" random."
print "Then edited the current map, with action="+action+" for selected voters and type="+type


