import numpy as np
import pandas as pd


df = pd.read_csv('train.csv')
df_no_fare = df.copy()
del df_no_fare['Fare']

df_no_name = df_no_fare.copy()
del df_no_name['Name']
del df_no_name['Cabin']

del df_no_name['Ticket']
#print(df_no_name.columns)


df = df_no_name.copy()

for passenger_index, passenger in df.iterrows():
	gender = passenger['Sex']

	if gender == 'male':
		df['Sex'][passenger_index] = 0

	if gender == 'female':
		df['Sex'][passenger_index] = 1


print(df.loc[0])

