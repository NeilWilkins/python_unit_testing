import matplotlib.mlab as ml
import numpy as np

def get_sightings(filename,animal):

	# Loading table
	tab = ml.csv2rec(filename)
	
	# Find total number of records for animal and calculate mean sightings
	isFocus = (tab['animal'] == animal)
	total_records = np.sum(isFocus)
	
	if total_records == 0:
		meanCount = 0
	else:
		meanCount = np.mean(tab['count'][isFocus])

	# Return number of records and animals seen
	return total_records, meanCount
	
