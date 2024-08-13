from flask import Flask, render_template, request, url_for, flash, redirect
from flask import session as sessions
from flask_session import Session as Sessions
from flask_login import LoginManager, login_user, login_required, logout_user
from sqlalchemy import create_engine, select, text, or_
from models import Base, User, UserMixin
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask_bootstrap import Bootstrap5
from forms import RegistrationForm, LoginForm, Logout
from werkzeug.security import generate_password_hash, check_password_hash
import os

db_path = 'sqlite:///todo.db'

engine = create_engine(db_path, echo=True)

try:

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    db = Session()
    user = User( id = User.id, email="minoumazeg@gmail.com", password=generate_password_hash('123456789'),
                firstname="Amine", lastname="Mazeg", username="user", dateAdd=datetime.now())
    db.add(user)
    db.commit()

except Exception as ex:
    print(ex)

app = Flask(__name__)

# initialize sessions
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Sessions(app)

# iinitialize csrf key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# initialize bootstrap
bootstrap = Bootstrap5(app)

# initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def user_loader(user_id):
    user =  db.execute(select(User).where(User.id == user_id)).first()
    for row in user:
        return row


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('layout.html')

@app.route("/login", methods=["POST", "GET"])
def login():

    # initialize the form
    loginForm = LoginForm()

    if request.method == "POST":
        # check if submit button has been pressed
        if loginForm.validate_on_submit:
            email = loginForm.email.data
            password = loginForm.password.data

            user = db.execute(select(User).where(or_(User.email == email, User.username == email))).first()  
            for row in user:
                print(row)
                if check_password_hash(row.password, password):
                    login_user(row)
                    return redirect(url_for('dashboard'))
                else:
                    flash('Password is incorrect')


    return render_template('login.html', form=loginForm)


@app.route("/register", methods=["GET", "POST"])
def register():

    sessions.clear()

    # initialise form
    registrationForm = RegistrationForm()

    # check if method is post
    if request.method == 'POST':
        # When user submits the form
        if registrationForm.validate_on_submit:
            # get data from form
            email = registrationForm.email.data
            password = registrationForm.password.data
            username = registrationForm.username.data
            confirm = registrationForm.confirm.data
            firstName = registrationForm.firstName.data
            lastName = registrationForm.lastName.data

            # hash password and password confirmation
            hachedPassword = generate_password_hash(password)

            # check if email is already registred
            getUserEmail = db.execute(
                select(User.email).where(User.email == email)).first()
            if getUserEmail:
                for UserEmail in getUserEmail:
                    if UserEmail == email:
                        flash('This email is already used')

            # check if username is already used
            getUsername = db.execute(select(User.username).where(
                User.username == username)).first()
            if getUsername:
                for Username in getUsername:
                    if Username == username:
                        flash('The username is already used')

            if not check_password_hash(hachedPassword, confirm):
                flash('passwords do not match')

            try:
                user = User(email=email, password=hachedPassword, firstname=firstName,
                            lastname=lastName, username=username, dateAdd=datetime.now())
                db.add(user)
                db.commit()
                return redirect(url_for('login'))
                # ToDo // return to login page or connect the user
            except Exception as e:
                db.rollback()
                print(e)

    return render_template('register.html', form=registrationForm)


@app.route('/dashboard', methods=["POST", "GET"])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)