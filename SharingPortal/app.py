from flask import Flask, render_template, request
from flask import redirect, url_for

application = Flask(__name__)

@application.route('/')
def home():
    return render_template("home.html")

@application.route('/files')
def file_page():
    return render_template("file.html")



if __name__ == "__main__":
    application.run(debug=True)