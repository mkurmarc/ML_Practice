import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

df = pd.read_csv('data/Merged_RaceData_2005-2017.csv')
df = pd.DataFrame(data=df)
# print(df)

# donut category labels
last_finish_place = df['final_place'].max()
donut_labels = list(range(1, last_finish_place + 1))
# donut values



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
            dcc.Graph(id='example_2',
              figure={'data':[
                {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
                {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':'SF'}
              ],
                        'layout':{
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor':colors['background'],
                            'font':{'color':colors['text']},
                            'title':'2ND PLOTS!'
                        }}),
            dcc.Graph(id='scatterplot',
                figure= {'data':[
                    go.Scatter(
                    x=random_x,
                    y=random_y,
                    mode='markers'
                    )],
                            'layout': go.Layout(title='My Scatterplot')}),
            dcc.Graph(id='donut chart',
                figure= {'data':[
                    go.Pie(
                    labels= donut_labels,
                    values=sss,
                        hole=.3
                    )],
                            'layout': go.Layout(title='My Scatterplot')})

], style={'backgroundColor':colors['background']}
)




if __name__ == '__main__':
    app.run_server()