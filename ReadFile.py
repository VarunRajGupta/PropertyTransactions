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



record_count = file_validation('pp2020.csv')
