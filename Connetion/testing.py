import pymysql

class dba:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',)
    cursor = connection.cursor()

    def dataBase(self, banco):
        '''Função destinada a criação do banco de dados'''

        try:
            cursor = self.connection.cursor()
            cursor.execute(f'create database {banco}')

        except Exception as e:
            print('Error message in the database : ',e)

    def update(self, query):

        '''Função destinada a alteração de dados '''
        try:

            self.cursor.execute(query)

        except Exception as e:
            print('Error message in the database : ',e)

    def create(self, query):
        try:

            self.cursor.execute(query)

        except Exception as e:
            print('Error message in the database : ',e)

    def delete(self, query):
        try:

            self.cursor.execute(query)

        except Exception as e:
            print('Error message in the database : ',e)

    def select(self,):
        try:
            self.cursor.execute('use DLC;')
            self.cursor.execute('select * from dlc;')




        except Exception as e:
            print('Error message in the database : ', e)

    def close(self):
        try:

            self.connection.close()

        except Exception as e:
            print('Error message in the database : ',e)

    def showDatabase(self):
        '''
        Este método verifica a extência de todos os bancos de dados
        '''

        try:
            cursor = self.connection.cursor()
            cursor.execute('SHOW DATABASES')

            for x in cursor:
                print(x)

        except Exception as e:
            print('Error message in the database : ',e)



