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
        self.pdvlog = "C:\\PdVlogs\\"
        self.pdvdefault = "C:\\PdV\\default\\"
        self.backup = ""

    def make_backup(self, pdvdir, pdvlog, pdvdefault):
        """
        make a PdV back up moving the directory
        """
        logfile = pdvlog+"\\pdv_log-%s" % int(time.time())
        print " ... moving "+pdvdir+" to "+logfile+" ..."
        shutil.move(pdvdir, logfile)
        print "... Done"
        return

    def put_default_code(self, pdvdir, pdvlog, pdvdefault):
        print " ... restarting PdV code from the directory "+pdvdefault+" to the default directory "+pdvdir+" ..."
        shutil.move(pdvdir, logfile)
        print "... Done"
        return

def main():
    X = Initiator()
    pdvdir = X.pdvdir
    pdvlog = X.pdvlog
    pdvdefault = X.pdvdefault
    backup = raw_input(" -> Step 1/4 :do you want to make a backup copy of "+pdvdir+" and move it to the directory "+pdvlog+"?")
    if backup == "y":
        X.make_backup(pdvdir, pdvlog, pdvdefault)
        print " ... Done"
    else:
        print pdvdir+" directory has not been changed at all."
        print
    print " -> Step 2/4 : KeypadIDs-SeatsIDs synchronization."
    print "Is this done? You need to open Sunvote software and check one by one the keypads and stick on their number"
    print "No? Then you need to edit "+pdvdir+"\\data\\map.tsv, the 2ond column, keypadID and fill it up"
    put_default = raw_input(" -> Step 3/4: Add the default PdV code to "+pdvdir+"? (y/n)")
    if put_default == "y":
        X.put_default_code(pdvdir, pdvlog, pdvdefault)
        l = "... Done"
    return
########################
main()
sys.exit(2)