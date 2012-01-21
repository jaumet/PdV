"""This file gets the votation list (key.tsv) and then adds the votation results' '\n'
 'to the active(yes,no,abs|true,false,block) column in map.tsv for each "true" keypadid.' '\n'
 'Finally it log map.tsv in data-temp/log/ and rewrites data-temp/map.tsv"""

import pprint
import time
import shutil

#### Getting the data

data1 = open("data-tmp/key.tsv")
votes = [i.strip().split() for i in data1.readlines()]

print ' -> number of votes: '+str(len(votes))

# add key.tsv to allkey.tsv. BUT change the first element of each newline (!)
f = open("data-tmp/allkey.tsv", 'a') # 'a' open existing file to append new line
timename = int(time.time())
for entry in votes:
    if entry[0] != "Topic":
        entry[0] = timename
    f.write("%s\n" % "\t".join([str(x) for x in entry]))
f.close()
print ' -> Appended votes from key.tsv to data-tmp/allkey.tsv'

data2 = open("data/map.tsv")
map = [i.strip().split() for i in data2.readlines()]

#pprint.pprint (votes)
#exit()

####################################
def main():
    #print list2tsv(votes2map(map, get_votations(votes)))
    #pprint.pprint(votes2map(map, get_votations(votes)))
    log_rewrite_map(votes2map(map, get_votations(votes)))

####################
def get_votations(votes):
    votes_list = dict()
    for vote in votes:
        if is_number(vote[4]):
            votes_list[vote[3]] = vote[4]
    pprint.pprint(votes_list)
    return votes_list

def votes2map(map, votes_list):
    new_map = []
    maphead = ""
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
                    #this are the voters who have not vote but could do it
                    line[9] = "absXX"
            new_map.append(line)
        else:
            maphead = line
    new_map.insert(0, maphead)
    return new_map

def list2tsv(list):
    mytsv = ""
    for line in list:
        for l in line:
            mytsv += "%s\t" % l
        mytsv += "\n"
    mytsv = mytsv.strip()
    return mytsv

def log_rewrite_map(map_new1):
    # Log the old map in data-tmp/log/
    # Check if the file exist
    fn = "data/map.tsv"
    shutil.copyfile(fn, "data-tmp/log/map-%s.tsv" % int(time.time()))
    print ' -> map.tsv log in data-tmp/log/'
    # Write the new map to this tsv file
    f = open(fn, "w")
    for entry in map_new1:
        f.write("%s\n" % "\t".join([str(x) for x in entry]))
        pprint.pprint("%s\n" % "\t".join([str(x) for x in entry]))
    f.close()
    print ' -> a new map.tsv writen'
    print

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

###################
main()
