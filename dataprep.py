import numpy as np
import csv

with open('fd_data_raw.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=' ',quotechar='|')

	count = 0  # row count
	lists = []	# list of all csv data 
	sel_col = [3,6,9,11,12,16,14] # selected column of all csv data 
									   # day, start_city, dest_city, dept_time, arrv_time, distance, delay
	sel_len = len(sel_col)
	dept_time_idx = 11
	arrv_time_idx = 12

	def calc_travel_time(start_time,finish_time):
		# print(start_time,finish_time)
		
		if(len(start_time)==3):						# 835 -> 8:35
			start_hour = int(start_time[0:1])		
			start_minute = int(start_time[1:])
		elif(len(start_time)==4):					# 1540 -> 15:40
			start_hour = int(start_time[0:2])		
			start_minute = int(start_time[2:])
		else:
			return -1

		if(len(finish_time)==3):					# 835 -> 8:35
			finish_hour = int(finish_time[0:1])
			finish_minute = int(finish_time[1:])
		elif(len(finish_time)==4):					# 1540 -> 15:40
			finish_hour = int(finish_time[0:2])
			finish_minute = int(finish_time[2:])
		else:
			return -1

		start = start_hour*60 + start_minute
		finish = finish_hour*60 + finish_minute
		travel_time = finish-start 		# in a unit of minute

		return travel_time
		
	def cut_col(alist):	# remove unwanted columns
		nlist = []
		# print(alist)
		if(len(alist)==alength):
			for i in sel_col:
				if(alist[i]!=""):	# if string is not empty, remove " and spacebar
					alist[i] = alist[i].strip('" ')
				
				if(i==dept_time_idx):
					continue
				if(i==arrv_time_idx):
					travel_time = calc_travel_time(alist[dept_time_idx],alist[arrv_time_idx])
					if(travel_time == -1):
						continue
					alist[i] = travel_time
				
				nlist.append(alist[i])
			
			return nlist

	for row in csv_reader:
		# print(row)
		if(count>0):	# row 0 not used since it's the table header
			line = " ".join(row)
			# print(line)
			alist = line.split(',')
			alength = len(alist)  
			#print(alength)
			newlist = cut_col(alist)

			if(count<10):	
				print(newlist)

			lists.append(newlist)

		count += 1

	data_file = open('fd_data_out_w_tt.csv',mode='w')
	writer = csv.writer(data_file,delimiter=',',quotechar='|')

	list_header = ["day", "start_city", "dest_city", "travel_time", "distance", "delay"]
	writer.writerow(list_header)
	for e in lists:
		# day, start_city, dest_city, dept_time, arrv_time, distance, delay
		writer.writerow(e)





	


