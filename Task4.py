#Task 4 of Week 1
#Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

from flask import Flask
app = Flask(__name__)
from flask import request

@app.route('/getcookies')
def get_cookie():
    name = request.cookies.get('name')
    age =request.cookies.get('age')
    return '<h1>Name: '+name+'</br>Age: '+age+'</h1>'


if __name__ == "__main__":
    app.run()
