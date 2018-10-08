import numpy as np
import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing


# df header looks like this:
# day start_city dest_city  travel_time  distance  delay
df = pd.read_csv('fd_data_out_w_tt.csv',sep=',',header=0)
# print(df.head())

c0 = df['start_city'].astype('category')
c0_list = c0.cat.categories.tolist()
print(c0_list)
c1 = df['dest_city'].astype('category')
c1_list = c1.cat.categories.tolist()

le = preprocessing.LabelEncoder()
le.fit(c0_list)
c0_list = le.transform(df['start_city']).tolist()
# print(df['start_city'])
# print(c0_list)
le.fit(c1_list)
c1_list = le.transform(df['dest_city']).tolist()

day_list = [day for day in df['day']]
tt_list = [tt for tt in df['travel_time']]
dist_list = [dist for dist in df['distance']]
delay_list = [delay for delay in df['delay']]
 
df_dict = {
	"day": day_list,
	"city_0": c0_list,
	"city_1": c1_list,
	"tt": tt_list,
	"dist": dist_list,
	"delay": delay_list 
}

data = pd.DataFrame(df_dict)
print(data.head())
data = data.dropna()

train, test = train_test_split(data,test_size=0.3)
# print(train.head())

X = train[['day','city_0','city_1','tt','dist']]
Y = train['delay']

# Train a decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

dot_data = tree.export_graphviz(clf,out_file="tree.dot")
graph = graphviz.Source(dot_data)
# print(graph)

# Test and evaluate by using accuracy score
X_test = test[['day','city_0','city_1','tt','dist']]
Y_test = test['delay']
Y_predict = clf.predict(X_test)
score = accuracy_score(Y_test,Y_predict)
print("Accuracy Score:", score)


