#Task 1 of Week 1
#A simple hello-world at http://127.0.0.1:5000/ that displays a simple string like "Hello World - Shreya"
#Code for the task:

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World-Shreya"

if __name__ == "__main__":
    app.run()
