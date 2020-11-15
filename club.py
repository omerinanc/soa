import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

mc = ['Sons', 'Mayans', 'Niners']
presidents = ['Jackie boy', 'Marcus Alvarez', 'Pope']
vpresidents = ['Chibs', 'Happy', 'August Marks']
memberno = [13,28,46]

club_label = ['mc', 'presidents', 'vpresidents', 'memberno']
club_columns = [mc, presidents, vpresidents, memberno]
club_zipped = list(zip(club_label, club_columns))
data = dict(club_zipped)

filePath = './club.csv'

club_df = pd.DataFrame(data)
club_df.to_csv(filePath, index=0)
club_csv = pd.read_csv(filePath, index_col = 'mc')

# I don't use the code below because I already used index_col = 'mc'
# club_csv.set_index('mc', inplace = True)

print(club_csv)

i = 0
for x in memberno:
	if (x > 15) : 
		print(mc[i] + ' is a large club')
	else:
		print(mc[i] + ' is a small club')
	i = i + 1

#mc_values=club_csv['mc']
memberno_values=club_csv['memberno']

#president_values=club_csv['presidents'].values

plt.plot(memberno_values, 'ro')#this method takes the first name u use as 'y' values and set the index as 'x' values
plt.savefig('memberno_values.png')
plt.show
