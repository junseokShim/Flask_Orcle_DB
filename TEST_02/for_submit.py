pizza = '''
<fieldset>
    <legend>피자 사이즈</legend>           
    <input type="radio" name="size" value="small"><label>small</label><br>
    <input type="radio" name="size" value="medium"><label>medium</label><br>
    <input type="radio" name="size" value="large"><label>large</label><br>
</fieldset>'''

inpo = '''
<label>고객명 : </label>
<input type="text" required name="myname"> <br>
<br>
<label>전화번호 : </label>
<input type="tel" pattern="\d{2,3}-\d{3,4}-\d{4}" placeholder="000-0000-0000 형식으로 입력" name="mytel"><br>
<br>
<label>이메일: </label>
<input type="email" name="myemail"><br>'''

toping = '''
<fieldset>
    <legend>토핑선택</legend>           
    <input type="checkbox" name="toping" value="베이컨"><label>베이컨</label><br>
    <input type="checkbox" name="toping" value="치즈"><label>치즈</label><br>
    <input type="checkbox" name="toping" value="양파"><label>양파</label><br>
</fieldset>'''

hope_time = '''
<label>희망배송시간 : </label>
<input type="time" name="mytime" min="09:00" max="22:00"><br>
'''

needs = '''
<label>배송 요청사항 : </label>
<textarea cols="10" name="mytxt"></textarea>'''

header = '''
<h1>피자주문서</h1>
<br>
'''

formresult = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Junseok's page_a</title>
    </head>
    <body>
        <br><br>
        <h4>고객명 : {{name}} </h4>
        <h4>전화번호 : {{tel}} </h4>
        <h4>이메일 : {{email}} </h4>
        <h4>피자사이즈 : {{size}} </h4>
        <h4>토핑선택</h4>
        <ul>
            {% for element in toping %}
            <li>{{element}}</li>
            {% endfor %}
        </ul>
        <h4>희망배송시간 : {{time}} </h4>
        <h4>배송요청사항 : {{txt}} </h4>
    </body>
</html>'''

main_page = f'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>test</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
        <style>
            .result_button{
            background-color: blue;
            border: 2px solid black;
            color : white;
            weight : bold;}
        </style>
    </head>
    <body>
        <form action="/formresult" target="_blank">
            <div class="container text-center">

                {header}

                <div class="row text-center">
                    <div class="col-sm-12 bg-white">
                        {inpo}
                    </div>

                    <div class="col-sm-6 border">
                        {pizza}
                    </div>

                    <div class="col-sm-6 jumbotron">
                        {toping}
                    </div>

                    <div class="col-sm-12 bg-white">
                        {hope_time}
                    </div>
                    <div class="col-sm-12 bg-white">
                        {needs}
                    </div>

                    <button class="result_button">
                        주문하기
                    </button>
                </div>
            </div>
        </form>
    </body>
</html> '''

formresult = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Junseok's page_a</title>
    </head>
    <body>
        <br><br>
        <h4>고객명 : {{name}} </h4>
        <h4>전화번호 : {{tel}} </h4>
        <h4>이메일 : {{email}} </h4>
        <h4>피자사이즈 : {{size}} </h4>
        <h4>토핑선택</h4>
        <ul>
            {% for element in toping %}
            <li>{{element}}</li>
            {% endfor %}
        </ul>
        <h4>희망배송시간 : {{time}} </h4>
        <h4>배송요청사항 : {{txt}} </h4>
    </body>
</html>
'''

from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )


@application.route("/")
def main_page():
    return main # response

@application.route("/formresult")
def form1result():
    print(request.args)
    return render_template('formresult',
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