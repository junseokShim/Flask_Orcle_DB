from flask import Flask, request, render_template, redirect, jsonify
import sys
import cx_Oracle as o
import json

dsn = o.makedsn('localhost','1521','xe')
mypool = o.SessionPool( user='goorm', password='goorm', dsn=dsn, min=1, max=5, increment=1 )

application = Flask( __name__ )
application.config['JSON_AS_ASCII'] = False

@application.route("/")
def hello():
    return "Hello goorm!"



# Sub Send Event
# >> Web 소켓 등의 실시간으로 데이터를 받아오는데 적절한 방법롤 (주식 차트 등등..)


@application.route("/sse")
def sse():
    return render_template("/sse.html")


@application.route("/ssecall")
def ssecall():
    
    print('sse start')
    
    # 전송 규약 (protocol)
    # text/event-stream
    data = "hello" # 전송할 데이터
    time = "2000"  # 시간
    sendStr = f"data: {data}\nretry : {time}\n\n"
    resp = application.make_response(sendStr)
    resp.mimetype = "text/event-stream"
    
    print('sse end')
    return resp


@application.route("/ssecalldb")
def ssecalldb():

    sql = 'select name, age from student'
    conn = mypool.acquire()
    cur = conn.cursor() #dictionary=True
    cur.execute( sql)
    cur.rowfactory = lambda *args: dict( zip( [d[0] for d in cur.description], args) )
    result = cur.fetchall()   

    # data = jsonify(result)
    data = json.dumps(result,ensure_ascii=False)  
    print( data )
    sendStr = f"data: {data}\nretry: 2000\n\n"
    resp = application.make_response(sendStr)
    resp.mimetype = "text/event-stream"
    conn.close()
    return resp


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True)
