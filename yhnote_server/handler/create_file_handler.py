# -*- coding: UTF-8 -*-
import time
import os
from handler import Handler
from db_executer import Db_executer
from werkzeug import secure_filename

class Create_file_handler(Handler):
    TEMP_DIR = '/tmp/yhnote'

    def __init__(self):
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)

    def handler(self, request, db):

        '''
        if not request.json or \
                not 'user_id' in request.json or \
                not 'parent_id' in request.json or \
                not 'format' in request.json or \
                not 'file_name' in request.json:
            raise Exception('request json error:' + request.json)

        if not request.files or \
                not 'file' in request.files:
            raise Exception('request files error' + request.files)
        '''

        user_id = request.json['user_id']
        parent_id = request.json['parent_id']
        format = request.json['format']
        file_name = request.json['file_name']

        file_id = self.get_uuid()

        submitted_file = request.files['file']
        if submitted_file:
            download_file_name = self.download_file(submitted_file, file_id)
            if not download_file_name:
                raise Exception('Create_file_handler:download_file failed')
            print 'download file success:' + download_file_name
        '''
        if not self.insert_to_db(user_id, parent_id, file_id, file_name, format):
            if os.path.exists(download_file_name):
                os.remove(download_file_name)
            raise Exception('Create_file_handler:insert_to_db failed')
        '''



    def download_file(self, submit_file, file_name):
        if submit_file:
            filename = secure_filename(submit_file.filename)
            submit_file.save(os.path.join(TEMP_DIR, filename))
            return TEMP_DIR + '/' + filename

        return ''

    def insert_to_db(self, user_id, parent_id, file_id, file_name, format):
        last_time = int(time.time() * 1000)

        ret = True
        if parent_id == '0':
            # 创建在顶级目录下
            if not Db_executer.create_file(db, user_id, '0', file_id, file_name, format, last_time):
                print 'Create_file_handler:Db_executer failed'
                ret = False
        else:
            # 检查父目录是否存在
            if not Db_executer.dir_id_exists(db, parent_id):
                print 'Create_file_handler:parent_id:%s not exists' % (parent_id)
                ret = False
            else:
                # 创建目录
                if not Db_executer.create_dir(db, user_id, parent_id, dir_id, dir_name, last_time):
                    print 'Create_file_handler:Db_executer failed'
                    ret = False
        return ret