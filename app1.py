# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:09:28 2021

@author: r.n.gokul
"""

import numpy as np
import json
from flask import Flask, request, jsonify, render_template
import pickle

server = Flask(__name__)

@server.route('/')
def home():
    return "Gokul"

@server.route('/a')
def home_a():
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y=json.loads(x)
    print(type(x))
    print(type(y))
    return y

@server.route('/b')
def home_b():
    x =  [{ "name":"John", "age":30, "city":"New York"}]
    y=json.dumps(x)
    return y

@server.route('/b1')
def home_b1():
    x =  '[{ "name":"John", "age":30, "city":"New York"}]'
    y=json.dumps(x)
    z=json.loads(y)
    return z


@server.route('/c')
def home_c():
    x =  [{ "name":"John", "age":30, "city":"New York"},{"name":"rahul"}]
    y=jsonify(x)
    print(type(x))
    print(type(y))
    return y

@server.route('/d')
def home_d():
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y=jsonify(x)
    print(type(x))
    print(type(y))
    return y

@server.route('/e', methods=['POST','GET'])
def home_e():
    x =  [{ "name":"John", "age":30, "city":"New York"},{"name":"sachin", "age":45}]
    for item in x:
        print(json.loads(json.dumps(item)))
    y=json.dumps(x[0])
    print(type(x))
    print(type(y))
    return json.loads(y)

@server.route('/f')
def home_f():
    x =  '[{ "name":"John", "age":30, "city":"New York"}]'
    y=json.dumps(x)
    return y



if __name__ == "__main__":
    #server.run(debug=True)
    server.run(host='0.0.0.0',port=8080)