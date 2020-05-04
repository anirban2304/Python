from flask import Flask, render_template, request
import pyodbc
from sqlalchemy import create_engine
import urllib
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

server = 'python-project.database.windows.net'
database = 'height_data'
username = 'admin-python'
password = 'Kolkata@23'
driver= '{ODBC Driver 17 for SQL Server}'

params = urllib.parse.quote_plus\
    (r'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str,echo=True)

print('connection is ok')
print(engine_azure.table_names())

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "email_height"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        print(email, height)
        data = Data(email, height)
        db.session.add(data)
        db.session.commit()
        average_height = db.session.query(func.avg(Data.height)).scalar()
        average_height = round(average_height, 2)
        print(average_height)
        return render_template("success.html", avg_height = str(average_height))

if __name__ == '__main__':
    app.debug = True
    app.run()