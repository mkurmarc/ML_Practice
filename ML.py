import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import plotly.express as px


df_train = pd.read_csv('data/Merged_RaceData_2005-2017.csv')
df_test = pd.read_csv('data/Merged_RaceData_2018-2019.csv')
# df = df[['highTemp', 'lowTemp', 'weather', 'trackCondition']]

# col = df.loc[:, "highTemp":"lowTemp"]
# df['meanTemp'] = col.mean(axis=1)
#
# avg_temp = df['meanTemp'].mean()  # split on the mean

# df1 = df[['highTemp', 'lowTemp']]
# df1 = df1.mean()
# df1 = df1[]
# print(df1)
# print(df)
# print(avg_temp)

################################

# ML Regression Dash
df_train = df_train[['Odds', 'final_place']]
# df_train = df_train[(df_train['Odds']>0)]


df_train = df_train[df_train['Odds'] > 0]
X_train = df_train.Odds.values[:, None]


# last_final_place = df_Train['final_place'].max()
# df_y = list(range(0, last_final_place + 1))
# X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.25)
#
print(X_train)

###############################
# OLS using plotly.express
# df = px.data.tips()
# fig = px.scatter(
#     df, x='total_bill', y='tip', opacity=0.65,
#     trendline='ols', trendline_color_override='darkblue'
# )
# fig.show()