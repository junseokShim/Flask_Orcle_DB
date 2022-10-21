from flask import Flask, request, render_template, redirect, jsonify
import sys
import cx_Oracle as o # 별도 설치 필요 pip install cs_Oracle
from base64 import b64encode
from dbHandlePool import insertFormatPool, searchFormatPool, mypool

# dsn = o.makedsn('localhost', '1521', 'xe')
# mypool = o.SessionPool(user='goorm', password='goorm', dsn=dsn, min=1, max=5, increment=1)

application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False


@application.route("/")
def hello():
    return "Hello goorm!"  # response

@application.template_filter('strftime')
def strftime_filter(dt):
    return dt.strftime('%Y년%m월%d일')

@application.route("/pMain")
def pMain():
    return render_template('pMain.html')

@application.route("/insertForm")
def insertForm():
    return render_template('insertForm.html')

@application.route("/insertResult")
def insertResult():
    pname = request.args['pname']
    pnum = int(request.args['pnum'])
    pdate = request.args['pdate']
    result = insertFormatPool(pname, pnum, pdate)
    return f'<h1>{result}</h1>' 

@application.route("/selectProductAll")
def selectProductAll():
    sql = 'select * from product'
    conn = mypool.acquire()
    cur = conn.cursor()
    cur.execute(sql)
    cur.rowfactory = lambda *args: dict( zip( [d[0] for d in cur.description], args))
    result = cur.fetchall()    
    print("result", result)
    conn.close()
    return jsonify(result)

@application.route("/searchForm")
def searchForm():
    return render_template('searchForm.html')


@application.route("/searchResultPool")
def searchResultPool():
    sname = request.args['sname']
    sql =f"select * from product where pname like '%{sname}%'"
    conn = mypool.acquire()
    cur = conn.cursor()
    cur.execute(sql)
    cur.rowfactory = lambda *args: dict( zip( [d[0] for d in cur.description], args))
    result = cur.fetchall()    
    print("result", result)
    conn.close()
    return jsonify(result)    
    # sname = request.args['sname']
    # result = searchFormatPool(sname)
    # return render_template('searchResultPool.html', result=result)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8077, debug=True)
