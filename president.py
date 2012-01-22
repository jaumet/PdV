"""This file choose 1 or 2 or n random values from active!=false in map.tsv and set those to active=block and rewrites map.tsv"""

# TODO: Need to rewrite map.tav adding block to the chosen keypads and type (president)

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

def getvoters(map):
	"""
	 Getting the voter that can be eligible (active not false voters)
	 """
	eligible = []
	for voter in map:
		if voter[9] != "false" and is_number(voter[0]):
			eligible.append(voter[1])
	print " Possibles per elegir:"
	print eligible
	return eligible

def chooser(method, voters):
	"""
    Choose random users from available ones and check if is possible to choose them
    """
	chosen = []
	c = 0
	if is_number(int(method)):
		print "random escollit(s): "
		if len(voters) >= int(method):
			for x in range(int(method)):
				chosen.append(random.choice(voters))
				voters.remove(chosen[c])
				c += 1
		elif len(voters) < 1:
			print "No eligible voters available!"
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
