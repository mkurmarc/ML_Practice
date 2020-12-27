import plotly
import plotly.express as px
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from dash.dependencies import Input, Output
import pandas as pd

df_all = pd.read_csv('data/Merged_RaceData_AllYears.csv')
raw = df_all

df_all = raw.fillna(0)
df_all = df_all.drop(['trackCondition', 'race_data_id',
                      'PP', 'Horse', 'Jockey', 'Trainer', 'Win', 'Place',
                      'Show', 'weather', 'year', 'race'], axis=1)

X = df_all[['Odds', 'highTemp', 'lowTemp', 'precipitation']]
Y = df_all['final_place']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2) # 20% to test set

model = linear_model.LinearRegression()
model.fit(X_train, Y_train)  # builds model using train data

Y_pred = model.predict(X_test)  # use test data and input into model to predict, assigns to Y_pred
Y_pred = np.ndarray.round(Y_pred, decimals=0)

fig1 = px.scatter(x=Y_test, y=Y_pred, labels={'x':'actual', 'y':'prediction'},
                  title='Horse Finish Place: Prediction vs. Actual')
fig1.add_shape(
    type="line", line=dict(dash='dash'),
    x0=Y_test.min(), y0=Y_test.min(),
    x1=Y_test.max(), y1=Y_test.max()
)

# plotly.offline.plot(fig1, filename='D:/Personal/WGU/Capstone_Docs/predict_graph.html')
fig1.write_html('D:/Personal/WGU/Capstone_Docs/predict_visual.html', include_plotlyjs='cdn')