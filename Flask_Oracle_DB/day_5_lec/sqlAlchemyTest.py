from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "oracle+cx_oracle://goorm:goorm@localhost:1521/xe"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    """
    기존 db table을 사용하려면
    해당 db table에 맞게 column명 정의해 모델 생성하면됨
    """
    __tablename__ = 'users' # table 정의
    
    # column 명 정의 (id, username, email)
    # db.Sequence --> 순서대로 1씩 증가하는 column
    # primary_key = True 해당 column을 주 키로 사용
    
    id = db.Column(db.Integer, db.Sequence('aaa', start=1, increment=1), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # 생성자 함수
    def __init__(self, username, email):
        # class의 member data
        self.username = username
        self.email = email

    # member 함수
    
    # overiding 함수 // 객체 정의 시, 출력
    def __repr__(self):
        return f'사용자이름:{self.username}'

@app.route("/")
def hello():
    return "hee"

@app.route("/insertForm")
def insertForm():
    return render_template('insertForm.html')

@app.route("/insertResult")
def insertResult():
    try:
        myname = request.args['myname']
        myemail = request.args['myemail']
        user = User(myname, myemail)
        db.session.add(user)
        db.session.commit()
        return "<h1> 추가 성공 </h1>"
    
    except Exception as err:
        return "<h1> 추가 실패 </h1>"

    
@app.route("/selectAll")
def selectAll():
    userList = User.query.all()
    return render_template('selectUser.html', userList = userList)


@app.route("/selectW")
def selectW():
    
    userList = User.query.filter(User.username.like('%이%'))
    # 그 외
    #userList = User.query.filter(User.username=="홍길동") # > >= <= == 사용
    #User.query.filter(User.username=="홍길동", User.email.like(%'a'%)) // AND
    #User.query.filter((User.username=="홍길동" | User.email.like(%'a'%))) // OR
    #User.query.filter(User.username.in_(["홍길동","이순신"])) 
    #User.query.filter(User.age.between(10, 30)) // between
    # select * from user order by username asc; #desc
    # User.query.order_by( User.username.desc() ) // 내림차순 정렬
    # User.query.order_by( User.username.asc() )  // 오름차순 정렬
    
    return render_template('selectUser.html', userList = userList)
    

@app.route("/update")
def update():
    userList = User.query.filter( User.username=='홍길동' )
    userList.update( {'username':'홍길동1', 'email':'tt@tt.com'} )
    db.session.commit()
    return "<h1>수정됨</h1>"


@app.route("/delete")
def delete():
    userList = User.query.filter( User.username=='홍길동1' )
    userList.delete()
    db.session.commit()
    return "<h1>삭제됨</h1>"
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
    
    
# with app.app_context():
#     db.create_all() # db.Model을 상속받은 클래스의 테이블을 생성
#                     # 단 이미 생성되어 있을 경우, 있으면 pass
        
#     user1 = User('홍길동', 'aa@bb.com')
#     user2 = User('이순신', 'bb@cc.com')
#     user3 = User('임꺽정', 'cc@dd.com')
#     user4 = User('김철수', 'dd@ee.com')
    
#     db.session.add(user1) # insert
#     db.session.add(user2) # insert
#     db.session.add(user3) # insert
#     db.session.add(user4) # insert
#     db.session.commit() # commit