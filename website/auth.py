from flask import Blueprint, render_template, request
auth  = Blueprint('auth', __name__)


@auth.route('/', methods = ['GET', 'POST'] )
def home():
    data = request.args.get("touch")
    print(data)
    
    return render_template("base.html")





@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signout')
def signout():
    return render_template('signout.html')


@auth.route('/player')
def player():
    return render_template('player.html')