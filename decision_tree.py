import numpy as np
import pandas as pd
# from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing

data = pd.read_csv('fd_data_out_w_tt.csv',sep=',',header=0)
# print(data.head())

c0 = data['start_city'].astype('category')
c0_list = c0.cat.categories.tolist()
# print(c0_list)

total_rows = len(data.index)

sc_column_index = 1
delay_column_index = 5

for index, c in enumerate(c0_list):
	data[c] = 0
	col_index = data.columns.get_loc(c)

	for x in range(total_rows):
		if c in data.iloc[x,sc_column_index]:
			data.iloc[x,delay_column_index+index] = 1
		else:
			data.iloc[x,delay_column_index+index] = 0

print(data.head())