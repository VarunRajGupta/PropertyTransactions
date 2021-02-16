from csv import reader
import os
from datetime import datetime
import pandas as pd
from collections import defaultdict
import json

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

def file_key_generation(file_name,record_count,PAON_loc,SAON_loc,PC_loc,header_file):
	print(get_currenttime(),': Unique Proprty Key Generation step started')
	# change directory to File Path
	os.chdir(r'D:\VarunDocuments\Street_Assesment\Data\arrival')
	# Read CSV File as DataFrame
	data_file = pd.read_csv(file_name)
	# Declare Column Name for DataFrame
	data_file.columns = ['TUI','Price','DOT','PostCode','PropertyType','AgeIndicator','Duration','PAON','SAON','Street','Locality','Town','District','County','PPDCat','RecordStatus']
	data_file.to_csv(header_file)
	df = pd.read_csv(header_file)
	row_no = 0
	prop_key = []
	while row_no < record_count-1:
		prop_key_value = str(df.iloc[row_no,PC_loc]).replace(" ","")+"_"+str(df.iloc[row_no,PAON_loc])+"_"+str(df.iloc[row_no,SAON_loc])
		prop_key.append(prop_key_value)
		#print(get_currenttime(),': Row processed successfully - ', row_no)
		row_no = row_no + 1
	print(get_currenttime(),': Unique Property Key Generation step completed')
	return(prop_key)

def append_prop_key(file_name,prop_key):
	print(get_currenttime(),': Property Key append to dataframe started')
	# change directory to File Path
	os.chdir(r'D:\VarunDocuments\Street_Assesment\Data\arrival')
	# Read CSV File as DataFrame
	data_file = pd.read_csv(file_name)
	# Add Property Key to csv
	data_file['PropertyKey'] = prop_key
	print(get_currenttime(),': Property Key appended to dataframe completed')
	#print(data_file.iloc[10:20,])
	return(data_file)

def create_JSON(data_frame,json_file_name):
	print(get_currenttime(),': JSON File data genration started')
	json_file = defaultdict(list)
	for _id in data_frame.T:
		data = data_frame.T[_id]
		Key = data.PropertyKey
		for row in json_file[Key]:
			values = {'TUI': data.TUI, 'Price': data.Price, 'DOT': data.DOT, 'PostCode': data.PostCode, 'PropertyType': data.PropertyType, 'AgeIndicator': data.AgeIndicator, 'Duration': data.Duration, 'PAON': data.PAON, 'SAON': data.SAON, 'Street': data.Street, 'Locality': data.Locality, 'Town': data.Town, 'District': data.District, 'County': data.County, 'PPDCat': data.PPDCat, 'RecordStatus': data.RecordStatus}
			json_file[Key].append(values)
	print(get_currenttime(),': JSON File data genration completed, writing to file')
	with open(json_file_name, 'w') as jf:
		json.dump(json_file,jf,indent=4)
	print(get_currenttime(),': JSON File writing to file written successfully')



		
record_count = file_validation('pp2020.csv')
prop_key = file_key_generation('pp2020.csv',record_count,7,8,3,'pp2020_header.csv')
data_frame = append_prop_key('pp2020_header.csv',prop_key)  
create_JSON(data_frame,'pp2020.json')
