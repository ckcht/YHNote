

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import render_template, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from gevent.wsgi import WSGIServer
import gevent
import os


UPLOAD_FOLDER = '/var/lib/yhnote/files'
ALLOWED_EXTENSIONS = set(['md', 'yh'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#File extension checking
def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/yhnote/file_service/v1.0/upload_file', methods=['POST'])
def create_task():
    submitted_file = request.files['file']
    if submitted_file and allowed_filename(submitted_file.filename):
        filename = secure_filename(submitted_file.filename)
        submitted_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'failed', 'reason': 'file name error'})
    return jsonify({'result': 'failed'})


@app.route('/yhnote/file_service/v1.0/download_file/<filename>', methods=['GET'])
def download(filename):
    if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    return jsonify({'result': 'failed', 'reason': 'can not find file'})


if __name__ == '__main__':

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    http_server = WSGIServer(('', 8000), app)
    http_server.serve_forever()
