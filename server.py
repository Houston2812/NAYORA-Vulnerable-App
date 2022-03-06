import sqlite3
from traceback import print_tb
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_session import Session


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    
    return render_template('index.html')
  
@app.route("/login", methods=["GET"])
def get_login():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def post_login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if len(username) > 0:
        conn = get_db_connection()
        user = conn.execute(f'SELECT * FROM users where username = "{username}"').fetchall()
        conn.close()
        
        if len(user) > 0:
            if len(password) > 0:
                conn = get_db_connection()
                query = f'SELECT username FROM users where username = "{username}" and  password = "{password}"'
                print(query)
                validation = conn.execute(query).fetchone()
                conn.close()
                print(validation[0])
                if len(validation) > 0:
                    session["name"] = request.form.get("username")
                    return redirect("/home")
                else:
                    flash("Wrong password", "error")
            else:
                flash("Enter password", "error")
        else:
            flash("Wrong username", "error")
    else:
        flash("Enter username", "error")
    return render_template("login.html")

@app.route("/home")
def home():
    print(session.get("name"))
    if not session.get("name"):
        return redirect("/")
    return render_template("home.html", username=session.get("name"))

@app.route("/logout")
def logout():
    session["name"] = None 
    return redirect("/")

if __name__=="__main__":
   
    app.run(debug=True, host = 'localhost')
