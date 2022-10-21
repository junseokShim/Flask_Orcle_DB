from flask import Flask, request, render_template, redirect
import sys
from modules.dbHandlePool import *

application = Flask( __name__ )

# filters
@application.template_filter('strftime')
def strftime_filter(dt):
    return dt.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')


# flask
@application.route("/")
def hello():
    return render_template("main.html") # response


@application.route("/insertMenu")
def insertMenu():
    return render_template('insertMenu.html') # response


@application.route("/insertResult")
def insertResult():
    # print(request.args)
    name = request.args['name']
    quantity = int(request.args['quantity'])
    days = request.args['days']
    
    # DB에 입력
    insertData(name,quantity,days)
    result = selectProductPool()
    print(result)
    return render_template('totalMenu.html',
                          result=result)


@application.route("/totalMenu")
def totalMenu():
    result = selectProductPool()
    return render_template('totalMenu.html',
                          result=result) # response


@application.route("/searchMenu")
def searchMenu():
    return render_template('searchMenu.html') # response

@application.route("/searchResult")
def searchResult():
    result = conditionalSelectProductPool(request.args['name'])
    print(result)
    return render_template('searchResult.html',
                            result=result)


# @application.route("/selectStudent")
# def selectStudentRoute():
#     result = selectStudentPool()
#     return render_template('selectStudent.html',
#                           result=result) # response

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True)