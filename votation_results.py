import sys
import pprint

'''This file gets the votation list (key.tsv) and then adds the votation results
 to the active(yes,no,abs|true,false,block) column in map.tsv for each "true" keypadid.
 Finally it rewrites map.tsv'''

#### Getting the data
data1 = open("data-tmp/key.tsv")
votes = [i.strip().split() for i in data1.readlines()]

data2 = open("data/map.tsv")
map = [i.strip().split() for i in data2.readlines()]

#pprint.pprint (votes)
#exit()

####################################
def main():
    #print list2tsv(votes2map(map, get_votations(votes)))
    pprint.pprint(votes2map(map, get_votations(votes)))

####################
def get_votations(votes):
    votes_list = dict()
    for vote in votes:
        if is_number(vote[4]):
            votes_list[vote[3]] = vote[4]
    #pprint.pprint(votes_list)
    return votes_list

def votes2map(map, votes_list):
    new_map = []
    for line in map:
        if is_number(line[0]):
            if line[9] != "false" and line[9] != "block":
                if line[1] in votes_list:
                    if votes_list[line[1]] == "1":
                        line[9] = "yes"
                    elif votes_list[line[1]] == "2":
                        line[9] = "no"
                    elif votes_list[line[1]] == "3":
                        line[9] = "abs"
                elif line[9] != "0":
                    '''this are the voters who have not vote but could do it'''
                    line[9] = "absXX"
            new_map.append(line)
    return new_map

def list2tsv(list):
    mytsv = ""
    for line in list:
        for l in line:
            mytsv += "%s\t" % l
        mytsv += "\n"
    mytsv = mytsv.strip()
    return mytsv

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

###################
main()
