from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )


@application.route("/")
def hello():
    
    return "Hello goorm!" # response

@application.route("/hn") # html document를 response 하는 방법
def hn():
    # rendoer_template : jinja를 통해 문서를 가져옴
    return render_template('a.html') # response hn path


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True) 