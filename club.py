import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
mc = ['Sons','Mayans','Niners']
presidents = ['Jackie boy','Marcus Alvarez','Pope']
vpresidents = ['Chibs','Happy','August Marks']
memberno = [13,28,46]
club_label = ['mc','presidents','vpresidents','memberno']
club_columns = [mc, presidents, vpresidents, memberno]
club_zipped = list(zip(club_label,club_columns))
data = dict(club_zipped)
club_df=pd.DataFrame(data)
club_df.to_csv('C:/Users/omer/Desktop/club.csv',index=0)
club_csv=pd.read_csv('C:/Users/omer/Desktop/club.csv')#,index_col='mc')
#I don't use the code below because i already used index_col = 'mc'
#club_csv.set_index('mc',inplace=True)

i1 = 0
for x in memberno:

	if (x > 15) : 
		print(mc[i1] + ' is a large club')
		
	else:
		print(mc[i1] + ' is a small club')

	i1 = i1 + 1
mc_values=club_csv['mc'].values
memberno_values=club_csv['memberno'].values
#president_values=club_csv['presidents'].values
print(club_csv)
plt.plot(mc_values,memberno_values,'ro')
plt.show()
