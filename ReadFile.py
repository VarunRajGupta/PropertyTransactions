from csv import reader
import os
from datetime import datetime
import pandas as pd

def get_currenttime():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	return current_time

def file_validation(file_name):
	counter = 0
	print(get_currenttime(),': File validation started')
	# change directory to File Path
	os.chdir(r'D:\VarunDocuments\Street_Assesment\Data\arrival')
	# open file in read mode
	with open(file_name, 'r') as read_item:
		csv_row = reader(read_item)
		for row in csv_row:
			counter = counter+1

	print("File contains -",counter," records")
	print(get_currenttime(),": File validation completed")
	return counter

def file_key_generation(file_name,record_count,PAON_loc,SAON_loc):
	print(get_currenttime(),': Unique Proprty Key Generation step started')
	# change directory to File Path
	os.chdir(r'D:\VarunDocuments\Street_Assesment\Data\arrival')
	# Read CSV File as DataFrame
	data_file = pd.read_csv(file_name)
	# Declare Column Name for DataFrame
	data_file.columns = ['TUI','Price','DOT','PostCode','PropertyType','AgeIndicator','Duration','PAON','SAON','Street','Locality','Town','District','County','PPDCat','RecordStatus']
	row_no = 0
	prop_key = []
	while row_no < record_count-1:
		prop_key_value = str(data_file.iloc[row_no,PAON_loc])+"_"+str(data_file.iloc[row_no,SAON_loc])
		prop_key.append(prop_key_value)
		#print(get_currenttime(),': Row processed successfully - ', row_no)
		row_no = row_no + 1
	print(get_currenttime(),': Unique Property Key Generation step completed')
	return(prop_key)

record_count = file_validation('pp2020.csv')
prop_key = file_key_generation('pp2020.csv',record_count,7,8)


