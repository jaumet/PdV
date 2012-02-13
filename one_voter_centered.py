
def main():
    change_map(15, 3)

def change_map(Xcolumn, Yrow):
    data = "C:\\PdV\\data\\map.tsv"
    file = open(data, "r")
    map = [i.strip().split() for i in file.readlines()]
    for line in map:
        if line[2] == str(Xcolumn) and line[3] == str(Yrow):
            line[9] = "true"
            print "###############"
            print line
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
    f.close()
    return mytsv

######################################
main()
