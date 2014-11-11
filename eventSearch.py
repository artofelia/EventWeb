import urllib2, json

def findEvents(interest, time, place):
    url="http://api.eventful.com/json/events/search?"
    app_key = "FV8xFzGKxmWvqtgC"
    url = url + "q=" + interest.replace(" ", "%20") + "&t=" + time + "&l=" + place + "&app_key=" + app_key
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    return d

'''
queryWhat = "Dumb and Dumber To"
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
'''
#url = url + "&app_key=" + app_key
#request = urllib2.urlopen(url)
#result = request.read()
#d = json.loads(result)
#print d
#rlist = d['responseData']['results']
#for r in rlist:
    #print r
