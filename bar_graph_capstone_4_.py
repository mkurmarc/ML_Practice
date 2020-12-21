import plotly
import plotly.express as px
from sklearn import linear_model
import numpy as np
import pandas as pd

raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)

df_top3 = df_all[df_all['final_place'] < 4]
odds_col = df_top3['Odds']
final_col = df_top3['final_place']


print(top3_col)
print(df_odds)


