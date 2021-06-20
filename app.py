from flask import Flask, render_template
from flaskext.mysql import MySQL


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
 

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()