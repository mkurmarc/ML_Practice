import plotly
import plotly.express as px
from sklearn import linear_model
import numpy as np
import pandas as pd

raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)

df_all = df_all[['Odds', 'lowTemp', 'highTemp', 'precipitation', 'final_place', 'PP']]
# below creates 2 new new columns
df_all['averageTemp'] = df_all['lowTemp'] + df_all['highTemp']
df_all['averageTemp'] = df_all['averageTemp'] / 2
df_all['top_3'] = df_all['final_place'] < 4
print(df_all)

# removes 2 columns
df_all = df_all.drop(['lowTemp','highTemp'], axis=1)

# fig3 = px.scatter_matrix(df_all, dimensions=['Odds', 'averageTemp', 'precipitation', 'final_place'],
#                          color='trackCondition')
fig3 = px.scatter_matrix(df_all,
                         dimensions=['Odds', 'averageTemp', 'precipitation', 'PP'],
                         color='final_place',
                         labels={'averageTemp':'AvgTemp', 'precipitation':'Rain',
                                 'final_place':'Final Place', 'trackCondition':'Track Condition',
                                 'top_3':'Top 3 Finish', 'weather':'Weather Description',
                                 'attendance':'Attendance', 'PP':'P.Position', 'Odds':'Odds'},
                         opacity=0.4,
                         title='Data Features Scatter Matrix')

fig3.write_html('D:/Personal/WGU/Capstone_Docs/predict_visual3.html', include_plotlyjs='cdn')
