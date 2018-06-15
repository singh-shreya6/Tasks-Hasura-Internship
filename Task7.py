#Task 7 of week 1
#A text box at http://127.0.0.1:5000/input which sends the data as POST to any endpoint of your choice.

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/input')
def my_form():
    return render_template('inputname.html')

@app.route('/input',methods = ['POST'])
def input():
   if request.method == 'POST':
      name = request.form['name']
      print(name)
   return '<h1>'+name+'<h1>'

if __name__ == '__main__':
    app.run(debug=True)
