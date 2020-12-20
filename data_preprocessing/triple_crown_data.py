import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

df_all = pd.read_csv('data/Merged_RaceData_AllYears.csv')
raw = df_all

df_all = raw.fillna(0)
df_all = df_all.drop(['attendance', 'trackCondition', 'race_data_id',
                      'PP', 'Horse', 'Jockey', 'Trainer', 'Win', 'Place',
                      'Show', 'weather', 'year', 'race'], axis=1)
# print(df_all.shape)
# print(df_all.head())
# print(df_all.dtypes)

X = df_all[['Odds', 'highTemp', 'lowTemp', 'precipitation']]
Y = df_all['final_place']
# print(X.shape)
# print(Y.shape)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2) # 20% to test set
# print(X_train.shape)
# print(Y_train.shape)
# print(X_test.shape)
# print(Y_test.shape)
model = linear_model.LinearRegression()
model.fit(X_train, Y_train)  # builds model using train data

Y_pred = model.predict(X_test)  # use test data and input into model to predict, assigns to Y_pred
Y_pred = np.ndarray.round(Y_pred, decimals=0)
print(Y_pred)
# Y_pred is the predicted value, while Y_test is the actual value

## print models performance
print('Coefficients: ', model.coef_)
print('Intercept: ', model.intercept_)
print('Mean squared error (MSE): %.2f'
      % mean_squared_error(Y_test, Y_pred))
print('Coefficient of determination (R^2): %.2f'
      % r2_score(Y_test, Y_pred))

# print(Y_test)
# print(Y_pred)


# graph scatter plot
sns.scatterplot(x=Y_test, y=Y_pred, alpha=0.5)


#?# which horse has the lowest odds of winning any race
# longest_odds = df_all[df_all['Odds'] == df_all['Odds'].max()]
# print(longest_odds)  # gives row
# print(longest_odds['Horse'])   # gives horse the longest odds from that row


#?# horses that finished top 3 in every race
# top_3 = df_all[df_all['final_place'] < 4]
# print(top_3)  # answer
# print(top_3['Horse'])  # gives only horse names


#?# which horse in Kentucky Derby has the lowest odds
# KD = df_all.groupby('race').get_group('Kentucky Derby')
# KD_longOdds = KD[KD['Odds'] == KD['Odds'].max()]
# print(KD_longOdds)

