# -*- coding: UTF-8 -*-
import MySQLdb

class Db_executer(object):

    @staticmethod
    def dir_id_exists(db, dir_id):

        cursor = db.cursor()

        sql = "select dir_id from dir_info where dir_id='%s'"%(dir_id)

        try:
            cursor.execute(sql)

            results = cursor.fetchall()

            if results:
                return True
            else:
                return False
        except:
            print "Error: unable to fecth data"
            return False

    @staticmethod
    def create_dir(db, user_id, parent_id, dir_id, dir_name, last_time):
        cursor = db.cursor()

        sql = "INSERT INTO dir_info(dir_id,user_id,parent_id,dir_name,last_time) " \
              "VALUES('%s','%s','%s','%s',%d)"%(dir_id, user_id, parent_id, dir_name, last_time)


        try:
            cursor.execute(sql)

            db.commit()
        except:
            db.rollback()
            return False

        return True

    @staticmethod
    def create_file(db, user_id, parent_id, file_id, file_name, format, last_time):
        cursor = db.cursor()

        sql = "INSERT INTO file_info(file_id, user_id, dir_id, file_name, format, last_time) " \
              "VALUES(%s, %s, %s, %s, %s, %d)"%(file_id, user_id, parent_id, file_name, format, last_time)

        try:
            cursor.execute(sql)

            db.commit()
        except:
            db.rollback()
            return False

        return True