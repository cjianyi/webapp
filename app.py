from flask import Flask, render_template
from flaskext.mysql import MySQL
from database import connect, createTable


app = Flask(__name__)

@app.route("/")
def main():
    try: 
        createTable()
        return render_template('index.html')
    except Exception:
        return render_template('index.html')


@app.route('/search')
def search():
    try:
        mysql = connect()
        conn = mysql.connect()
        cur = conn.cursor()
        #Executing SQL Statements
        cur.execute(''' SELECT count(*) FROM patients''')
        conn.commit()
        cur.close()
        return render_template('search.html')
    except:
        return render_template('error.html')

if __name__ == '__main__':
    app.run()