import sys
import os
import pprint
import csv
import pyodbc
import shutil
import pickle

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
print fn
#sys.exit()

#####################################
#### cp last file everytime we want to read the votes (coz t
#### he MS Access file looks like is blocked during votations
fn2 = u'C:\\PdV\\00.ars'
shutil.copyfile(fn, fn2)

#########################################
#### pyodbc: getting the votes
print fn2
MDB = fn2
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'

conn = pyodbc.connect('DRIVER=%s;DBQ=%s;' % (DRV,MDB))
curs = conn.cursor()

SQL = 'SELECT R_KeypadID, R_Result, R_Speed FROM ARS_Response;' # insert your query here
curs.execute(SQL)
rows = curs.fetchall()

curs.close()
conn.close()

output =[]
for row in rows:
    print row
    #pickle.dump("%s" % "\t".join([str(x) for x in row]), 'myoutput.tsv')
    output.append("%s" % "\t".join([str(x) for x in row]))
print output
print
