from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )

@application.route("/podowon") # html document를 response 하는 방법
def toy_pjt():
    return render_template('intro.html') # response hn path

@application.route("/intro") # html document를 response 하는 방법
def intro():
    return render_template('intro.html') # response hn path

@application.route("/member") # html document를 response 하는 방법
def member():
    return render_template('member.html') # response hn path

@application.route("/notice") # html document를 response 하는 방법
def notice():
    return render_template('notice.html') # response hn path

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True) 