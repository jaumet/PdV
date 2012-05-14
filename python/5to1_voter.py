from random import choice
import common

c = common

data = c.pdvdata+"map.tsv"
file = open(data, "r")
map = [i.strip().split() for i in file.readlines()]
the_five = []
for line in map:
    if line[9] != "false" and line[9] != "block" and line[0] != "seatid":
        the_five.append(line[1])
        print line
the_one = choice(the_five)

print "chosen voter:"
print the_one

mytsv = ""
for line1 in map:
    if line1[1] in the_five and line1[1] != the_one:
        line1[9] = "block"
        print "block"
    for l in line1:
        mytsv += "%s\t" % l
    mytsv = mytsv.strip()
    mytsv += "\n"
mytsv = mytsv.strip()
f = open(data, "w")
f.write(mytsv)
f.close()



