from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )


@application.route("/")
def hello():    
    return "Hello goorm!" # response


@application.route("/form") # html document를 response 하는 방법
def form():
    return render_template('form.html') # response hn path

@application.route("/formresult")
def form1result():
    return render_template('formresult.html',
                          sum_result=float(request.args["num1"])+float(request.args["num2"]) 
                          )

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True) 