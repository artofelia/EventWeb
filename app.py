from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
import os
import base
import eventSearch

app = Flask(__name__)
corner = """
 
"""
@app.route('/')
def index():
    if 'username' in session:
        return render_template ("index.html", 
                                corner = escape(session['username']))
    else:
        return render_template ("index2.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if base.validate (request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            flash('You were successfully logged in')
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials"
            return render_template ("login.html", error = error)
    else:
        return render_template ("login.html", error = error)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    flash("You have logged out")
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if 'username' in session:
        flash("You are already logged in")
        return redirect(url_for('index'))
    elif request.method == 'POST':
        if base.addUser (request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            flash ("You have successfully registered")
            return redirect(url_for('index'))
        else:
            error = "That username is already taken"
            return  render_template ("register.html", error = error)
    else:
        return  render_template ("register.html", error = error)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    error = None
    if 'username' in session:
        if request.method == 'POST':
            if base.updateUser (escape(session['username']), request.form['password'], request.form ['newpassword']):
                flash ("You have successfully changed your settings")
                return redirect(url_for('index'))
            else:
                error = "You have entered the wrong password"
                return render_template ("settings.html", 
                                        corner = escape(session['username']), 
                                        error = error)
        else:
            return render_template ("settings.html", 
                                        corner = escape(session['username']), 
                                        error = error)
    else:
        return render_template ("error.html")

@app.route('/about')
def about():
    if 'username' in session:
        return render_template  ("page1.html",
                                 corner = escape(session['username']))
    else:
        return render_template ("page1.html",
                                 corner = None)

@app.route('/findEvents', methods=['GET', 'POST'])
def findEvents():
    error = None
    if 'username' in session:
        user = escape(session['username'])
        
        if request.method == 'POST':
            form_keys = request.form.keys()
            
            if ('where' in form_keys) and ('when' in form_keys):
                interests = base.getAggInterests(user)
                jsret = eventSearch.findEvents(interests, None, None)
                events = []
                for key in jsret.keys():
                    evobj = jsret[key]
                    ev[0] = evobj['title']
                    ev[1] = evobj['url']
                    ev[2] = evobj['where']
                    ev[3] = evobj['when']
                    events.add(ev)
                    
                return render_template ("pageEvent.html",
                                            corner = escape(session['username']),
                                            error = error,
                                            events = events)   
        else:
            return render_template ("pageEvent.html",
                                            corner = escape(session['username']),
                                            error = error,
                                            events = [])   
    else:
        return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    error = None
    if 'username' in session:
        user = escape(session['username'])
        
        if request.method == 'POST':
            form_keys = request.form.keys()
            
            if 'newInterest' in form_keys:
                print 'got add command'
                newInterest = request.form['newInterest']
                base.updateInterest(user, newInterest)
                
            if 'cinterest' in form_keys:
                print 'got remove command'
                rmInterest = request.form['cinterest']
                base.removeInterest(user, rmInterest)
               
            ###                   
            if 'newFriend' in form_keys:
                print 'got add command'
                newFriend = request.form['newFriend']
                if base.validateFriend(newFriend):
                    base.updateFriend(user, newFriend)
                else:
                    flash('Username Not Found!!!')
                    
            if 'cfriend' in form_keys:
                print 'got remove command'
                rmFriend = request.form['cfriend']
                res = base.removeFriend(user, rmFriend)
                
            interests = base.getInterests(user)[0]
            friends = base.getFriends(user)[0]
            return render_template ("pageProfile.html",
                                        corner = escape(session['username']),
                                        error = error,
                                        interests = interests,
                                        friends = friends)   
        else:
            interests = base.getInterests(user)[0]
            friends = base.getFriends(user)[0]
            return render_template ("pageProfile.html",
                                        corner = escape(session['username']),
                                        error = error,
                                        interests = interests,
                                        friends = friends)
    else:
        return redirect(url_for('login'))

@app.route('/reset')
def reset():
    base.restart()
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
# this is fake very fake oooh
app.secret_key = os.urandom(24)

if __name__ == "__main__":
    app.debug = True
    app.run(host = "127.0.0.1", port = 1247)
