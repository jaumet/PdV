import sys
import os
import pprint
import pyodbc
import shutil
import time

class mdb2tsv:
    def __init__(self):
        self.path = u'C:\\SunVote ARS 2010\\Resources\\DataBase\\'
        self.fn = ""

    def select_odbc(self,curs):
        # Get the votes:
        #SQL = 'SELECT R_KeypadID, R_Result, R_Speed FROM ARS_Response;' # insert your query here
        SQL = 'SELECT * FROM ARS_Response;' # insert your query here
        curs.execute(SQL)
        rows = curs.fetchall()
        return rows

    def clean_odbc(self,curs):
        # Clean the votes
        SQL = 'DELETE * FROM ARS_Response;' # insert your query here
        curs.execute(SQL)


    #####################################
    #### Getting the last file of a directory
    def getLastFile(self):
        os.chdir(self.path)
        files = filter(os.path.isfile, os.listdir(self.path))
        files.sort(key=lambda x: os.path.getmtime(x))
        fn1 = files[-1]
        print self.path
        fn1 = self.path+fn1
        self.fn = fn1.replace("\\", "\\\\")
        print "fn:"
        print self.fn
        #sys.exit()

        #### Check whether the *.ars file is empty
        if os.path.getsize(self.fn) > 0:
            print os.path.getsize(self.fn)
            pass
        else:
            print "-----------> ARS file is empty!!"
            print os.path.getsize(self.fn)
            sys.exit()
        #####################################
        #### cp last file everytime we want to read the votes (coz t
        #### he MS Access file looks like is blocked during votations
        #fn2 = u'C:\\PdV\\data-tmp\\00.ars'
        #shutil.copyfile(fn, fn2)
        print "- Size of "+self.fn
        print os.path.getsize(self.fn)

    #########################################
    #### pyodbc: getting the votes
    def getMBC_cursor(self):
        self.getLastFile()
        print self.fn
        MDB = self.fn
        DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'

        self.conn = pyodbc.connect('DRIVER=%s;DBQ=%s;' % (DRV,MDB))
        self.curs = self.conn.cursor()

    def cleanDatabase(self):
        self.getMBC_cursor()
        # delete all existing rows
        self.clean_odbc(self.curs)
        self.conn.commit()
        print "clean data done"

    def getAndCleanDatabase(self):
        self.getMBC_cursor()
        # backup data before clean
        rows = self.select_odbc(self.curs)
        # delete all existing rows
        self.clean_odbc(self.curs)
        # commit is very necessary to save changes in database.
        self.conn.commit()

        print "- Size after clean it:"
        print os.path.getsize(self.fn)

        # close database
        self.curs.close()
        self.conn.close()

        # output all row for debug
        self.output = []
        for row in rows:
            #print row
            self.output.append("%s" % "\t".join([str(x) for x in row]))



    def main(self):
        self.getAndCleanDatabase()
        self.write_votes(self.list2tsvx())

    def write_votes(self,key):
        # Write the new votes to key.tsv file
        f = open("C:\PdV\data-tmp\key.tsv", "w")
        f.write(key)
        #pprint.pprint(key)
        f.close()
        print " -> a new key.tsv writen in data-tmp/key.tsv"
        return

    def list2tsvx(self):
        """
        list to string (in tsv format)
        """
        list = self.output
        mytsv = "Topic\tjudge\tuser\tkeypad\tvote\tspeed\n"
        for line in list:
            mytsv += "%s\t" % line
            mytsv += "\n"
        mytsv = mytsv.strip()
        print "mytsv:"
        print mytsv
        return mytsv

    ##################

if __name__=="__main__":
    mymdb2tsv = mdb2tsv()
    mymdb2tsv.main()