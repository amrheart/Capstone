from flask import Flask
import sqlite3
from Python_DB import GetLastRow

app = Flask(__name__)

@app.route("/")
def hello_world():
    row = GetLastRow()
    new_string = """<p>
    Average Speed: {} f/s,
    Trip Time: {} seconds,
    Trip Distance: {} feet,
    Start Temperature: {} C,
    End Temperature: {} C
    </p>""".format(row[1],row[2],row[3],row[4],row[5])
    return new_string