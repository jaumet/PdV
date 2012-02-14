"""This file gets the votation list (key.tsv) and then adds "true"
to the "active" column in map.tsv for each keypadid. When keypadid is not present, then adds "false"
Finally it rewrites map.tsv"""

import shutil
import pprint

#### Getting the data
data1 = open("C:\\PdV\\data-tmp\\key.tsv")
votes = [i.strip().split() for i in data1.readlines()]

map0 = open("C:\\PdV\\data\\map.tsv")
map = [i.strip().split() for i in map0.readlines()]

#pprint.pprint (map)
#exit()

def main():
    """
    main function
    """
    log_rewrite_map(list2tsv(votes2map(map, get_votations(votes))))
    #print list2tsv(votes2map(map, get_votations(votes)))

def get_votations(votes):
    """
    Get votations
    """
    votes_list = dict()
    for vote in votes:
        if is_number(vote[4]):
            votes_list[vote[3]] = vote[4]
    print "votes list:"+str(len(votes_list))
    #print votes_list
    return votes_list

def votes2map(map, votes_list):
    """
    votes 2 map
    """
    new_map = []
    for line in map:
        if is_number(line[0]):
            if line[1] in votes_list:
                line[9] = "true"
            else:
                line[9] = "false"
            new_map.append(line)
    #print " map0:"
    #pprint.pprint(new_map)
    return new_map

def list2tsv(list):
    """
    list to string (in tsv format)
    """
    mytsv = "seatid	keypadid	Xcolumn	Yrow	Xpx	Ypx	section	group	type	active	gender\n"
    for line in list:
        for l in line:
            mytsv += "%s\t" % l
        mytsv += "\n"
    mytsv = mytsv.strip()
    return mytsv

def log_rewrite_map(map_new1):
    """
    Log the old map in data-tmp/log/
    Check if the file exist
    """
    fn = "C:\\PdV\\data\\map.tsv"
    shutil.copyfile(fn, "C:\\PdV\\data-tmp\\log\\map0.tsv")
    print ' -> First map log in data-tmp\log\map0.tsv'
    # Write the new map to this tsv file
    f = open(fn, "w")
    f.write(map_new1)
    f.close()
    #print map_new1
    print " -> a new map.tsv writen in data/map.tsv"
    return

def is_number(s):
    """
    Check if s is number
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

###################
main()
