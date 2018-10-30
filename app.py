#!/usr/bin/env python
#encoding:utf-8
'''
@author: yangmv
@file: app.py
@time: 18/10/29下午2:24
'''

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)