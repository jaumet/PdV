import sys
from itertools import tee

#### Getting the data
data1 = open("key.tsv")
out1 = [i.strip().split() for i in data1.readlines()]
data2 = open("feedback.tsv")
out2 =[i.strip().split('\t') for i in data2.readlines()]

####################################
def main():
    print "------------------------------------------------------"
    print "Aquest es un exemple per a 30 votants."
    print
    print "(1) Number of votations"
    print "(2) Last Votation (xml)"
    print "(3) Last Votation (tsv)"
    print "(4) Results last votation (array)"
    print "(5) Results last votation (xml)"

    name = raw_input("Choose an option:")

    if name == "1":
        print "Number of votations (feedback): "
        print len(list2)
        print "Number of votations (keys): "
        print len(list_votations)
        print "Votations list:"
        print list_votations
    elif name == "2":
        mytitle = last_votation_results(list2)
        print "Votation Title: \""+mytitle[1][1]+"\""
        print "----------------------------------- last_xml"
        print get_last_votes('xml')
    elif name == "3":
        print "Votation Title: \""+mytitle[1][1]+"\""
        print "----------------------------------- last_tsv"
        print get_last_votes('tsv')
    elif name == "4":
        print "Results last votation (array)"
        print last_votation_results(list2)
    elif name == "5":
        print "Results last votation (xml)"
        print last_votation_results(list2, 'xml')
    else:
        print "Sorry..."
        print "his is not a right option"
 
####################

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

list2 = computeList(out2)

def get_last_votes(f='xml'):
    last_tsv = ""
    last_xml = '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
    for i in out1:
        if i[0] == last_votation:
                last_tsv += i[3]+"\t"+i[4]+"\n"
                last_xml += "<item>\n\t<id>"+i[3]+"</id>\n\t<vote>"+i[4]+"</vote>\n</item>\n"
    if f == 'tsv':
        return last_tsv
    if f == 'xml':
        return last_xml

def last_votation_results(list2, f):
    if f == '':
        last_result = list2[-1]
    if f == 'xml':
        last_result = '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
        last_result += "\t<votacio>\n\t\t<title>"+list2[0][1][1]+"</title>\n"
        print list2
        for i in list2:
            c = 0
            for f in i:
                if is_number(f[0]) and c>0:
                    last_result += "\t\t<options>\n"
                    ##print f[0]
                    last_result += "\t\t\t<option>"+f[1].strip()+"</option>\n"
                    last_result += "\t\t\t<votes>"+f[2]+"</votes>\n"
                    last_result += "\t\t\t<percent>"+f[3]+"</percent>\n"
                    last_result += "\t\t</options>\n"
                c = c +1
        last_result += "\t</votacio>"
    return last_result

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
###################

list_votations = []
for i in out1:
    if not i[0] in list_votations:
        list_votations.append(i[0])

del list_votations[0]
last_votation = list_votations[-1]

###################
main()