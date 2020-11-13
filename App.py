from flask import Flask, render_template, url_for, redirect, request, session
import modules.user_module
import modules.user_auth_module
from modules import functions_module as fn

app = Flask(__name__)
app.secret_key = b'\xad\x9766-\xa8\x19-9\xacD{|\xcf/\x89'

@app.route('/')
def home():
    """ Main route """
    return render_template('Home.html')

@app.route('/signin', methods=['POST','GET'])
def signin():
    """ Sign-in route """
    if request.method == 'POST':
        #get username and password, then verify the user.
        is_logged_in = modules.user_auth_module.verify_login(request.form['username'],request.form['password'])
        
        if is_logged_in == True:
            #add username and is logged in variables to the session, then redirect to the dashboard.
            username = session['username'] = request.form['username']
            session['is_logged'] = True
            return redirect(url_for('dashboard', user=username))
        
        else:
            #print invalid entered credentials, and stay in the same page.
            error = 'Invalid username or password!'
            return render_template('SignIn.html', error=error)
    
    else:
        
        return render_template('SignIn.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    """ Sign-up route """
    if request.method == 'POST':
        #Store user entered information in a User object.
        user = modules.user_module.User
        user.username = request.form['username']
        user.password = request.form['password']
        user.email = request.form['email']
        user.role = 'user'
        rpass = request.form['rpass']

        if user.password == rpass:#Check matching passwords.
            #Register the user.
            is_registered = modules.user_auth_module.register_user(user)
            
            if is_registered == True:#If registered successfully.
                #redirect him to sign-in route.    
                return redirect(url_for('signin'))
            
            else:
                #if the username is already exists, alert user.
                username_error = 'Username exists, try another one.'
                return render_template('SignUp.html', username_error=username_error)
        else:

            pass_error = "Password mismatch!"
            return render_template("SignUp.html", pass_error=pass_error)

    else:

        return render_template('SignUp.html')


@app.route('/course_list')
def course_list():
    #omitted for now, trying to figure out what is this route usefull for.
    return render_template('CourseList.html')


@app.route('/language/<string:course>')
def language(course):
    """ language(A.K.A plans) route """
    
    if 'is_logged' in session:#if there is a logged in user
        #get his plans from the database.
        plan = fn.fetch_plan_info(course)
        #pass plans to 'LanguageCards.html'
        return render_template('LanguageCards.html', plan=plan)
    
    else:
        #else take him sign-in route.
        return render_template('SignIn.html')

@app.route('/connect')
def connect():
    """ Connect route """
    return render_template('Connect.html')

@app.route('/about')
def about():
    """ About route """
    return render_template('About.html')

@app.route('/dashboard/<string:user>')
def dashboard(user):
    """ dashboard route """
    #get user plans from database.
    user_plans = fn.get_user_plans(user)
    return render_template('CourseList.html',user_plans=user_plans)#pass them to 'CourseList.html'

@app.route('/start/<int:id>')
def start(id):
    """ Start route """
    #if the user is logged in
    if 'username' in session:
        
        #store his name
        username = session['username']
        #add the given plan to his list. Note, id = plan_id, based from the 'LanguageCards.html'.
        plan_selected = fn.select_plan(username, id)
        
        #if the plan successfully selected.
        if plan_selected != False:
            #take him to dashboard.    
            return redirect(url_for('dashboard',user=username))
        
        else:
            #handling error, take the user to error page, with an error code.
            return redirect(url_for('error',ecode="PSE_04_DC"))
    
    else:
        #if the user is not logged in, take him to sign in route.
        return redirect(url_for('signin'))


@app.route('/resources/<int:id>')
def resources(id):
    """ resources route """
    #get resources list for the given plan ID
    resource_list = fn.get_resources_list(id)
    #and send them to 'resource_list.html'
    return render_template('resource_list.html',resource_list=resource_list)

@app.route('/completed/<int:id>')
def completed(id):
    """ completed route """
    #get the user ID and store it.
    user_id = fn.get_user_id(session['username'])
    #if the given plan for a the given user is marked complete successfully.
    is_completed = fn.mark_plan_complete(id, user_id)
    
    if is_completed:
        #take him to his dashboard
        return redirect(url_for('dashboard',user=session['username']))
    
    else:
        
        return redirect(url_for('error',ecode="EMC_01_DC"))
    

@app.route('/error/<string:ecode>')
def error(ecode):
    """ error route """
    #take the coming error code and send an appropriate message.
    if ecode == "EMC_01_DC":

        msg = "Failed to mark a plan as complete.\nSend us a feedback."    
    
    elif ecode == "PSE_04_DC":
        
        msg = "Failed to select a plan.\nSend us a feedback."
    
    return render_template('error.html',msg=msg)

@app.route('/logout')
def logout():
    """ logout route """
    # remove the username from the session if it's there
    session.pop('username', None)
    session['is_logged'] = False
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)