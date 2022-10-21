from flask import Flask, request, render_template, redirect, jsonify
import sys
import cx_Oracle as o
from base64 import b64encode

dsn = o.makedsn('localhost','1521','xe')
mypool = o.SessionPool( user='goorm', password='goorm', dsn=dsn, min=1, max=5, increment=1 )


application = Flask( __name__ )
application.config['JSON_AS_ASCII'] = False

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/fileForm")
def fileForm():
    return render_template('fileForm.html')

@application.route("/fileSend", methods=['POST'] )
def fileSend():
    # request.args header
    # request.form body(쿼리스트링)에 
    # request.files 파일전송파라미터 인경우
    print('call')
    try:
        n = request.form['myname']
        f = request.files['myfile'] #파일객체
        # print( '이름', n)
        # print( f.filename)
        # f.save("aa.jpg") # f.save("image/aa.jpg")
        sql = 'insert into imgup(name,imgfile) values(:name,:imgfile)'
        conn = mypool.acquire()
        cur = conn.cursor()
        cur.execute( sql, (f.filename, f.read() ) )
        conn.commit()
        conn.close()

        return "<h1>파일 db저장</h1>"
    except Exception as err:
        return f"<h1>에러:{err}</h1>"


    
@application.template_filter('base64')
def strftime_filter(img):
    b = b64encode( img.read()).decode('utf-8')
    return 'data:;base64,'+b


@application.route("/selectImg")
def selectImg():
    
    sql = 'select * from imgup'
    conn = mypool.acquire()
    cur = conn.cursor()
    cur.execute( sql)
    result = cur.fetchall()
    return render_template('selectImg.html', result=result) 
    # data = []
    # for n, img in result:
    #     b = b64encode( img.read()).decode('utf-8')
    #     data.append( (n, 'data:;base64,'+b) )
        
    # conn.close()         
    # return render_template('selectImg.html', result=data)
    
@application.route("/ajaxForm")
def ajaxForm():
    return render_template('ajaxForm.html') 

@application.route("/ajaxtest")
def ajaxtest():
    return "<h1>hello korean</h1>"

@application.route("/travelmain")
def travelmain():
    return render_template('travelmain.html') 

@application.route("/thai")
def thai():
    # return "<h1>태국여행정보</h1>"
    return render_template('thai.html') 

@application.route("/phil")
def phil():
    return "<h1>필리핀 여행정보</h1>"

@application.route("/hong")
def hong():
    return "<h1>홍콩여행정보</h1>"



@application.route("/selectStudent")
def selectStudent():
    sql = 'select * from student'
    conn = mypool.acquire()
    cur = conn.cursor()
    cur.execute( sql)
    result = cur.fetchall()    
    conn.close()
    return render_template("selectStudent.html",result=result)


@application.route("/selectAjaxhtml")
def selectAjaxhtml():
    return render_template('selectAjax.html') 


@application.route("/selectJson")
def selectJson():
    #json array
    # d = [{'name':'홍길동','age':20},{'name':'이순신','age':30}]
    sql = 'select name, age from student'
    conn = mypool.acquire()
    cur = conn.cursor() #dictionary=True
    cur.execute( sql)
    cur.rowfactory = lambda *args: dict( zip( [d[0] for d in cur.description], args) )
    result = cur.fetchall()   
    print( result) 
    #[('홍길동',20),('이순신',20)] ==>[{'name':'홍길동','age':20},('이순신',20)]
    conn.close()    
    return jsonify(result)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8077, debug=True)

    
    
    
    
    
    
    
    
    
    
    