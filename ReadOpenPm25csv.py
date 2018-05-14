
import pandas as pd

#data = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")
data=pd.read_csv("http://opendata.epa.gov.tw/ws/Data/AQI/?$format=csv")

print(data.head(12))