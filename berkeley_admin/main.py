import pandas as pd

df = pd.read_csv('berkeley.csv')

male_admit = 0
female_admit = 0
male_total = 0
female_total = 0


for i in range(0, 24):
	if df.loc[i]['Gender'] == "Male":
		male_total += df.loc[i]['Freq']

		if df.loc[i]['Admit'] == "Admitted":
			male_admit += df.loc[i]['Freq']

	if df.loc[i]['Gender'] == "Female":
		female_total += df.loc[i]['Freq']

		if df.loc[i]['Admit'] == "Admitted":
			female_admit += df.loc[i]['Freq']

print(1 - male_admit / male_total)
print(1 - female_admit / female_total)