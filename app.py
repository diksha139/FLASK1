from flask import Flask, render_template


app= Flask(__name__)

@app.route('/')
def firstFlask():
    return "Hello , this is my second flask program"

@app.route('/kartavya')
def display():
    return "Hi ....This is Kartavya"

@app.route('/index')

def first_webpage():
    name= "Aryan"
    return render_template('index.html',indexName=name)



app.run(debug=True)

