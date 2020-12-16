import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
import pandas as pd


# creating the training and test data sets
df = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_1 = pd.read_csv('data/Merged_RaceData_2005-2017.csv')  # training data
df_2 = pd.read_csv('data/Merged_RaceData_2018-2019.csv')  # test data

X = df[['Odds', 'final_place']]
X = X.fillna(0)
X.values.reshape(-1, 1)

# X_train  is a 2d array with [Odds, final_place] from the training data
X_train = df_1[['Odds', 'final_place']]
X_train = X_train.fillna(0)
X_train.values.reshape(-1, 1)

# y_train  is a list of the final_place, 1st, 2nd, 3rd, etc from the training data
y_train = df_1['final_place']
# final_place_1 = df_1['final_place'].max()
# y_train = list(range(0, final_place_1 + 1))

# X_test  is a 2d array with [Odds, final_place] from the testing data
X_test = df_2[['Odds', 'final_place']]
X_test = X_test.fillna(0)
X_test.values.reshape(-1, 1)

# y_test  is a list of the final_place, 1st, 2nd, 3rd, etc from the testing data
y_test = df_2['final_place']
# # print(X.Odds.unique())
# print("X: " + str(X.size) + '\n' +
#       "X_train: " + str(X_train.size) + '\n' +
#       "y_train: " + str(y_train.size) + '\n' +
#       "X_test: " + str(X_test.size) + '\n' +
#       "y_test: " + str(y_test.size) + '\n')
# # print(y_train)

models = {'Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor}

app = dash.Dash()

app.layout = html.Div([
    html.P("Select Model:"),
    dcc.Dropdown(
        id='model-name',
        options=[{'label': x, 'value': x}
                 for x in models],
        value='Regression',
        clearable=False
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"),
    [Input('model-name', "value")])
def train_and_display(name):
    model = models[name]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure([
        go.Scatter(x=X_train.squeeze(), y=y_train,
                   name='train', mode='markers'),
        go.Scatter(x=X_test.squeeze(), y=y_test,
                   name='test', mode='markers'),
        go.Scatter(x=x_range, y=y_range,
                   name='prediction')
    ])

    return fig

if __name__ == '__main__':
    app.run_server()