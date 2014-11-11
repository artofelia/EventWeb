import random
from pymongo import Connection

conn = Connection()

db = conn['1247']


def restart():
    db.usertable.drop()
    tdic = {'username': 'testing', 'password':'testing', 'intrests':['testing'],
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
    nu = {'username': usernamei, 'password':passwordi, 'intrests':[],
          'friends':[]}
    db.usertable.save(nu)
    return True

def updateUser(usernamei, passwordi, passwordn):
    if validate (usernamei, passwordi):
        db.usertable.update ({'username':usernamei, 'password':passwordi}, {"$set": {'username': usernamei, 'password':passwordn}})
        return True
    return False

def updateIntrest(usernamei, intresti):
    if validateFriend(usernamei):
        db.usertable.update({'username':usernamei},
							{"$addToSet": {'intrests': intresti}})
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

def getIntrests(usernamei):
    if validateFriend(usernamei):
        cres = db.usertable.find({'username': usernamei})
        res = [r['intrests'] for r in cres]
        return res
    return False
	
def getFriends(usernamei):
    if validateFriend(usernamei):
        cres = db.usertable.find({'username': usernamei})
        res = [r['friends'] for r in cres]
        return res
    return False
    
