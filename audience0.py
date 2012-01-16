import sys
import pprint

'''This file gets the votation list (key.tsv) and then adds "true"
 to the "active" column in map.tsv for each keypadid. When keypadid is not present, then adds "empty"
 Finally it rewrites map.tsv'''

#### Getting the data
data1 = open("data-tmp/key.tsv")
votes = [i.strip().split() for i in data1.readlines()]

map0 = open("data/map.tsv")
map = [i.strip().split() for i in map0.readlines()]

#pprint.pprint (map)
#exit()

####################################
def main():
    print list2tsv(votes2map(map, get_votations(votes)))

####################
def get_votations(votes):
    votes_list = dict()
    for vote in votes:
        if is_number(vote[4]):
            votes_list[vote[3]] = vote[4]
    return votes_list

def votes2map(map, votes_list):
    new_map = []
    for line in map:
        if is_number(line[0]):
            if line[1] in votes_list:
                line[6] = "true"
            else:
                line[6] = "empty"
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
