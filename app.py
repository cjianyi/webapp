from flask import Flask, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'patients'
mysql = MySQL(app)

cursor = mysql.connection.cursor()
 
#Executing SQL Statements
cursor.execute(''' CREATE TABLE patients (id INTEGER, name VARCAHR(255), dob DATE) ''')
mysql.connection.commit()
cursor.close()
 

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()