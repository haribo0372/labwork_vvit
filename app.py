import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="123456",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "" or password == "":
        return render_template('login.html' , empty_credentials=True)
    else:
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        if len(records) == 0:
            return render_template('login.html' , not_registered=True)
        else:
            return render_template('account.html', full_name=records[0][1]) + render_template('account.html', login=records[0][2]) + render_template('account.html', password=records[0][3])

if __name__ == "__main__" :
    app.run(debug=True)