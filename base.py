from flask import Flask, render_template, url_for, request
import psycopg2
import db_center

dbname="postgres"

app = Flask(__name__)

connect = psycopg2.connect(
    host = hostname,
    database = dbname,
    user = username,
    port = port_id,
    password = pwd, )

cur = connect.cursor()

posts = [
    {
        
    }
]

@app.route("/")
@app.route("/home")
def home():
    cur.execute("SELECT * from spisok")
    rows = cur.fetchall()
    return render_template('home.html', rows = rows)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)