import random
from pymongo import Connection

conn = Connection()

db = conn['1247']


def restart():
    db.usertable.drop()
    tdic = {'username': 'testing', 'password':'testing', 'interests':['testing'],
            'friends':['testing']}
    db.usertable.insert(tdic)   

def printData():
    cres = db.usertable.find()
    #{}, {'_id':False})
    #print cres
    #res = [r
    for r in cres:
        print r

def validate(usernamei, passwordi):
    cres = db.usertable.find({'username': usernamei,'password':passwordi})
    res = [r for r in cres]  
    if len(res)>0:
        return True
    return False

def validateFriend(usernamei):
    cres = db.usertable.find({'username': usernamei})
    res = [r for r in cres]  
    if len(res)>0:
        return True
    return False

def addUser(usernamei, passwordi):
    cres = db.usertable.find({'username':usernamei})
    res = [r for r in cres]
    print res
    if len(res)>0:
        return False
    nu = {'username': usernamei, 'password':passwordi, 'interests':[],
          'friends':[]}
    db.usertable.save(nu)
    return True

def updateUser(usernamei, passwordi, passwordn):
    if validate (usernamei, passwordi):
        db.usertable.update ({'username':usernamei, 'password':passwordi}, {"$set": {'username': usernamei, 'password':passwordn}})
        return True
    return False

def updateInterest(usernamei, interesti):
    if validateFriend(usernamei):
        db.usertable.update({'username':usernamei},
							{"$addToSet": {'interests': interesti}})
        return True
    return False

def updateFriend(usernamei, friendi):
    if validateFriend(usernamei):
        if validateFriend(friendi):
            db.usertable.update({'username':usernamei},
                            {"$addToSet": {'friends': friendi}})
            return True
        return False
    return False

def getInterests(usernamei):
    if validateFriend(usernamei):
        cres = db.usertable.find({'username': usernamei})
        res = [r['interests'] for r in cres]
        return res
    return False
	
def getFriends(usernamei):
    if validateFriend(usernamei):
        cres = db.usertable.find({'username': usernamei})
        res = [r['friends'] for r in cres]
        return res
    return False
    
def removeInterest(usernamei, interesti):
    if validateFriend(usernamei):
        db.usertable.update({'username': usernamei}, {"$pull": {'interests':interesti}})
        return True
    return False
	
def removeFriend(usernamei, friendi):
    if validateFriend(usernamei):
        db.usertable.update({'username': usernamei}, {"$pull": {'friends':friendi}})
        return True
    return False
    
def getAggInterests(usernamei):
    if validateFriend(usernamei):
        myint = getInterests(usernamei)[0]
        allint = myint
        
        frs = getFriends(usernamei)[0]
        for fr in frs:
            nint = getInterests(fr)[0]
            allint = allint+nint
        return allint
        
    return False

def getAllUsers():
    users = []
    for user in db.usertable.find({},{'username':1}):
        users.append(user['username'])
        print "USER: " + user['username']
    return users
