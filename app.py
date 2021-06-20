from flask import Flask, render_template
from flaskext.mysql import MySQL
from database import connect

    
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/search')
def search():
    mysql = connect()
    conn = mysql.connect()
    cur = conn.cursor()
    #Executing SQL Statements
    cur.execute(''' SELECT count(*) FROM patients''')
    conn.commit()
    cur.close()
    return render_template('search.html')

if __name__ == '__main__':
    app.run()