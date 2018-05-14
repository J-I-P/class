from urllib.parse import urlparse
url = 'http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1'
o = urlparse(url)
print(o)

print("scheme={}".format(o.scheme))
print("netloc={}".format(o.netloc))
print("port={}".format(o.port))
print("path={}".format(o.path))
print("query={}".format(o.query))