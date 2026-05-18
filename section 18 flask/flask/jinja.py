from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcom():
    return "welcome to flask app"

@app.route('/success/<int:score>')
def success(score):
    res=" "
    if score>=50:
        res="pass"
    else:
        res="Fail"
    return render_template('result.html',results=res)        

if __name__=='__main__':
    app.run(debug=True)