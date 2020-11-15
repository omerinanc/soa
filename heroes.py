import pandas as pd
import matplotlib.pyplot as plt

heroes_level = ['1','2','3']
heroes_gold = ['1','3','5']
heroes_damage_1gold = ['100','200','300']
heroes_damage_3gold = ['200','350','550']
heroes_damage_5gold = ['300','500','1000']

heroes_label = ['level','1','3','5']
heroes_column = [heroes_level,heroes_damage_1gold,heroes_damage_3gold,heroes_damage_5gold]
heroes_zipped = list(zip(heroes_label,heroes_column))
data = dict(heroes_zipped)

filepath='./heroes_csv'

df = pd.DataFrame(data)
df.to_csv(filepath,index=0)
heroes_csv = pd.read_csv(filepath, index_col='level')

print(heroes_csv)

heroes_csv.plot( color = ['green','blue','red'])
plt.ylabel('Heroes`s Damage')
plt.show()