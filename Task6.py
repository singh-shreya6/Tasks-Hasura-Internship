#Task 6 of Week 1
#Render an HTML page at http://127.0.0.1:5000/html

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/html')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

