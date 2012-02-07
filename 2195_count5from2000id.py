import pprint

#### Getting the data
data1 = open("C:\\PdV\\data-tmp\\count5.tsv")
votes = [i.strip().split() for i in data1.readlines()]

counter = dict()
countertmp = dict()
pprint.pprint(votes)
for vote in votes:
    if "--" not in vote[0]:
        counter[vote[0]] = 0
        countertmp[vote[0]] = 0
for vote in votes:
    print vote
    if vote[1] == "yes":
        countertmp[vote[0]] += 1
    if vote[1] == "no":
        countertmp[vote[0]] += -1
    if vote[0] == "--":
        counter = countertmp
        countertmp[vote[0]] = 0

    print counter

print counter
