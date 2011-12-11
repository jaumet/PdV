import sys
from itertools import tee

#### Getting the data
data1 = open("data-tmp/key.tsv")
out1 = [i.strip().split() for i in data1.readlines()]
data2 = open("data-tmp/feedback.tsv")
out2 =[i.strip().split('\t') for i in data2.readlines()]

list_votations = []
for i in out1:
      if not i[0] in list_votations:
          list_votations.append(i[0])
del list_votations[0]
last_votation = list_votations[-1]

####################################
def main():
    list2 = computeList(out2)
    print get_votations(out1, list2, list_votations)

####################
def get_votations(out1, list2, list_votations):
    myxml = '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
  #myxml = '\t<items>\n'
    c = 0
    for i in list2:
        myxml += "<votations>\n"
        myxml += "\t<votation>\n\t\t<title>"+list2[c][1][1]+"</title>\n"
        myoptions = ''
        for f in i:
            d = 0
            if is_number(f[0]) and len(f)>3	:
                myoptions += "\t\t\t<option>\n"
                myoptions += "\t\t\t\t<label>"+f[1].strip()+"</label>\n"
                myoptions += "\t\t\t\t<numvotes>"+f[2]+"</numvotes>\n"
                myoptions += "\t\t\t\t<percent>"+f[3][:-1]+"</percent>\n"
                myoptions += "\t\t\t</option>\n"

            if f[0] == "Participants" :
                myxml += "\t\t\t<participants>"+f[2]+"</participants>\n"
            if f[0] == "Submitted":
                myxml += "\t\t\t\t<submitted>"+f[2]+"</submitted>\n"

            for l in out1:
                if i[0] == "Submitted	":
                    myxml += "\t\t\t\t<submitted>"+f[2]+"</submitted>\n"

        myxml += "\t\t<options>\n"+myoptions+"\n\t\t</options>\n"
        myxml += "\t\t<votes>\n"

        for v in out1:
            if v[0] == list_votations[c]:
                if v[0][:4] == "Sign":
                    x = 4
                else:
                    x = 3
                myxml += "\t\t\t<vote>\n"
                myxml += "\t\t\t\t<keypadid>"+v[x]+"</keypadid>\n"
                myxml += "\t\t\t\t<answer>"+v[x+1]+"</answer>\n"
                myxml += "\t\t\t\t<speed>"+v[x+2]+"</speed>\n"
                myxml += "\t\t\t</vote>\n"

        myxml += "\t\t</votes>\n"
        myxml += "\t</votation>\n"
        myxml += "</votations>\n"
        c = c +1
    return myxml

def computeList(l): 
        SEPARATOR = ['']
        result = []
        tmp = []
        for item in l:
                if item == SEPARATOR:
                        result.append(tmp)
                        tmp = []
                else:
                        tmp.append(item)
        result.append(tmp)
        return result

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

###################
main()
