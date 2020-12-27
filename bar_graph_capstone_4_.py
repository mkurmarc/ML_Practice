import plotly
import plotly.express as px
from sklearn import linear_model
import numpy as np
import pandas as pd

raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)
df_all['Odds_Mean'] = df_all['Odds'].mean()
df_all['trackCondition'].replace(to_replace='Muddy', value='Sloppy', inplace=True)

# df_top3 = df_all[df_all['final_place'] < 4]
X = df_all['Odds']
Y = df_all['Odds']

# sloppy_fil = df_top3[(df_top3['trackCondition'] == 'Sloppy')]


# fig_bar = px.bar(df_top3, x='trackCondition', y='Odds_Mean',
#                  title='Average Odds of Top 3 Based on Track Conditions'
#                  )

fig_histogram = px.histogram(df_all, x=X, color='trackCondition',
                 title='Average Odds of Top 3 Based on Track Conditions'
                 )

# fig_bar.write_html('D:/Personal/WGU/Capstone_Docs/visual_bar.html', include_plotlyjs='cdn')

fig_histogram.write_html('D:/Personal/WGU/Capstone_Docs/visual_histogram.html', include_plotlyjs='cdn')
