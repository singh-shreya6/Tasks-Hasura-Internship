#Task 3 of Week 1
#Set a simple cookie at http://127.0.0.1:5000/setcookie with the following values: name=<your-first-name> and age=<your-age>

from flask import Flask
app = Flask(__name__)

from flask import make_response

@app.route('/setcookie')
def index():
    resp = make_response()
    resp.set_cookie('name',value= 'Shreya')
    resp.set_cookie('age',value='21')
    return resp

if __name__ == "__main__":
    app.run()
