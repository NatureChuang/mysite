import folium

kh_gps = (22.6273, 120.3014)
url = "https://data.kcg.gov.tw/dataset/449e45d9-dead-4873-95a9-cc34dabbb3af/resource/fe3f93da-9673-4f7b-859c-9017d793f798/download/110.8.20.csv"
import pandas as pd
df = pd.read_csv(url)
df.head()
m = folium.Map(location=kh_gps, zoom_start=16)
m.save("docs/index.html")