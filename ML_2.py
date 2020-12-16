import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import plotly.express as px

# creating the training and test data sets
# df = pd.read_csv('data/Merged_RaceData_AllYears.csv')
# df_1 = pd.read_csv('data/Merged_RaceData_2005-2017.csv')  # training data
# df_2 = pd.read_csv('data/Merged_RaceData_2018-2019.csv')  # test data

df = pd.DataFrame(np.random.randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

filtered_rows = df[df['W'] > 0]  # filter rows where category W is >0

filtered_rows2 = df[df['Z'] < 0]
# df[df[['W'] > 0]][['Y', 'X']]  # produces same as filtered_rows2 above but with showing Y and Z columns

two_conditions = df[(df['Z'] < 0) & (df['Y']) > 1]  # multiple conditions use & for AND, | for OR

reset_index = df.reset_index()  # resets index into actual column, inplace=True to affect the df permanently

newind = 'CA NY WY OR CO'.split()  # splits on spaces. This creates a quick list
df['States'] = newind  # creates new column called States using the 5 values. Works cuz # of values equals # of rows in dataframe

df.set_index('States')  # changes the State column to be the index, overwrites old index. inplace=True to affect the df permanently



# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))  # creates a list of tuple pairs
hier_index = pd.MultiIndex.from_tuples(hier_index)

df2 = pd.DataFrame(np.random.randn(6,2), hier_index, ['A','B'])  # df with multilevel index
df2.index.names = ['Groups', 'Num']  # adds names to the index levels, group being the outer most index

# df.loc('G1')  # locates rows in index G1
locate_cell = df2.loc['G1'].loc[2]['B']
df2 = df2.xs(1, level='Num')  # another way to locate rows with multi-indexes. 1 is index# and level is the name of the index



### missing data
d = {'A':[1,2,np.nan],'B':[5, np.nan, np.nan], 'C':[1,2,3]}  # A,B,C are columns. items in [] are the values
df3 = pd.DataFrame(d)
df3.dropna(axis=1, thresh=2)  # drops any columns with NaN in it. thresh is how many NaNs to look for.

# df3.fillna(value='FILL VALUE', inplace=True)  # replaces NaN with FILL VALUE

df3['A'].fillna(value=df3['A'].mean(), inplace=True)


### Groupby
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df4 = pd.DataFrame(data)
byComp = df4.groupby('Company')
# byComp.mean()  # mean/avg of the values in each group
# byComp.sum()  # sum of the values in each group
# byComp.std()  # standard deviation
# byComp.sum().loc['FB']  # access by index
# below - outputs same as commented out lines above
sum_byComp = df4.groupby('Company').sum().loc['FB']
# print(sum_byComp)

# print(df4.groupby('Company').describe())  # gives analysis of data
# print(df4.groupby('Company').describe().transpose()['FB'])  # analysis of specific category
# print(df4)

### SQL type merging
# pd.merge(df2, df3, how='inner', on=['key1', 'key2'])  # can change how to: outer, etc

### apply
# print(df4['Sales'].apply(lambda x: x*2))  # applies functions to column, lambda, define function, methods

### sort column
# print(df4.sort_values('Sales'))


## pivot table


#############

df_main = pd.read_csv('data/Merged_RaceData_2005-2017.csv')
df5 = df_main[['year', 'race', 'race_data_id']]

print(df5)