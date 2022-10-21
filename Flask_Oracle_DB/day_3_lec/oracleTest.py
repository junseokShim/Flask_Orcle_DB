import cx_Oracle as o
import pandas as pd

def createTable():
    try:
        sql="create table births(byear int, male int, female int)"
        dsn = o.makedsn('localhost','1521','xe')
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        cur.execute( sql ) #insert, delete, update 반영된갯수 리턴
        conn.close()
        print('테이블생성')
        
    except Exception as err:
        print('에러발생',err)
        

def insertData(name, age, birth):
    try:
        sql = "insert into student( name, age, birth) values(:name,:age,to_date(:birth,'YYYY-MM-DD') )"
        dsn = o.makedsn('localhost','1521','xe')
        
        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.execute( sql ,(name, age, birth)) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        print(f'{conn} 추가성공')

    except Exception as err:
        print('에러발생',err)
        

# insertData('이이', 50 , '1969-03-12')
# insertData('이황', 60 , '1959-03-12')

def insertBulk(myList, table):
    try:
        sql = f"insert into {table}(byear, male, female) values(:byear,:male, :female )"
        dsn = o.makedsn('localhost','1521','xe')

        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.executemany( sql ,myList) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        print(f'{conn} 추가성공')

    except Exception as err:
        print('에러발생',err)

def insertBulk_Birth(myList):
    try:
        sql = f"insert into births(byear, male, female) values(:byear,:male, :female )"
        dsn = o.makedsn('localhost','1521','xe')

        conn = o.connect( user='goorm', password='goorm', dsn=dsn )
        cur = conn.cursor()
        nCnt = cur.executemany( sql ,myList) #insert, delete, update 반영된갯수 // 리턴, 포맷 데이터는 반드시 튜플 또는 딕셔너리

        conn.commit() #명령확정(insert, delete, update)
        conn.close()
        print(f'{conn} 추가성공')

    except Exception as err:
        print('에러발생',err)

