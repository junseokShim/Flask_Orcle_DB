import cx_Oracle as o

# 미리 연결을 맺어 풀에 등록
dsn = o.makedsn('localhost', '1521', 'xe')
mypool = o.SessionPool(user='goorm', password='goorm', dsn=dsn, min=1, max=5, increment=1) # connection pool을 5개까지 만듬

# 이미 연결되어 있으므로 필요X
# dsn = o.makedsn('localhost','1521','xe')
# conn = o.connect( user='goorm', password='goorm', dsn=dsn )
def selectProductPool():
    try:
        sql = "select * from flask"
        conn = mypool.acquire()
        cur = conn.cursor()
        cur.execute( sql ) #포맷데이터는 반드시 튜플(딕셔너리)로
        result =  cur.fetchall()

        cur.close() # DB 관리 메모리에 올라온 Data를 제거
        conn.close() # 풀에 반납
        return result
    
    except Exception as err:
        return f'에러 : {err}'
    
def conditionalSelectProductPool(name):
    print(name)
    try:
        sql = f"select * from flask where name like '%{name}%'"
        conn = mypool.acquire()
        cur = conn.cursor()
        cur.execute( sql ) #포맷데이터는 반드시 튜플(딕셔너리)로
        result =  cur.fetchall()

        cur.close() # DB 관리 메모리에 올라온 Data를 제거
        conn.close() # 풀에 반납

        return result
    
    except Exception as err:
        return f'에러 : {err}'
    
def insertData(name, title, contents):
    '''
    DML insert function
    '''
    try:
        sql = "insert into flask( name, title, contents) values(:name,:title,:contents )"
        dsn = o.makedsn('localhost','1521','xe')
        
        conn = mypool.acquire()
        cur = conn.cursor()
        nCnt = cur.execute( sql ,(name, title, contents)) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        
        return f'{cur.rowcount} 추가성공'

    except Exception as err:
        return f'추가 실패 : {err}'
    
def deleteData(name):
    '''
    DML delete function
    '''
    try:
        sql = "delete from flask where name=:name"
        dsn = o.makedsn('localhost','1521','xe')
        
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.execute( sql ,(name,)) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        
        return f'{cur.rowcount} 삭제 성공'

    except Exception as err:
        return f'삭제 실패 : {err}'
    
    
def updateData(name, to_name, to_title, to_contents):
    '''
    DML update function
    '''
    try:
        sql = f"update flask set name='{to_name}', title='{to_title}', contents='{to_contents}' where name='{name}'"
        dsn = o.makedsn('localhost','1521','xe')
        
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.execute(sql) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        
        return f'{cur.rowcount} 추가성공'

    except Exception as err:
        return f'추가 실패 : {err}'
    