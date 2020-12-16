import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

colors = {'background':'#111111', 'text':'#7fdbff'}  #dictionary to organize colors used throughout layout
# colors['text'] # this calls the color of the text

app.layout = html.Div(children=[
            html.H1('Triple Crown Races Dashboard', style={'textAlign':'center',
                                                           'color':colors['text']}),
            dcc.Graph(id='example',
              figure={'data':[
                {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
                {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':'SF'}
              ],
                        'layout':{
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor':colors['background'],
                            'font':{'color':colors['text']},
                            'title':'BAR PLOTS!'
                        }})
], style={'backgroundColor':colors['background']}
)




if __name__ == '__main__':
    app.run_server()