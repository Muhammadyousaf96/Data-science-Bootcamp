from flask import Flask 

app=Flask(__name__)

@app.route('/')
def welcom():
    return "welcome to flask app"

@app.route('/index')
def index():
    return 'index page founded'

if __name__=='__main__':
    app.run(debug=True)