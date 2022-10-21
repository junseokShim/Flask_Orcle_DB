from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )


@application.route("/")
def main_page():
    return render_template('/tempinc_test/maincontent.html') # response

@application.route("/formresult")
def form1result():
    print(request.args)
    return render_template('formresult.html',
                          name=request.args["myname"],
                          tel=request.args["mytel"],
                          email=request.args["myemail"],
                          size=request.args["size"],
                          toping=request.args.getlist("toping"),
                          time=request.args["mytime"],
                          txt=request.args["mytxt"]
                          )

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True) 