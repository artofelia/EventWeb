import urllib2, json
import random

def findEvents(interests, time, place):
    url="http://api.eventful.com/json/events/search?"
    app_key = "FV8xFzGKxmWvqtgC"
    all = []
    random.shuffle(interests)
    interests = [interests[0]]
    for interest in interests:
        print interest
        url = url + "q=" + interest.replace(" ", "%20") + "&t=" + time + "&l=" + place + "&app_key=" + app_key
        request = urllib2.urlopen(url)
        result = request.read()
        d = json.loads(result)
        print d
        ret_ev = d['events']['event']
        ct = 0
        for item in ret_ev:
            print item
            ev = []
            ev.append(item['description'])
            ev.append(item['venue_url'])
            ev.append(item['city_name'] + ', ' + item['country_name'])
            ev.append(item['start_time'])
            all.append(ev)
            ct = ct + 1
            if ct > 3:
                break
        
    
    return (interests[0], all)

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
