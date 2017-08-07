from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import render_template, redirect, url_for, send_from_directory
from gevent.wsgi import WSGIServer
import gevent
import os
from handler.create_dir_handler import Create_dir_handler
import MySQLdb

app = Flask(__name__)

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWD = '123456'
DB_DATABASE = 'YHNote_note'

@app.route('/yhnote/api/v1.0/create_dir', methods=['POST'])
def create_idr():
    db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWD, DB_DATABASE)
    handler = Create_dir_handler()
    result_json = handler.handler(request, db)
    db.close()
    return jsonify(result_json)

@app.route('/yhnote/api/v1.0/create_file',methods=['POST'])
def create_file():
    db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWD, DB_DATABASE)
    handler = Create_file_handler()
    result_json = handler.handler(request, db)
    db.close()
    return jsonify(result_json)


if __name__ == '__main__':

    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

