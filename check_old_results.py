"""
Votation_results
redenir arguments per aquesta accio

(Vots="No" from ID=30) -> type=block
"""

import os

class CheckResults(object):
    def __init__(self, id, vote):
        """
        Class to access to the log map files snd count votes="No" or "Si"
        """
        self.id = id
        self.vote = vote
        self.path = "C:\\PdV\\data-tmp\\log\\"
        self.mytsv = ""

    def get_votes(self):
        """
        get the map-log for the name starting by "map-[ID]-"
        """
        for filename in os.listdir(self.path):
            name = "map-"+str(self.id)+"-"
            #print filename
            #print "---"+name
            if name in filename:
                print  "--->"+filename
                self.mytsv = filename
        return self.mytsv
        #fopen(path)

#################################

check = CheckResults(3, "No")
print check.get_votes()


