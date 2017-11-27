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

    def __init__(self, num_plate_appearances, num_hits, num_doubles, num_triples, num_homeruns, num_singles, num_bb, batter_name):
    	self.num_plate_appearances =  num_plate_appearances
    	self.num_hits = num_hits
    	self.num_doubles = num_doubles
    	self.num_triples = num_triples
    	self.num_homeruns = num_homeruns
    	self.num_singles = num_singles
    	self.num_bb = num_bb
    	self.batter_name = batter_name



def init_batters():

	 with open(filename) as csvfile:
	 	spamreader = csv.reader(csvfile)
	 	for row in spamreader:
	 		print row[1]


init_batters()

    