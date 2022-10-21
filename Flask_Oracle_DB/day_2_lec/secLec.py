from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )


@application.route("/")
def hello():    
    return "Hello goorm!" # response

@application.route("/a") # html document를 response 하는 방법
def a():
    s = 'hello'
    n = 100
    return render_template('a.html', j1=s, j2=n) # response hn path

@application.route("/form1") # html document를 response 하는 방법
def form():
    return render_template('form1.html') # response hn path

@application.route("/form1result")
def form1result():
    return render_template('form1result.html',
                          name=request.args["myname"], 
                          age=request.args["myage"],
                          birth=request.args["mybirth"]
                          )


@application.route("/jinjaexp") # html document를 response 하는 방법
def jinjaexp():
    n = 5
    return render_template('jinjaexp.html', num=n) # response hn path

@application.route("/jinjafor") # html document를 response 하는 방법
def jinjafor():
    return render_template('jinjafor.html', myList=["사과","딸기","포도","수박"]) # response hn path

@application.route("/tablefor") # html document를 response 하는 방법
def tablefor():
    data = []
    data.append({'name':'홍길동', 'age':20})
    data.append({'name':'이순신', 'age':30})
    data.append({'name':'임꺽정', 'age':40})
    return render_template('tablefor.html', myData=data) # response hn path

@application.route("/grid") # html document를 response 하는 방법
def gridfor():
    return render_template('grid.html') # response hn path

@application.route("/main") # html document를 response 하는 방법
def navbar():
    return render_template('maincontent.html') # response hn path

@application.route("/thai") # html document를 response 하는 방법
def thailand():
    return render_template('thaicontent.html') # response hn path

@application.route("/maintemp") # html document를 response 하는 방법
def toy_pjt():
    return render_template('/tempinc/maintemp.html') # response hn path

@application.route("/filtertest") # html document를 response 하는 방법
def filter_test():
    m = -10
    return render_template('filter_test.html', n=m, f=3.141592, s='abc', s1='                abc') # response hn path

@application.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

application.jinja_env.filters['reverse']= reverse_filter # 필터 등록

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True) 