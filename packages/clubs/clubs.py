import os 
import csv
import pickle

def clubs_msg(result):
	try:
		club = result['parameters']['club']
	except:
		club = "The Lion"
	return find_clubs(club)

def make_club_dict():
	club_dict = {}
	club_file = open('./packages/clubs/clubs.csv')
	for club in club_file:
		club_info = club.split("\t")
		if len(club_info) < 2: 
			continue
		club_dict[club_info[0].strip()] = club_info[1].strip()
	club_file.close()
	output_file = open("./club_dict", "wb")
	pickle.dump(club_dict, output_file)
	output_file.close()

def find_clubs(club):
	club = club.lower()
	input_file = open("./club_dict", "rb")
	clubs_dict = pickle.load(input_file)
	input_file.close()
	results = []
	response = ""
	for club_name in clubs_dict.keys():
		club_name_lower = club_name.lower()
		if club in club_name_lower:
			club_result = club_name + ": " + clubs_dict[club_name] 
			results.append(club_result)

	"""

	- Modification: now find_clubs returns a list of strings instead of a single string
	- If the list is empty: no result is found
	- If the list has multiple entries: any one of them might be the club the user is looking for. In that case, the bot 
	  should handle the logic to check with the users which club is the one they want. 


	"""

	return results

	"""
	if len(results) == 0:
		msg = "Looks like I couldn't find any information about that club."
		return msg

	else:
		for line in results:
			response += line + "\n"
	response = response.rstrip()
	return response
	"""

