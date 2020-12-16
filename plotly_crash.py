import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/Merged_RaceData_2005-2017.csv')

# ser_of_bool = df['final_place'] == 1  # list of booleans winner of each race
# print(df[ser_of_bool])  # prints the rows with true aka winners
# print(df[df['Age'] > 30])  # same as above row

df = pd.DataFrame(data=df)
df2 = df[['year', 'race', 'Odds']]
favorites_list = []
# longerversion of line below
# bool_series = df['year'] == 2005
# result_df = df[bool_series]
# result_df2 = df2[df2['year']==2005]
# result_df2 = result_df2[result_df2['race'] == 'Kentucky Derby']

#multiple conditions
# for year in range(1,21)
df2 = df2[(df2['year']==2005) & (df2['race'] == 'Kentucky Derby')]
favorite = df2['Odds'].min()


print(df2)

# print(df.columns)  # list of column names

# data = [go.Bar(x=df[''])]



# pie donut chart code below
# labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
# values = [4500, 2500, 1053, 500]
#
# # Use `hole` to create a donut-like pie chart
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
# fig.show()
