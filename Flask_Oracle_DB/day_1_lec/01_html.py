from flask import Flask, request, render_template, redirect
import sys

application = Flask(__name__)
#application = Flask(__name__, static_folder="static", template_folder="templates")
# [DEFAULT] static_folder = "static" // 해당 변수명 변경을 통해 기본 static folder 변경 가능
# [DEFAULT] template_folder = "tamplates" // 해당 변수명 변경을 통해 기본 template_foloder 변경 가능

@application.route("/")
def hello():
    return "Hello, this path is a route path!" # response route path

@application.route("/hi")
def hello_hi():
    return "<h1>Hello, this path is a hi path</h1>" # response hi path

@application.route("/hn") # html document를 response 하는 방법
def hn():
    # rendoer_template : jinja를 통해 문서를 가져옴
    return render_template('a.html') # response hn path

@application.route("/b") # html document를 response 하는 방법
def b():
    # rendoer_template : jinja를 통해 문서를 가져옴
    return render_template('b.html') # response b path

@application.route("/c") # html document를 response 하는 방법
def c():
    # rendoer_template : jinja를 통해 문서를 가져옴
    return render_template('c.html') # response c path

@application.route("/d") # html document를 response 하는 방법
def d():
    # rendoer_template : jinja를 통해 문서를 가져옴
    return render_template('d.html') # response d path

@application.route("/e") # html document를 response 하는 방법
def e():
    # rendoer_template : jinja를 통해 문서를 가져옴
    return render_template('e.html') # response e path

@application.route("/f") # html document를 response 하는 방법
def f():
    # rendoer_template : jinja를 통해 문서를 가져옴
    return render_template('f.html') # response e path


# web server 구동
if __name__ == "__main__": 
    # debug = True -> Server restart없이 Web browser update
    application.run(host='0.0.0.0', port=3000, debug=True) 
    
    