import pymysql

class dba:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',)
    cursor = connection.cursor()

    def dataBase(self):

        try:
            cursor = self.connection.cursor()
            cursor.execute('create database DLC')

        except Exception as e:
            print('ERROR IN DBA: ',e)

    def update(self):
        try:

            self.cursor.execute()

        except Exception as e:
            print('ERROR IN DBA: ', e)

    def create(self):
        try:

            self.cursor.execute()

        except Exception as e:
            print('ERROR IN DBA: ', e)
    def delete(self):
        try:

            self.cursor.execute()

        except Exception as e:
            print('ERROR IN DBA: ', e)
