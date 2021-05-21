import pandas as pd
df = pd.read_csv("train.csv")
# print(df.head())
# print(df.shape)

import folium
from folium import plugins

arr = df[['Y', 'X']].values


m = folium.Map(location=[arr[0][0], arr[0][1]], zoom_start=10)
m.add_child(plugins.HeatMap(arr[:50000], radius=10))
m.save('abcd.html')
