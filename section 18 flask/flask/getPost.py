from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':

        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        # gender=request.form['gender']
        # skill=request.form['skills']
        # country=request.form['country']
        return f"name = {name} ,  email={email}, password={password}"
    else:
         
        return render_template('form.html') #with proper render_templete


if __name__=='__main__':
    app.run(debug=True)