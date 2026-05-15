from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def welcom():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html') #with proper render_templete

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)