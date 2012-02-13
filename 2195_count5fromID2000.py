
def main():
    change_map(get_winner())

def get_winner():
    #### Getting the data
    data1 = open("C:\\PdV\\data-tmp\\count5.tsv")
    votes = [i.strip().split() for i in data1.readlines()]

    winneroption = []
    points = 0
    result = ""
    voters = []
    for vote in votes:
        if vote[0] != "--":
            print vote
            if vote[0] not in voters:
                voters.append(vote[0])
            if vote[1] == "yes":
                points += 1
            if vote[1] == "no":
                points += -1
        else:
            if points <= 0:
                results = "no"
            else:
                results = "yes"
            winneroption.append(results)
            points = 0
            print "winner option: "+str(results)
            print voters
            print "-----"

    v = 0
    winners = []
    for vote in votes:
        if vote[0] != "--":
            if vote[1] == winneroption[v]:
               winners.append(vote[0])
            v += 1
        else:
            v = 0

    counts = dict()
    for n in winners:
        if n not in counts:
            counts[n] = 0
        counts[n] += 1
    mywinner =  sorted(counts.items())

    print "Score:"
    print mywinner
    print "max"
    key,ignored = max(counts.iteritems(), key=lambda x:x[1])
    print key
    return key

def change_map(voter):
    data = "C:\\PdV\\data\\map.tsv"
    file = open(data, "r")
    map = [i.strip().split() for i in file.readlines()]
    for line in map:
        if line[1] == voter:
            line[9] = "true"
        else:
            if line[9] != "false":
                line[9] = "block"
    mytsv = ""
    for line1 in map:
        for l in line1:
            mytsv += "%s\t" % l
        mytsv += "\n"

    mytsv = mytsv.strip()
    f = open(data, "w")
    f.write(mytsv)
    #print "map with one voter:"
    #print mytsv
    f.close()
    return mytsv

######################################
main()
