"""
Recolocation2
"""

import random
import pprint
import os
import sys
import re
import common

#####################################################
# CONFIGURATION:

# get number of members for each group from settings.xml
xmldata = open(common.pdvsettings)
xml = xmldata.readlines()

for element in xml:
	if "group_number_members" in element:
		print element
		element = element.strip()
		myelement = re.split('.*>(.*)<.*', element)
		print myelement[1]
group_number_members_strings = myelement[1].split(",")
# Convert strings to int
group_number_members = []
for k in group_number_members_strings: 
    group_number_members.append(int(k)) 
    	
print "Number of member per group:)"
print group_number_members

# Number of groups:
number_of_groups = len(group_number_members)

# Number of seats
seats = 0
for g in group_number_members:
	seats += g

print "Number of seats: "+str(seats)

# set here the first seatid for each group
group_start_seatid = [1]
c = 0
start_seatid = 0
for g in group_number_members:
	print group_number_members[c]
	start_seatid = start_seatid + group_number_members[c]
	group_start_seatid.append(start_seatid)
	c += 1
group_start_seatid.pop(len(group_number_members))
print group_start_seatid
#sys.exit()

# Get the map.tsv
file = common.pdvdata+"map.tsv"
f = open(file)
map = [i.strip().split() for i in f.readlines()]

#####################################################
# functions
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def p(x):
	pprint.pprint(x)

# Put keypads-data (keypadid, group, type, active, gender) falses & active lists and block all active ones
actives = []
falses = []
for line in map:
	if is_number(line[0]):
		if line[9] != "false":
			line[9] = "block"
			actives.append([line[1], line[7], line[8], line[9], line[10]])
		else:	
			falses.append([line[1], line[7], line[8], line[9], line[10]])
			
# Active/false stats:
print "Actives: "
print "- len activess = "+str(len(actives))
print "- Actives per group = "+str(len(actives)/number_of_groups)
active_per_group = len(actives) -(len(actives)/number_of_groups)*number_of_groups
print "Sobren = "+str(len(actives) -(len(actives)/number_of_groups)*number_of_groups)
print
print "Falses: "
print "- len falses = "+str(len(falses))
print "- Falses per group = "+str(len(falses)/number_of_groups)
print "Sobren = "+str(len(falses) -(len(falses)/number_of_groups)*number_of_groups)
print

# Define groups lists 
G = []
for i in range(number_of_groups):
	G.append([])
p(G)

# Distributing falses in each empty group
lastLoop = 0
totalLoop = len(falses)*2
while len(falses)>0 and lastLoop<totalLoop:
	c = 0
	for i in G:
		if len(i) < group_number_members[c]:
			if len(falses) > 0:
				i.append(falses[0])
				falses.pop(0)
		c += 1
	lastLoop+=1

# Distributing actives in each group
activesGroups = []
for i in range(number_of_groups):
	activesGroups.append([])
	
c = 0
for i in activesGroups:
	while len(G[c]) < group_number_members[c] and len(actives) > 0: 
		if group_number_members[c]>(len(G[c])+len(i)):
			i.append(actives[0])
			actives.pop(0)
		else:
			break
	random.shuffle(i)
	print "len(group_list) -> "+str(len(i))
	c += 1
print "------"
print len(G[0])
print "--------"
p(activesGroups)
#sys.exit()
c = 0
for i in G:
	i.extend(activesGroups[c])
	i.reverse()
	c += 1

# Choose 1 voter per group
chosen = []
chosen_tmp = []
for group in G:
	print "len group: "+str(len(group))
	chosen_tmp = []
	while len(chosen_tmp) < 1:
		chosen_tmp = random.choice(group)
		if chosen_tmp[2] == "null" and chosen_tmp[3] != "false":
			chosen.append(chosen_tmp)
		else:
			chosen_tmp = []
p(chosen)
# Activate chosen voters. And shuffle & join groups
for group in G:
	for g in group:
		if g in chosen:
			print "chosen!"
			print g
			g[3] = "true"
			print "And changed to:"
			print g
			print

map_kp = []
for group in G:
	map_kp.extend(group)

# Combine original map with the new keypads data
l = 0
for line in map:
	if is_number(line[0]):
		line[1], line[7], line[8], line[9], line[10] = map_kp[l]
		l += 1

# Adding group number
group_start_seatid.append(seats)
for line in map:
	if is_number(line[0]):
		for i in range(number_of_groups+1):
			if int(line[0]) == 1:
				line[7] = str(1)
			if group_start_seatid[i-1] < int(line[0]) <= group_start_seatid[i]:
				line[7] = str(i)
				#print " -> "+str(group_start_seatid[i-1])+" <= "+str(int(line[0]))+" < "+str(group_start_seatid[i])
			if int(line[0]) == group_start_seatid[i]:
				line[7] = str(i)

# Write back map.tsv
map_new = ""
recolocation2_table = []
for line in map:
	if is_number(line[0]):
		# Building recolocation2 table: keypadID - seatID
		recolocation2_table.append([int(line[0]),int(line[1])])
	for l in line:
		map_new += "%s\t" % l
	map_new = map_new.strip()
	map_new += "\n"
map_new = map_new.strip()
f = open(file, "w")
f.write(map_new)
f.close()

# Sorting recolocation2 table by keypadID
recolocation2_sorted = sorted(recolocation2_table, key=lambda x: x[0])
# Write recolocation2.tsv
recolocation2 = "keypadID -> seatID\n"
for line in recolocation2_sorted:
	for l in line:
		recolocation2 += "%s\t" % l
	recolocation2 = recolocation2.strip()
	recolocation2 += "\n"
recolocation2 = recolocation2.strip()
ff = open(common.pdvdatatmp+"recolocation2.tsv", "w")
ff.write(	recolocation2)
ff.close()
