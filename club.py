import pandas as pd 
mc = ['Sons','Mayans','Niners']
presidents = ['Jackie boy','Marcus Alvarez','Pope']
vpresidents = ['Chibs','Happy','August Marks']
memberno = [13,28,46]
club_label = ['mc','presidents','vpresidents','memberno']
club_columns = [mc, presidents, vpresidents, memberno]
club_zipped = list(zip(club_label,club_columns))
data = dict(club_zipped)
club_df=pd.DataFrame(data)
club_df.set_index('mc', inplace=True)
club_df.to_csv('C:/Users/omer/Desktop/club.csv')
club_csv=pd.read_csv('C:/Users/omer/Desktop/club.csv')
print(club_csv)
i1 = 0
for x in memberno:

	if (x > 15) : 
		print(mc[i1] + ' is a large club')
		
	else:
		print(mc[i1] + ' is a small club')

	i1 = i1 + 1