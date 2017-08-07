# -*- coding: UTF-8 -*-
import time
from handler import Handler
from db_executer import Db_executer

class Create_dir_handler(Handler):
    def handler(self, request, db):

        if not request.json or \
                not 'user_id' in request.json or \
                not 'parent_id' in request.json or \
                not 'dir_name' in request.json:
            raise Exception('request json error:' + request.json)

        user_id = request.json['user_id']
        parent_id = request.json['parent_id']
        dir_name = request.json['dir_name']

        dir_id = self.get_uuid()

        last_time = int(time.time() * 1000)

        ret = True
        if parent_id == '0':
            #创建在顶级目录下
            if not Db_executer.create_dir(db, user_id, '0', dir_id, dir_name, last_time):
                print 'Create_dir_handler:Db_executer failed'
                ret = False
        else:
            #检查父目录是否存在
            if not Db_executer.dir_id_exists(db, parent_id):
                print 'Create_dir_handler:parent_id:%s not exists'%(parent_id)
                ret = False
            else:
                #创建目录
                if not Db_executer.create_dir(db, user_id, parent_id, dir_id, dir_name, last_time):
                    print 'Create_dir_handler:Db_executer failed'
                    ret = False

        ret_json = {}

        if ret:
            ret_content = {}
            ret_content['dir_id'] = dir_id
            ret_content['last_time'] = last_time

            ret_json['result'] = 'success'
            ret_json['content'] = ret_content
        else:
            ret_json['result'] = 'failed'

        return str(ret_json)

