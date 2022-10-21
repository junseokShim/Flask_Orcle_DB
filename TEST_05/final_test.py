from flask import Flask, request, render_template, redirect
import sys
from modules.dbHandlePool import *

application = Flask( __name__ )

@application.route("/") # html document를 response 하는 방법
def main_page():
    return render_template('main.html') # response hn path

@application.route("/writing") # html document를 response 하는 방법
def writing_page():
    return render_template('writing.html') # response hn path

@application.route("/check") # html document를 response 하는 방법
def check_page():
    result = selectProductPool()
    print(result)
    return render_template('check.html',
                          result=result) # response hn path

@application.route("/insertResult")
def insertResult():
    # print(request.args)
    name = request.args['name']
    title = request.args['title']
    contents = request.args['contents']
    
    # DB에 입력
    insertData(name,title,contents)
    result = selectProductPool()
    return render_template('check.html',
                          result=result)


@application.route("/delete")
def delete():
    return render_template('delete.html')

@application.route("/deleteResult")
def deleteResult():
    # print(request.args)
    name = request.args['name']
    
    # DB에 반영
    deleteData(name)
    result = selectProductPool()
    return render_template('searchResult.html',
                          result=result)

@application.route("/searchMenu")
def searchMenu():
    return render_template('searchMenu.html') # response

@application.route("/searchResult")
def searchResult():
    result = conditionalSelectProductPool(request.args['name'])
    print(result)
    return render_template('searchResult.html',
                            result=result)

@application.route("/update")
def update():
    return render_template('update.html')


@application.route("/updateResult")
def updateResult():
        # print(request.args)
    name = request.args['name']
    to_name = request.args['to_name']
    to_title = request.args['to_title']
    to_contents = request.args['to_contents']
    
    # DB에 입력
    print(updateData(name, to_name,to_title,to_contents))
    result = selectProductPool()

    return render_template('check.html', result=result)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True)