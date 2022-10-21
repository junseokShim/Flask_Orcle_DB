
import cx_Oracle as o # 별도 설치 필요 pip install cs_Oracle

dsn = o.makedsn('localhost', '1521', 'xe')
mypool = o.SessionPool(user='goorm', password='goorm', dsn=dsn, min=1, max=5, increment=1)

def insertFormatPool(pname, pnum, pdate):
    try:
        sql ="insert into product values(:pname, :pnum, to_date(:pdate,'YYYY-MM-DD'))"
        conn = mypool.acquire()
        cur = conn.cursor()
        cur.execute(sql, (pname, pnum, pdate))
        conn.commit()
        cur.close
        conn.close() # 연결 끊기
        return f'입력되었습니다.:{cur.rowcount}'
    except Exception as err:
        return f'입력실패:{err}'
    
def selectProductPool():
    try:
        sql ="select * from product"
        conn = mypool.acquire()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall() # 결과값
        cur.close()
        conn.close() # 연결 끊기
        return result
    except Exception as err:
        return f'에러:{err}'
    
def searchFormatPool(sname):
    try:
        sql =f"select * from product where pname like '%{sname}%'"
        conn = mypool.acquire()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall() # 결과값
        cur.close
        conn.close() # 연결 끊기
        return result
    except Exception as err:
        return f'에러:{err}'
