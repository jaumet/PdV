"""This file choose 1 or 2 or n random values from active!=false in map.tsv and set those to active=block and rewrites map.tsv"""

import sys
import pprint
import random

# Getting arguments first argument
usage = """
	Usage:
		python president.py [number] [type]
		* number can be: an integer > 0: 1, 2, 3, 4,...
		* type can be: president OR tribunal OR ejercito
		"""


#noinspection PyBroadException
try:
	sys.argv[1]
except:
	print usage
	sys.exit(1)
else:
	method = sys.argv[1]

#noinspection PyBroadException
try:
	sys.argv[2]
except:
	print usage
	sys.exit(1)
else:
	type = sys.argv[2]

#### Getting the data
map0 = open("data/map.tsv")
map = [i.strip().split() for i in map0.readlines()]

####################################
def main():
	update_map(type, map, chooser(method,getvoters(map)))
	print "Has beed chosen "+method+" users as \""+type+"\""

def getvoters(map):
	"""
	 Getting the voter that can be eligible (active not false voters)
	 """
	eligible = []
	for voter in map:
		if voter[9] != "false" and is_number(voter[0]) and voter[8] == "null":
			eligible.append(voter[1])
	print " Possibles per elegir:"
	print eligible
	return eligible

def chooser(number, voters):
	"""
	Choose random users from available ones and check if is possible to choose them
	"""
	chosen = []
	c = 0
	if is_number(int(number)):
		print "random chosen: "
		if len(voters) >= int(number):
			for x in range(int(number)):
				chosen.append(random.choice(voters))
				voters.remove(chosen[c])
				c += 1
		elif len(voters) < 1:
			print "No eligible voters available!"
		else:
			print "The method is too big"
			chosen = ["none"]
	elif number == "manual":
		print "random: "+number
	else:
		print "The method is not correct"
		chosen = ["none"]
	print chosen
	return chosen

def update_map(type, map, chosen):
	mytsv = ""
	for line in map:
		if line[1] in chosen and line[8] == "null":
			line[8] = type
			line[9] = "block"
			#print line
		for l in line:
			mytsv += "%s\t" % l
		mytsv += "\n"
	mytsv = mytsv.strip()
	#pprint.pprint(mytsv)
	# Write the new map to this tsv file
	fn = "data/map.tsv"
	f = open(fn, "w")
	f.write(mytsv)
	#pprint.pprint("%s\n" % "\t".join([str(x) for x in entry]))
	f.close()
	print ' -> a new map.tsv writen'
	return

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

###################
main()
