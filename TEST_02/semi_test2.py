
from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )

@application.route("/quiz2")
def quiz2():
    return render_template('./quiz/main.html') # response

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8077, debug=True) 
