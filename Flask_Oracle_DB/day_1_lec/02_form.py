from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )


@application.route("/")
def hello():
    return "Hello goorm!" # response

@application.route("/form")
def form():
    return render_template('form.html')

@application.route("/formresult")
def formresult():
    print(request.args) # querystring 값을 반환함
    name = request.args['myname']
    age = request.args['myage']
    birth = request.args['mybirth']
    time = request.args['mytime']
    tel = request.args['mytel']
    email = request.args['myemail']
    url = request.args['myurl']
    color = request.args['color']
    hobby = ', '.join(request.args.getlist('hobby'))
    company = request.args['company']
    txt = request.args['mytxt']
    return f'''<h1>결과 </h1>
<pre>
이름 : {name} 
나이 : {age}
생일 : {birth}
시간 : {time}
전화번호 : {tel}
이메일 : {email}
주소 : {url}
색깔 : {color}
취미 : {hobby}
회사 : {company}
설명 : {txt}
</pre>'''

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True)