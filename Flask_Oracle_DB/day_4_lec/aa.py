from flask import Flask, request, render_template, redirect, jsonify
import sys

application = Flask( __name__ )

@application.route("/")
def hello():
    return "Hello goorm!"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8077, debug=True)

    
    
    
    
    
    
    
    
    
    
    