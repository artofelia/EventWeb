import urllib2, json

app_key = "FV8xFzGKxmWvqtgC"
url="http://api.eventful.com/json/events/search?"

queryWhat = "Dumb%20and%20Dumber%20To"
queryWhen = "Today"
queryWhere = None#"NYC"
andNeeded = True

if queryWhat != None:
    url = url + "q=" + queryWhat
#if andNeeded:
#url = url + "q=" + queryWhat
        
if queryWhen != None:
    url = url + "&t=" + queryWhen
if queryWhere != None:
    url = url + "&l=" + queryWhere

url = url + "&app_key=" + app_key
request = urllib2.urlopen(url)
result = request.read()
d = json.loads(result)
print d
rlist = d['responseData']['results']
#for r in rlist:
    #print r
