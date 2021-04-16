import urllib.request

# REST API (Representational State Transfer - Application Programmers Interface)
url = urllib.request.urlopen("https://www.reddit.com/r/todayilearned/top.json?limit=100")
text = url.read().decode()

destination = open("json_data.json", "w")
destination.write(text)
destination.close()
