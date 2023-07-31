from flask import Flask, render_template, request 
from flask import redirect, url_for,session
from datetime import datetime
from insert_data import add_profile,add_message,get_data

application = Flask(__name__)
application.secret_key ="ab2a3a7f-d830-441b-bca3-6c4fe12e7774"



def get_time():
    return datetime.now().strftime("%d-%m-%y %H:%M:%S")

@application.route('/',methods = ['GET','POST'])
def Dash():
    if request.method == 'POST':
        text = request.form['textarea']
        add_message(text)

    return render_template("get_message.html", value=get_time(),data=get_data(3))

@application.route('/files')
def file_page():
    return render_template("file.html",value=get_time(),data=get_data(7))

@application.route('/login')
def Login():
    return render_template('login.html', Name="Login", msg=None)


@application.route('/Signup',methods = ['GET','POST'])
def Signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return add_profile(name,email,password)
    else:
        return render_template('Signup.html',msg=None)

if __name__ == "__main__":
    application.run(debug=True,host='0.0.0.0')
    print("Working")
