#coding = utf-8

import flask
from flask import Flask
import config



app=Flask(__name__)
app.secret_key = config.SECRET_KEY



@app.route('/',methods=['GET'])
def test():

    print flask.request.args

    return 'hello'




app.run('127.0.0.1',8999)