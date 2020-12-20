import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

df_all = pd.read_csv('data/Merged_RaceData_AllYears.csv')
raw = df_all

df_all = raw.fillna(0)
df_all = df_all.drop(['attendance', 'trackCondition', 'race_data_id',
                      'PP', 'Horse', 'Jockey', 'Trainer', 'Win', 'Place',
                      'Show', 'weather', 'year', 'race'], axis=1)

# X = df_all['highTemp']
X = df_all[['final_place', 'Odds', 'highTemp', 'lowTemp', 'precipitation']]

X_train, X_test, Y_train, Y_test = train_test_split(X, X.final_place, test_size=0.2) # 20% to test set
print(X_train)
print(Y_train)
# Y_pred = model.predict(X_test)  # use test data and input into model to predict, assigns to Y_pred
# Y_pred = np.ndarray.round(Y_pred, decimals=0)
# Y_pred is the predicted value, while Y_test is the actual value

## print models performance
# print('Coefficients: ', model.coef_)
# print('Intercept: ', model.intercept_)
# print('Mean squared error (MSE): %.2f'
#       % mean_squared_error(Y_test, Y_pred))
# print('Coefficient of determination (R^2): %.2f'
#       % r2_score(Y_test, Y_pred))

# graph scatter plot
# sns.scatterplot(x=Y_test, y=Y_pred, alpha=0.5)

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
    model.fit(X_train, Y_train)

    # x_range = np.linspace(X.min(), X.max(), 100)
    # y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure([
        go.Scatter(x=X_train.squeeze(), y=Y_train,
                   name='train', mode='markers'),
        go.Scatter(x=X_test.squeeze(), y=Y_test,
                   name='test', mode='markers')
        # go.Scatter(x=x_range, y=y_range,
        #            name='prediction')
    ])

    return fig

if __name__ == '__main__':
    app.run_server()