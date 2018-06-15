#Task5 of Week 1
#Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)

from flask import Flask
app = Flask(__name__)

from flask import abort, redirect, url_for


@app.route('/robots.txt')
def errcode():
    return redirect(url_for('myerror'))

@app.route('/error')
def myerror():
    abort(403)


if __name__ == "__main__":
      app.run()
