from flask import Flask, request, render_template, redirect
import sys
from modules.dbHanddle import *
from modules.dbHandlePool import *

application = Flask( __name__ )

# filters
@application.template_filter('strftime')
def strftime_filter(dt):
    return dt.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')

# flask
@application.route("/")
def hello():
    return "Hello goorm!" # response


@application.route("/insertForm")
def insertForm():
    return render_template('insertForm.html') # response


@application.route("/insertResult")
def insertResult():
    n = request.args['myname']
    a = int(request.args['myage'])
    b = request.args['mybirth']
    return f"<h1> {insertData(n,a,b)} </h1>"


@application.route("/selectStudent")
def selectStudentRoute():
    result = selectStudentPool()
    return render_template('selectStudent.html',
                          result=result) # response

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True)