import common
c= common

def main():
    change_map()

def change_map():
    data = c.pdvdata+"map.tsv"
    file = open(data, "r")
    map = [i.strip().split() for i in file.readlines()]
    cnt = 0
    for line in map:
        if line[9]=="no":
            line[9] = "block"
            cnt += 1
    mytsv = ""
    for line1 in map:
        for l in line1:
            mytsv += "%s\t" % l
        mytsv += "\n"

    mytsv = mytsv.strip()
    f = open(data, "w")
    f.write(mytsv)
    f.close()
    print
    print "All keypads who voted 'no' blocked in current map.tsv"
    print "Total blocked = "+str(cnt)
    print "Done!"
    print
    return mytsv

######################################
main()
