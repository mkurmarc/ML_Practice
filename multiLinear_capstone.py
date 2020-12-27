import plotly
import plotly.express as px
from sklearn import linear_model
import numpy as np
import pandas as pd

raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)

df_all = df_all[['Odds', 'lowTemp', 'highTemp', 'precipitation', 'final_place',
                 'PP', 'trackCondition', 'weather']]
# below creates new averageTemp feature or column
df_all['averageTemp'] = df_all['lowTemp'] + df_all['highTemp']
df_all['averageTemp'] = df_all['averageTemp'] / 2
# below replaces sloppy and muddy with other
df_all['trackCondition'].replace(to_replace='Muddy', value='Sloppy', inplace=True)
df_all['weather'].replace(to_replace='Showery', value='Rainy', inplace=True)
df_all['weather'].replace(to_replace='Foggy', value='Cloudy', inplace=True)

fig = px.scatter(df_all,
                 x='final_place',
                 y='Odds',
                 facet_col='trackCondition',
                 color='weather',
                 trendline='ols')

fig.write_html('D:/Personal/WGU/Capstone_Docs/multiLinear.html', include_plotlyjs='cdn')

