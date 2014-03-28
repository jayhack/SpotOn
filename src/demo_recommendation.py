# Script: demo_recommendation
# ---------------------------
# script to demonstrate the recommendation capabilities
# of SpotOn class
import json
from SpotOn import SpotOn
from util import *
import numpy as np

if __name__ == "__main__":
	print_header ("RECOMMENDATION DEMO")

	#=====[ Step 1: construct/load SpotOn object	]=====
	so = SpotOn ()
	so.load ()
	


	#=====[ Step 2: get user, activities ]=====
	all_activities = json.load (open('activities_new.json', 'r'))
	user = [	
				all_activities[94], 
				all_activities[196], 
				all_activities[101], 
				all_activities[365]
			]
	activities = all_activities


	#=====[ DISPLAY USER ]=====
	print_header ("USER REP:")
	for activity in user:
		print activity['_source']['name'], " | ", activity['_source']['description']
		print '\n', '=' * 40, '\n'
	print "\n\n\n"

	#=====[ Step 3: get/display scores for activities	]=====
	scored_activities,act = so.score_activities (user, activities)
	sorted_act = np.argsort(scored_activities)[::-1]
	# sorted_activities = sorted(zip(activities, scored_activities), key=lambda x: x[1], reverse=True)
	print_header ("ACTIVITY RECOMMENDATIONS: ")
	for i in range(5):
		activity_index = sorted_act[i]
		print i, ": ", act.iloc[activity_index]
		print '\n', '='*40, '\n'
	# for activity, score in sorted_activities:
		# print score, ": ", activity['_source']['name'], " | ", activity['_source']['description']
		# print '\n', '=' * 40, '\n'



	