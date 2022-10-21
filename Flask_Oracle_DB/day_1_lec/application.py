from flask import Flask
import sys

# import module_name
# from function import module_name
## __name__ = "__main__"
application = Flask(__name__)


@application.route("/") # Decorator(특정 함수에 특정 기능을 부여해주는 Python 문법) : Routing information
# rest API : html 문서의 효율적 관리를 위해 계층적으로 관리하기 위한 방법, 따라서 Decorator에 경로를 적어줌
# Response 시 호출되는 응답함수
def hello():
    return "Hello goorm!" # response


if __name__ == "__main__": 
    # Web server 구동
    # host = '0.0.0.0' 클라리언트 모든 ip에 대해 응답
    # sys.argv[1] = ['application.py', 'port_number']
    application.run(host='0.0.0.0', port=int(sys.argv[1])) # web server 구동
    
    