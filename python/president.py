"""This file choose 1 or 2 or n random values from active!=false in map.tsv and set those to active=block and rewrites map.tsv"""

import sys
import pprint
import random
import common

#Getting the path vars
c = common

# Getting arguments first argument
usage = """
    Usage:
        python president.py [number] [type] [gender]
        * number can be: an integer > 0: 1, 2, 3, 4,...
        * type can be: president OR tribunal OR army
        * gender: can be "wm" (choose un man and one women) or "-" (not discriminate by gender)
        """

#noinspection PyBroadException
try:
    number = sys.argv[1]
    type = sys.argv[2]
    gender = sys.argv[3]
except:
    print usage
    sys.exit(1)
else:
    print "number = "+number+" | typr = "+type+" | gender = "+gender


#### Getting the data
map0 = open(c.pdvdata+"map.tsv")
map = [i.strip().split() for i in map0.readlines()]

####################################
def main():
    update_map(type, map, chooser(number,getvoters(map), gender))
    print "Has beed chosen "+number+" users as \""+type+"\""

def getvoters(map):
    """
     Getting the voter that can be eligible (active not false voters)
     """
    eligible = []
    all = []
    men = []
    women = []
    for voter in map:
        if voter[9] != "false" and is_number(voter[0]) and voter[8] == "null":
            all.append(voter[1])
            if voter[10] == "m":
                men.append(voter[1])
            elif voter[10] == "w":
                women.append(voter[1])
    print " Possibles per elegir:"
    eligible.append(all)
    eligible.append(men)
    eligible.append(women)
    print eligible
    return eligible

def chooser(number, voters, gender):
    """
    Choose random users from available ones and check if is possible to choose them
    """
    chosen = []
    c = 0
    print voters[1]
    if is_number(int(number)):
        print "random chosen: "+number+", "+gender+", "+str(len(voters[1]))+", "+str(len(voters[2]))
        if len(voters[0]) >= int(number):
            if number == "2" and gender == "wm":
                chosen.append(random.choice(voters[1]))
                chosen.append(random.choice(voters[2]))
            else:
                for x in range(int(number)):
                    chosen.append(random.choice(voters[0]))
                    voters[0].remove(chosen[c])
                    c += 1
        elif len(voters[0]) < 1:
            print "No eligible voters available!"
        else:
            print "The number "+str(len(voters[0]))+" is too big"
            chosen = ["none"]
    elif number == "manual":
        print "random: "+number
    else:
        print "The number is not correct"
        chosen = ["none"]
    print chosen
    return chosen

def update_map(type, map, chosen):
    mytsv = ""

    for line in map:
        if line[8] == type:
            line[8] = "null"
            line[9] = "true"
        if line[1] in chosen and line[8] == "null":
            line[8] = type
            #line[9] = "block"
            #print line
        for l in line:
            mytsv += "%s\t" % l
        mytsv += "\n"
    mytsv = mytsv.strip()
    #pprint.pprint(mytsv)
    # Write the new map to this tsv file
    fn = c.pdvdata+"map.tsv"
    f = open(fn, "w")
    f.write(mytsv)
    #pprint.pprint("%s\n" % "\t".join([str(x) for x in entry]))
    f.close()
    print ' -> a new map.tsv writen'
    return

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

###################
main()
