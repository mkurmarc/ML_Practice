import dash
import dash_core_components as dcc
import dash_html_components as html
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np


app = dash.Dash()

df_all = pd.read_csv('data/Merged_RaceData_AllYears.csv')
raw = df_all

df_all = raw.fillna(0)
df_all = df_all.drop(['trackCondition', 'race_data_id',
                      'PP', 'Horse', 'Jockey', 'Trainer', 'Win', 'Place',
                      'Show', 'weather', 'year', 'race'], axis=1)

X = df_all[['Odds', 'highTemp', 'lowTemp', 'precipitation', 'attendance']]
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

# fig = px.scatter(
#
# )

colors = {'background':'#111111', 'text':'#7fdbff'}  #dictionary to organize colors used throughout layout
# colors['text'] # this calls the color of the text

app.layout = html.Div(children=[
            html.H1('Triple Crown Races Dashboard',style={'textAlign':'center',
                                                           'color':colors['text']}),
            html.Div('Race results from all three Triple Crown Races and the track conditions on each contest day. '
                     'Data starts in year 2005 through 2017. '),
            dcc.Graph(id='example',
              figure={'data':[
                {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
                {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':'SF'}
              ],

                        'layout':{
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor':colors['background'],
                            'font':{'color':colors['text']},
                            'title':'Bar Chart to show the place each betting favorite finished on race day. '
                        }}),
            # dcc.Graph(id='',
            #           figure=),
            dcc.Graph(id='predict_graph',
                      figure=fig1)


], style={'backgroundColor':colors['background']}
)



if __name__ == '__main__':
    app.run_server()