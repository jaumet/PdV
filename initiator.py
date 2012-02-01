"""
initiator.oy

This script is checking and preparing the Pdv file system for a new show.
What it does?
1) Asks to make a copy of the [PdV directory] in [log directory]
2)
"""
from cgi import logfile
import sys
import shutil
import time

class Initiator:
    def __init__(self):
        """
        init def
        """
        self.pdvdir = "C:\\PdV\\"
        self.pdvdatadir = "C:\\PdV\\data\\"
        self.pdvdatatmpdir = "C:\\PdV\\data-tmp\\"
        self.pdvlog = "C:\\PdV\\PdVlogs\\"
        self.pdvdefault = "C:\\PdV\\PdVdefault\\"
        self.backup = ""

    def make_backup(self, pdvdatadir, pdvlog, pdvdatatmpdir):
        """
        make a PdV back up moving the directory
        """
        logfile = pdvlog+"\\pdv_log-%s" % int(time.time())
        print
        print " ... moving "+pdvdatatmpdir+" to "+logfile+" ..."
        shutil.copytree(pdvdatatmpdir, logfile+"\\data-tmp")
        print " ... moving "+pdvdatadir+" to "+logfile+" ..."
        shutil.copytree(pdvdatadir, logfile+"\\data")
        print "... Done"
        print
        return

    def put_default_code(self, pdvdatadir, pdvdatatmpdir, pdvdefault):
        theater = raw_input(" -> Which theater (madrid)?")
        if theater == "madrid":
            #shutil.copytree(pdvdefault+theater+"\\data-tmp", pdvdatadir)
            try:
                #shutil.move(pdvdir+"\\data-tmp", pdvdir+"\\data-tmpLALALA")
                shutil.copytree(pdvdefault+theater+"\\data", pdvdatadir)
                shutil.copytree(pdvdefault+theater+"\\data-tmp", pdvdatatmpdir)
            except:
                print "The path "+pdvdefault+theater+"\\data-tmp doesn't exist or is not accessible."
                print "Create it run again this script"
                print "bye!"
                sys.exit(2)
            print " ... restarting PdV code from the directory "+pdvdefault+theater+" to the default directory ..."
            print "... Done"
        else:
            print "I cannot find "+pdvdefault+theater+"\\data-tmp. Default data not copyed (!)"
        return

def main():
    X = Initiator()
    pdvdir = X.pdvdir
    pdvlog = X.pdvlog
    pdvdefault = X.pdvdefault
    pdvdatadir = X.pdvdatadir
    pdvdatatmpdir = X.pdvdatatmpdir
    backup = raw_input(" -> Step 1/4 :do you want to make a backup copy of "+pdvdir+" and move it to the directory "+pdvlog+"?")
    if backup == "y":
        X.make_backup(pdvdatadir, pdvlog, pdvdatatmpdir)
        print " ... Done"
    else:
        print pdvdir+" directory has not been changed at all."
        print
    print " -> Step 2/4 : KeypadIDs-SeatsIDs synchronization."
    print "Is this done? You need to open Sunvote software and check one by one the keypads and stick on their number"
    print "No? Then you need to edit "+pdvdir+"\\data\\map.tsv, the 2ond column, keypadID and fill it up"
    put_default = raw_input(" -> Step 3/4: Add the default PdV data-tmp to "+pdvdir+" ? (y/n)")
    if put_default == "y":
        X.put_default_code(pdvdatadir, pdvdatatmpdir, pdvdefault)
        l = "... Done"
    return
########################
main()
sys.exit(2)