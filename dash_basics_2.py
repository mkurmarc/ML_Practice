# part 2
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

# creating Data
df = pd.read_csv('data/Merged_RaceData_2005-2017.csv')
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# this is the layout used when using plotly
app.layout = html.Div([dcc.Graph(id='scatterplot',
                                figure= {'data':[
                                        go.Scatter(
                                        x=random_x,
                                        y=random_y,
                                        mode='markers'
                                        )],
                                'layout': go.Layout(title='My Scatterplot')}
)])



if __name__ == '__main__':
    app.run_server()