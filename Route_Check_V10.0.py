#!/usr/bin/env python
"""Route_Check_V10.0.py: Calculates minimum number of stops based on Range/Distance"""
__author__ = "Jonathan Alejandro"
__copyright__ = "Copyright 2018, The Min Stop Project"
__credits__ = ["Jonathan Alejandro", "Dhivarhar Premaul", "Jose Oliveras"]
__license__ = "GPL"
__version__ = "10.0"
__maintainer__ = "Jonathan Alejandro"
__email__ = "brisbraniac@hotmail.com"
__status__ = "Production"
from itertools import combinations
from operator import itemgetter
def validate_route(route):
	x = 0
	y = 1
	pos = 0
	gas = 0
	start_pos = route[0][0]
	start_gas = route[0][1]
	gas += start_gas
	pos += start_pos
	while x < len(route) - 1:
		stop = route[x]
		next_stop = route[y]
		t1 = next_stop[0] - stop[0]
		if gas >= t1:
			#print('Traveling from :' , pos, 'To' ,next_stop[0] , 'with' , gas, 'Gallons of Gas')
			gas -= t1
			#print(gas , 'Tank after travel')
			gas += next_stop[1]
			#print(gas, 'tank after refueling')
			pos -= pos
			pos += next_stop[0]
			x += 1
			y += 1
		else:
			#print('Invalid Steps')
			#print(gas , t1)
			x += 9999
		count = x - 1
	if count >= 0:
		return count
	else:
		return 999		
def enum_routes(tank,target,stations,inventory):
	nodes = []
	nodes.append((0, tank))
	routes = []
	while len(stations) > 0:
		nodes.append((stations[0], inventory[0]))
		inventory.remove(inventory[0])
		stations.remove(stations[0])
	nodes.append((target , 0))
	#print('Nodes' , nodes)
	r = len(nodes)
	while r > 0:
		x = combinations(nodes,r)
		for i in x:
			if i[0] == (0, tank) and i[-1] == (target , 0):
				routes.append(i)
		r -= 1
	answers = []
	for route in routes:
		#print(route)
		answer = validate_route(route)
		answers.append(answer)
	print('Minimum' , min(answers) , 'Stop/s needed')
def datas():
	usr_in1 = input('Destination: ')
	usr_in2 = input('Current Fuel: ')
	if usr_in1.isdigit()and usr_in2.isdigit():
		target = int(usr_in1)
		tank = int(usr_in2)
	usr_in3 = input('How many stations: ')
	inputs_a = int(usr_in3)
	stations = []
	inventory = []
	while inputs_a > 0:
		usr_inb = input('Stations Dist: ')
		usr_inc = input('Stations Inventory: ')
		if usr_inb.isdigit() and usr_inc.isdigit():
			stations.append(int(usr_inb))
			inventory.append(int(usr_inc))
		else:
			print("Integer Values only")
			raise SystemExit
		inputs_a -= 1
	enum_routes(tank,target,stations,inventory)	
if __name__ == "__main__":	
	datas()