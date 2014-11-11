import urllib2, json

app_key = "FV8xFzGKxmWvqtgC"
url="http://api.eventful.com/json/events/search?"

queryWhat = "Dumb and Dumber To"
queryWhen = "Today"
queryWhere = "NYC"

if queryWhat != None:
    url = url + "q=" + queryWhat
if queryWhen != None:
    url = url + "&t=" + queryWhen
if queryWhere != None:
    url = url + "&l=" + queryWhere

request = urllib2.urlopen(url)
result = request.read()
d = json.loads(result)
#print d
#rlist = d['responseData']['results']
#for r in rlist:
 #   print r
