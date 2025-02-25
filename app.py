from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['UPLOAD_PATH'] = 'static/images'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['studentid']
        password = request.form['password']

        if username == "anurej" and password == "1234":
            return redirect(url_for('home'))
        
        else:
            flash("Invalid Username or Password", "error")

    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/eligibility')
def eligibility():
    return render_template('eligi.html')

@app.route('/eligibility/upload', methods=['POST'])
def upload():
    file = request.files['myfile']
    file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
    return "file uploaded"

if __name__ == '__main__':
    app.run(debug=True)
