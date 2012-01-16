import sys
import pprint
import random

'''This file choose 1 or 2 random values from active=true in map.tsv and set those
 to active=block and reqrites map.tsv'''

# Getting arguments first argument
try:
    method = sys.argv[1]
    print method
except:
    print "python president.py [method]"
    print "Method can be:"
    print "* an integer: 1, 2"
    print "* or 'manual'"

#exit()

#### Getting the data
map0 = open("data/map.tsv")
map = [i.strip().split() for i in map0.readlines()]


#pprint.pprint (map)
#exit()

print " ------------ comenca"

####################################
def main():
    print "fi"
    print chooser(method,getvoters(map))


####################
def getvoters(map):
    voters = []
    for voter in map:
        if voter[6] == "true":
            voters.append(voter[1])
    print " Possibles per elegir:"
    print voters
    return voters

def chooser(method, voters):
    choose = []
    if is_number(method):
        print "random ecollit: "
        choose.append(random.choice(voters))
        voters.remove(choose[0])
        choose.append(random.choice(voters))
    elif method == "manual":
        print "random"+method
    return choose

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

###################
main()