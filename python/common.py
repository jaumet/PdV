'''
	common path's vars for PdV
'''
pdvbasedir = "/home/j/Desktop/Suntests/PdV/" # with trailing slash at the end

# From here on: NO TRAILING SLASH AT THE BEGINNING, coz they are all appended to pdvbasedir
# And, with trailing slash at the end

pdvbasedir = "C:\\PdV\\" # with trailing slash at the end

# From here on: NO TRAILING SLASH AT THE BEGINNING, coz they are all appended to pdvbasedir

# And, with trailing slash at the end
pdvdefault = pdvbasedir+"PdVdefault\\" 

# FIXME From the run file -> take from settings.xml the name of the dir inside pdvlogs were default data is (f.e. "madrid\\")
pdvlogs = pdvbasedir+"PdVlogs\\"

pdvdata = pdvbasedir+"data\\"
pdvdatatmp = pdvbasedir+"data-tmp\\"
pdvdatatmplog = pdvbasedir+"data-tmp\\log\\"

pdvsettings = pdvbasedir+"OF\\pdv\\bin\\data\\settings.xml"
pdvpngs = pdvbasedir+"data\\png_export_export\\"

'''
# common.py usage from another file:

import common
c = common

THEN:

print c.pdvdefault

OR:

class Mydef():
	def mydef(self):
		print "Inside class method: "+c.pdvdefault
	
m = Mydef()
m.mydef()
'''
