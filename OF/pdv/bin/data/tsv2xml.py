import sys
from itertools import tee

#### Getting the data
data1 = open("key.tsv")
out1 = [i.strip().split() for i in data1.readlines()]
data2 = open("feedback.tsv")
out2 =[i.strip().split('\t') for i in data2.readlines()]

####################################
def main():
    print total_results_xml(list2, out1)
 
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

def get_last_votes(out1, f):
    last_tsv = ""
    last_xml = '\t<items>\n'
    for i in out1:
        if i[0] == last_votation:
                last_tsv += i[3]+"\t"+i[4]+"\n"
                last_xml += "\t\t<item>\n\t\t\t<id>"+i[3]+"</id>\n\t\t\t<vote>"+i[4]+"</vote>\n\t\t</item>\n"
    last_xml += '\t</items>\n'
    if f == 'tsv':
        return last_tsv
    if f == 'xml':
        return last_xml

def last_votation_results(list2, f):
    if f == '':
        last_result = list2[-1]
    if f == 'xml':
        last_result = '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
        last_result += "<votacio>\n\t<title>"+list2[0][1][1]+"</title>\n"
        for i in list2:
            c = 0
            for f in i:
                if is_number(f[0]) and c>0:
                    last_result += "\t<options>\n"
                    ##print f[0]
                    last_result += "\t\t<option>"+f[1].strip()+"</option>\n"
                    last_result += "\t\t<votes>"+f[2]+"</votes>\n"
                    last_result += "\t\t<percent>"+f[3]+"</percent>\n"
                    last_result += "\t</options>\n"
                c = c +1
    return last_result

def total_results_xml(list2, out1):
    chunk1 = last_votation_results(list2, 'xml')
    chunk2 = get_last_votes(out1, 'xml')
    output = chunk1 + chunk2 + '</votacio>'
    return output

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