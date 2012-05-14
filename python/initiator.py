"""
initiator.oy

This script is checking and preparing the Pdv file system for a new show.
What it does?
#ToDo
1) Asks to make a copy of the [PdV\data\] and [PdV\data-tmp\] in [PdVlogs]
2) Put the default data for the theater in the main PdV directory. P.e.: PdV\PdVdefault\madrid\ -> [PdV\data\] and [PdV\data-tmp\]
"""
from cgi import logfile
import sys
import shutil
import time
from mdb2tsv import mdb2tsv
import re
import common

class Initiator:
    def __init__(self):
        """
        init def
        """
        '''
        print common.pdv
        self.pdvdir = "C:\\PdV\\"
        self.pdvdatadir = "C:\\PdV\\data"
        self.pdvdatatmpdir = "C:\\PdV\\data-tmp"
        self.pdvlog = "C:\\PdV\\PdVlogs\\"
        self.pdvdefault = "C:\\PdV\\PdVdefault\\"
        self.backup = ""
        '''

    def make_backup(self, pdvdatadir, pdvlog, pdvdatatmpdir, pdvdir, theater):
        """
        make a PdV back up moving the directory
        """
        logfile = pdvlog+"\\pdv_log-%s" % int(time.time())
        print
        print " ... moving "+pdvdatatmpdir+" to "+logfile+" ..."

        shutil.copytree(pdvdatatmpdir, logfile+"\\data-tmp", ignore=self.ignored_files)

        #shutil.copytree(pdvdatatmpdir, logfile+"\\data-tmp")
        print " ... moving "+pdvdatadir+" to "+logfile+" ..."
        shutil.copytree(pdvdatadir, logfile+"\\data", ignore=self.ignored_files)
        #shutil.copytree(pdvdatadir, logfile+"\\data")
        print "... Done"
        print
        return

    def ignored_files(self,adir,filenames):
        return [filename for filename in filenames if filename.endswith('svn')]

    def put_default_code(self, pdvdatadir, pdvdatatmpdir, pdvdefault, pdvdir):
        theater = "madrid"
        try:
            shutil.rmtree(pdvdatadir)
            print "Remove "+pdvdatadir+" done...."
            shutil.copytree(pdvdefault+theater+"\data", pdvdatadir , ignore=self.ignored_files)
            #shutil.copytree(pdvdefault+theater+"\\data", pdvdatadir)
        except OSError:
            print
            print "ERROR1: Copy "+pdvdefault+theater+"\data to "+pdvdatadir+" doesn't work."
            print "!!!!!!"
            sys.exit(2)
        try:
            shutil.rmtree(pdvdatatmpdir)
            print "Remove "+pdvdatatmpdir+" done...."
            shutil.copytree(pdvdefault+theater+"\data-tmp", pdvdatatmpdir, ignore=self.ignored_files)
        except:
            print
            print "ERROR2: Copy "+pdvdefault+theater+"\data-tmp to "+pdvdatatmpdir+" doesn't work."
            print "!!!!!!"
            sys.exit(2)
        print
        print " ... restarting PdV data from the directory "+pdvdefault+theater+" to the default directory ..."
        print "... Done"
        return

def main():
    # call method from mdb2tsv.py
    ##mymdb2tsv = mdb2tsv()
    ##mymdb2tsv.cleanDatabase()
    # start iniciator after clean
    
    X = Initiator()
    pdvdir = common.pdvbasedir
    pdvlog = common.pdvdatatmplog
    pdvdefault = common.pdvdefault
    pdvdatadir = common.pdvdata
    pdvdatatmpdir = common.pdvdatatmp

    # Getting the theater name (= directory name in PdV/PdVdefault/[theater]) from settings.xml
    # get number of members for each group from settings.xml
    xmldata = open(common.pdvsettings)
    xml = xmldata.readlines()

    for element in xml:
      if "<theater>" in element:
        print element
        element = element.strip()
        myelement = re.split('^<.*>(.*)<.*', element)
        theater = myelement[1]

    X.make_backup(pdvdatadir, pdvlog, pdvdatatmpdir, pdvdir, theater)
    		
    print "Number of member per group:)"
    print group_number_members 

    print
    X.put_default_code(pdvdatadir, pdvdatatmpdir, pdvdefault, pdvdir)
    print
    print "All done. Bye!"
    return
########################
main()
sys.exit(2)
