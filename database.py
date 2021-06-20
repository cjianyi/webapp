from flaskext.mysql import MySQL
from flask import Flask, render_template



def connect():
    """
    Connect to the database and create table
    """
    app = Flask(__name__)
        
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'patients'
    mysql = MySQL(app)
    return mysql



def createTable():
    """
    Create table patients
    """
    app = Flask(__name__)
        
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'patients'
    mysql = MySQL(app)


    conn = mysql.connect()
    cur = conn.cursor()
    #Executing SQL Statements
    cur.execute(''' CREATE TABLE patients (id INTEGER, name VARCHAR(255)
    ''')
    conn.commit()
    cur.close()