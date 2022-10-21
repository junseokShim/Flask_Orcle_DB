from flask import Flask, request, render_template, redirect
import sys
from bmi import divide_states

application = Flask( __name__ )
    
@application.route("/form")
def hello():
    return render_template('form.html')

@application.route("/formresult")
def output_result():
    height = float(request.args['myHeight'])
    weight = float(request.args['myWeight'])
    
    img, rate =divide_states(height, weight)
    
    return f'''
    <div align='center'>
    키 : {height} <br>
    몸무게 : {weight} <br>
    비만도 : {rate} <br>
    <div>
    <img src="static/{img}.png">
    '''

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True)