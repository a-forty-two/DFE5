import flask
from flask import Flask
app = Flask("myapp")

@app.route('/')
def helloworld():
    return 'hello world'

@app.route('/home')
def sendPage():
    return '<input type="button">Click Me</input><br/><br/><p>Good luck with that button working!</p>'

@app.route('/sum/<x>/<y>')
def findsum(x,y):
    x= int(x)
    y = int(y)
    response = { "sum" : x+y }
    return response


app.run(host='0.0.0.0')
