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
    def __init__(self, id, vote, number, action, type):
        """
        Class to access to the log map files snd count votes="No" or "Si"
        """
        # arguments
        self.id = id
        self.vote = vote
        self.action = action
        self.number = number
        self.type = type

        # variables
        self.pathlog = "C:\\PdV\\data-tmp\\log\\"
        self.srcmap = "C:\\PdV\\data\\map.tsv"
        self.mytsv = ""

    def get_filename_from_ID(self):
        """
        get the map-log for the name starting by "map-[ID]-"
        """
        if self.id == "-":
            self.mytsv = self.srcmap
        else:
            for filename in os.listdir(self.pathlog):
                name = "map-"+str(self.id)+"-"
                if name in filename:
                    print  "--->"+filename
                    self.mytsv = self.pathlog+filename
        print "My file is: "+self.mytsv
        return self.mytsv

    def chooser(self, mapold, vote, number, type, action):
        """
        1) Getting the oldmap data. 2) choosing [number] random keypads (if needed). 3) writing type & action in current map.tsv
        """
        # 1)
        file = open(mapold, "r")
        old = [i.strip().split() for i in file.readlines()]
        oldmap_votes = []
        for line in old:
            if line[9] == vote:
                oldmap_votes.append(line[1])
        print "list of oldmap_votes "+vote+":"
        print oldmap_votes

        # 2)
        chosen =[]
        if int(number) > 0:
            if len(oldmap_votes)>0:
                chosen = []
                oldmap_votes1 = oldmap_votes
                c = 0
                for x in range(int(number)):
                    chosen.append(random.choice(oldmap_votes1))
                    oldmap_votes1.remove(chosen[c])
                    c += 1
                print "Chosen keypads:"
                print chosen
                print "numer:"
                print number

            # 3)
        f = open(self.srcmap)
        last = [i.strip().split() for i in f.readlines()]
        if int(number)>0:
            old = chosen
        else:
            old = oldmap_votes
        for line in last:
            if line[1] in old:
                if len(type)>1:
                    line[8] = type
                if len(action)>1:
                    line[9] = action

        mytsv = ""
        for line1 in last:
            for l in line1:
                mytsv += "%s\t" % l
            mytsv = mytsv.strip()
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
	python check_old_results.py [screenID] [vote=yes/no/abs/block/false] [random number|0] [action=block] [type]
	This does: take the map-205.tsv, get the keypads who have action = [vote]. from them takes X random ones. FInally
	writes [action] & [type]in the current map
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

check = CheckResults(id, vote, number, type, action)
newmap = check.chooser(check.get_filename_from_ID(), vote, number, type, action)
#print newmap
print "We got the votation id="+str(id)
print "We selected the votes="+vote
if number>0:
    print "Then we took "+str(number)+" random."
print "Then edited the current map, with action="+action+" for selected voters and type="+type


