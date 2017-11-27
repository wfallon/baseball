#author: Billy Fallon
#version: 1.1
#date last updated: 11/26/17

import random
import csv


filename = 'yankees_2016.csv'

#2016 NYY batting data (baseball-reference.com)
num_plate_appearances = 6059

num_hits = 1378

num_doubles = 245

num_triples = 20

num_homeruns = 183

num_singles = num_hits - num_doubles - num_triples - num_homeruns

num_bb = 536 #this includes walks and hit by pitch


num_outs = num_plate_appearances - num_hits - num_bb
#need more accurate data for probability of double play, will tentatively use an estimate

num_double_plays = 100

num_single_outs = num_outs - num_double_plays

def calculate_probability(item, total):
    return item/float(total)

def simulate_at_bat(state):
    rand = random.randint(1,num_plate_appearances)
    
    #a single is hit
    if 1 < rand < num_singles:
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
    elif num_singles < rand < num_singles + num_doubles:
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
elif num_singles + num_doubles < rand < num_singles + num_doubles + num_triples:
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
elif num_singles + num_doubles + num_triples < rand < num_singles + num_doubles + num_triples + num_homeruns:
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
elif num_singles + num_doubles + num_triples + num_homeruns < rand < num_singles + num_doubles + num_triples + num_homeruns + num_bb:
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






#returns number of runs in num_innings amount of innnings
def inning(num_innings):
    count = 0
    total_runs = 0
    while count < num_innings:
        outs = 0
        
        #first index of state represents runners on bases, second index represents outs, third index represents runs scored in the inning
        #for the first index, 0 indicates no runners on bases,
        #1 indicates 1 runner on first,
        #2 indicates 1 runner on second,
        #3 indicates 1 runner on third,
        #4 indicates 1 runner on 1st and 1 runner on 2nd,
        #5 indicates 1 runnner on 1st and 1 runner on 3rd,
        #6 indicates 1 runner on 2nd and 1 runner on 3rd,
        #7 indicates 1 runner on 1st, 1 runner on 2nd, and 1 runner on 3rd
        state = [0, 0, 0]
        
        while state[1] < 3:
            state = simulate_at_bat(state)
        
        total_runs = total_runs + state[2]
        count = count + 1
    
    return total_runs


#analyzes the success of a sacrifice bunt in terms of its effects on expected runs
def sacrifice_bunt_simulation (num_innings, initial_outs):
    count = 0
    total_runs = 0
    
    #finding average for one runner on first
    while count < num_innings:
        state = [1, initial_outs, 0] #runner on first with amount of outs set equal to initial_outs parameter
        
        while state[1] < 3:
            state = simulate_at_bat(state)
        
        total_runs = total_runs + state[2]
        count = count + 1
    
    print("Initial Outs: ")
    print(initial_outs)

print("\nExpected runs per inning with a batter on first:")
    print(total_runs/float(num_innings))
    
    count = 0
    total_runs = 0
    
    #finding average after the runner on first advanced to second after a sacrifice bunt
    while count < num_innings:
        state = [2, initial_outs + 1, 0] #runner on second with amount of outs set equal to initial_outs parameter + 1
        
        while state[1] < 3:
            state = simulate_at_bat(state)
        
        total_runs = total_runs + state[2]
        count = count + 1
    
    print("\nExpected runs per inning after the runner on first advanced to second after a sacrifice bunt:")
    print(total_runs/float(num_innings))






sacrifice_bunt_simulation(10000, 0)
