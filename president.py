"""This file choose 1 or 2 or n random values from active!=false in map.tsv and set those to active=block and rewrites map.tsv"""

# TODO: Need to rewrite map adding block to the chosen keypads

import sys
import pprint
import random

# Getting arguments first argument

#noinspection PyBroadException
try:
	sys.argv[1]
except:
	print
	print "Usage:"
	print "  python president.py [method]"
	print "Method can be:"
	print "* an integer: 1, 2"
	print "* or manual"
	sys.exit(1)
else:
	method = sys.argv[1]

#### Getting the data
map0 = open("data/map.tsv")
map = [i.strip().split() for i in map0.readlines()]

####################################
def main():
	print chooser(method,getvoters(map))


####################
def getvoters(map):
	choosed = []
	for voter in map:
		if voter[9] != "false" and is_number(voter[0]):
			choosed.append(voter[1])
	print " Possibles per elegir:"
	print choosed
	return choosed

def chooser(method, voters):
	chosen = []
	c = 0
	if is_number(int(method)):
		print "random escollit(s): "
		if len(voters) >= int(method):
			for x in range(int(method)):
				chosen.append(random.choice(voters))
				voters.remove(chosen[c])
				c += 1
		else:
			print "The method is too big"
			chosen = ["none"]
	elif method == "manual":
		print "random: "+method
	else:
		print "The method is not correct"
		chosen = ["none"]
	return chosen

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

###################
main()
