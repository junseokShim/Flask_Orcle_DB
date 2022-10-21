import cx_Oracle as o

def insertData(name, age, birth):
    '''
    DML insert function
    '''
    try:
        sql = "insert into student( name, age, birth) values(:name,:age,to_date(:birth,'YYYY-MM-DD') )"
        dsn = o.makedsn('localhost','1521','xe')
        
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.execute( sql ,(name, age, birth)) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        
        return f'{cur.rowcount} 추가성공'

    except Exception as err:
        return f'추가 실패 : {err}'
    

def updateData(to_name, to_age, name):
    '''
    DML update function
    '''
    try:
        sql = "update student set name=:name, age=:age where name=:name"
        dsn = o.makedsn('localhost','1521','xe')
        
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.execute( sql ,(to_name, to_age, name)) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        
        return f'{cur.rowcount} 추가성공'

    except Exception as err:
        return f'추가 실패 : {err}'
    

def deleteData(age):
    '''
    DML delete function
    '''
    try:
        sql = "delete from student where age=:age"
        dsn = o.makedsn('localhost','1521','xe')
        
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.execute( sql ,(age,)) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        
        return f'{cur.rowcount} 삭제 성공'

    except Exception as err:
        return f'삭제 실패 : {err}'

def selectStudent():
    try:
        sql ="select * from student"
        dsn = o.makedsn('localhost','1521','xe')
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        cur.execute( sql ) #포맷데이터는 반드시 튜플(딕셔너리)로
        result =  cur.fetchall()
        conn.close()
        # for n,a,b in result:
        #     s = b.strftime('%Y년%m월%d일 %H시%M분%S초')
        #     print(n,a,s)
        return result
    
    except Exception as err:
        return f'에러 : {err}'    
    
#selectStudent()