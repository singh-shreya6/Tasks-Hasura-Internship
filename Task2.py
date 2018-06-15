#Task 2 of Week 1
#Add a route, for e.g. http://127.0.0.1:5000/authors, which:
#a)fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
#b)fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
#c)Respond with only a list of authors and the count of their posts (a newline for each author).

from flask import Flask, render_template
app = Flask(__name__)
import requests
import json

@app.route('/authors')
def authors():
        url1='https://jsonplaceholder.typicode.com/users'
        url2='https://jsonplaceholder.typicode.com/posts'
        r1=requests.get(url1)
        r2=requests.get(url2)
        data1=r1.json()
        data2=r2.json()
        return render_template('result.html',data1=data1,data2=data2)



if __name__ == "__main__":
    app.run(debug=True)
