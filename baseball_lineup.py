#author: Billy Fallon
#version: 1.0
#date last updated: 11/26/17

import random
import csv

filename = 'yankees_2016.csv'

class batter(object):

    """
		Attributes:
			num_plate_appearances
			num_hits
			num_doubles
			num_triples
			num_homeruns
			num_singles
			num_bb
			batter_name
    """

    def __init__(self, num_plate_appearances, num_hits, num_doubles, num_triples, num_homeruns, num_bb, num_hbp, batter_name):
    	self.num_plate_appearances =  int(num_plate_appearances)
    	self.num_hits = int(num_hits)
    	self.num_doubles = int(num_doubles)
    	self.num_triples = int(num_triples)
    	self.num_homeruns = int(num_homeruns)
    	self.num_singles = int(num_hits) - int(num_doubles) - int(num_triples) - int(num_homeruns)
    	self.num_bb = int(num_bb) + int(num_hbp)
    	self.batter_name = batter_name



def init_batters():
	batters = []

	with open(filename) as csvfile:
	 	spamreader = csv.reader(csvfile)
	 	count = 0
	 	for row in spamreader:
	 		if count == 11:
	 			break
	 		if count == 0:
	 			count = count + 1
	 		elif count == 9:
	 			count = count + 1
	 		else:
	 			temp = batter(row[5], row[8], row[9], row[10], row[11], row[15], row[24], row[2])
	 			batters.append(temp)
	 			count = count + 1
	return batters

	 		
def simulate_at_bat(state, batter):
    rand = random.randint(1,batter.num_plate_appearances)
    
    #a single is hit
    if 1 < rand < batter.num_singles:
        if state[0] == 0:
            state[0] = 1
        
        elif state[0] == 1:
            state[0] = 4
        
        elif state[0] == 2:
            state[0] = 1
            state[2] = state[2] + 1
        
        elif state[0] == 3:
            state[0] = 1
            state[2] = state[2] + 1
        
        elif state[0] == 4:
            state[0] = 4
            state[2] = state[2] + 1
        
        elif state[0] == 5:
            state[0] = 4
            state[2] = state[2] + 1
        
        elif state[0] == 6:
            state[0] = 1
            state[2] = state[2] + 2
        
        elif state[0] == 7:
            state[0] = 4
            state[2] = state[2] + 2
    
    #a double is hit
    elif batter.num_singles < rand < batter.num_singles + batter.num_doubles:
        if state[0] == 0:
            state[0] = 2
        
        elif state[0] == 1:
            state[0] = 6
        
        elif state[0] == 2:
            state[0] = 2
            state[2] = state[2] + 1
        
        elif state[0] == 3:
            state[0] = 2
            state[2] = state[2] + 1
        
        elif state[0] == 4:
            state[0] = 6
            state[2] = state[2] + 1
        
        elif state[0] == 5:
            state[0] = 6
            state[2] = state[2] + 1
        
        elif state[0] == 6:
            state[0] = 2
            state[2] = state[2] + 2
        
        elif state[0] == 7:
            state[0] = 6
            state[2] = state[2] + 2

    #a triple is hit
    elif batter.num_singles + batter.num_doubles < rand < batter.num_singles + batter.num_doubles + batter.num_triples:
        if state[0] == 0:
            state[0] = 3
        
        elif state[0] == 1:
            state[0] = 3
            state[2] = state[2] + 1

        elif state[0] == 2:
            state[0] = 3
            state[2] = state[2] + 1
        
        elif state[0] == 3:
            state[0] = 3
            state[2] = state[2] + 1

        elif state[0] == 4:
            state[0] = 3
            state[2] = state[2] + 2
        
        elif state[0] == 5:
            state[0] = 3
            state[2] = state[2] + 2

        elif state[0] == 6:
            state[0] = 3
            state[2] = state[2] + 2
        
        elif state[0] == 7:
            state[0] = 3
            state[2] = state[2] + 3

    #a homerun is hit
    elif batter.num_singles + batter.num_doubles + batter.num_triples < rand < batter.num_singles + batter.num_doubles + batter.num_triples + batter.num_homeruns:
        if state[0] == 0:
            state[0] = 0
            state[2] = state[2] + 1
        
        elif state[0] == 1:
            state[0] = 0
            state[2] = state[2] + 2

        elif state[0] == 2:
            state[0] = 0
            state[2] = state[2] + 2
        
        elif state[0] == 3:
            state[0] = 0
            state[2] = state[2] + 2

        elif state[0] == 4:
            state[0] = 0
            state[2] = state[2] + 3
        
        elif state[0] == 5:
            state[0] = 0
            state[2] = state[2] + 3

        elif state[0] == 6:
            state[0] = 0
            state[2] = state[2] + 3
        
        elif state[0] == 7:
            state[0] = 0
            state[2] = state[2] + 4
            #grandslam!

    #batter is walked
    elif batter.num_singles + batter.num_doubles + batter.num_triples + batter.num_homeruns < rand < batter.num_singles + batter.num_doubles + batter.num_triples + batter.num_homeruns + batter.num_bb:
        if state[0] == 0:
            state[0] = 1
        
        elif state[0] == 1:
            state[0] = 4

        elif state[0] == 2:
            state[0] = 4
        
        elif state[0] == 3:
            state[0] = 5

        elif state[0] == 4:
            state[0] = 7
        
        elif state[0] == 5:
            state[0] = 7
        
        elif state[0] == 6:
            state[0] = 7

        elif state[0] == 7:
            state[0] = 7
            state[2] = state[2] + 1

    #batter is out (need to add double play funcitonality)
    else:
        state[1] = state[1] + 1
    
    return state


def simulate_game(num_games, batters):


	count = 0
	inning = 1#represents current innning of game
	batter = 0#represents which batter is at bat
	total_runs = 0

	while count < num_games:
		count = count + 1
		inning = 1
		batter = 0
		while inning < 10:
			inning = inning + 1
			state = [0, 0, 0]
			while state[1] < 3:
				state = simulate_at_bat(state, batters[batter])
	        	if batter == 8:
	        		batter = 0
	        	else:
	        		batter = batter + 1
			total_runs = total_runs + state[2]
		
	return total_runs/float(9)


batters = init_batters()

runs = simulate_game(100000, batters)
print("Average runs per inning with 2016 NYY Batting Order: ")
print(runs/float(100000))

batters_new = []
batters_new.append(batters[5])
batters_new.append(batters[0])
batters_new.append(batters[4])
batters_new.append(batters[6])
batters_new.append(batters[3])
batters_new.append(batters[2])
batters_new.append(batters[1])
batters_new.append(batters[7])
batters_new.append(batters[8])




runs = simulate_game(100000, batters_new)
print("Average runs per inning with batting order organized by OBP: ")
print(runs/float(100000))

batters_new.reverse()
runs = simulate_game(100000, batters_new)
print("Average runs per inning with batting order organzied by OBP reversed: ")
print(runs/float(100000))

random.shuffle(batters_new)
runs = simulate_game(100000, batters_new)
print("Average runs per inning with batting order randomized: ")
print(runs/float(100000))











    