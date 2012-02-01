import sys
import os
import pprint
import pyodbc
import shutil
import time

path = u'C:\\SunVote ARS 2010\\Resources\\DataBase\\'

#####################################
#### Getting the last file of a directpry
os.chdir(path)
files = filter(os.path.isfile, os.listdir(path))
files.sort(key=lambda x: os.path.getmtime(x))
fn1 = files[-1]
print path
fn1 = path+fn1
fn = fn1.replace("\\", "\\\\")
print "fn:"
print fn
#sys.exit()

#### Check whether the *.ars file is empty
if os.path.getsize(fn) > 0:
    pass
else:
    print "-----------> ARS file is empty!!"
    print os.path.getsize(fn)
    sys.exit()

#####################################
#### cp last file everytime we want to read the votes (coz t
#### he MS Access file looks like is blocked during votations
fn2 = u'C:\\PdV\\data-tmp\\00.ars'
shutil.copyfile(fn, fn2)
print "- Size of 00.ars:"
print os.path.getsize(fn)

#########################################
#### pyodbc: getting the votes
print fn2
MDB = fn2
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'

conn = pyodbc.connect('DRIVER=%s;DBQ=%s;' % (DRV,MDB))
curs = conn.cursor()

#SQL = 'SELECT R_KeypadID, R_Result, R_Speed FROM ARS_Response;' # insert your query here
SQL = 'SELECT * FROM ARS_Response;' # insert your query here
curs.execute(SQL)
rows = curs.fetchall()

curs.close()
conn.close()

output = []
for row in rows:
    print row
    output.append("%s" % "\t".join([str(x) for x in row]))

def main():
    write_votes(list2tsvx(output))

def write_votes(key):
    # Write the new votes to key.tsv file
    f = open("C:\PdV\data-tmp\key.tsv", "w")
    f.write(key)
    pprint.pprint(key)
    f.close()
    print " -> a new key.tsv writen in data-tmp/key.tsv"
    return

def list2tsvx(list):
    """
    list to string (in tsv format)
    """
    mytsv = "Topic\tjudge\tuser\tkeypad\tvote\tspeed\n"
    for line in list:
        mytsv += "%s\t" % line
        mytsv += "\n"
    mytsv = mytsv.strip()
    #print "mytsv:"
    #print mytsv
    return mytsv

##################
main()