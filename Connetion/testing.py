from aifc import Error

import pymysql


class dba:

    ''' https://pynative.com/python-mysql-tutorial/

    Documentação do Mysql para Python, tudo que eu preciso para criação e manipação do banco de dados

    '''

    connection = pymysql.connect(host='localhost',
                                 database = 'DLC',
                                 user='root',
                                 passwd='',)
    cursor = connection.cursor()

    def createDataBase(self, banco):
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

    def insert(self):
        try:
            self.cursor.execute("""INSERT INTO dlc (id_dlc, cod_dlc, nome_dlc) 
                           VALUES 
                           (2, 24, 'Call of duty') """)
            self.connection.commit()
            print(self.cursor.rowcount, "Record inserted successfully into Laptop table")

            self.close()

        except Exception as e:
            print('Error message in the database : ', e)

    def select(self):
        try:
            sql_select_Query = "select * from dlc"
            self.cursor.execute(sql_select_Query)
            records = self.cursor.fetchall()
            print("Total number of rows in Laptop is: ", self.cursor.rowcount)

            print("\nPrinting each laptop record")
            for row in records:
                print(row)

            self.close()
        except Error as e:
            print("Error reading data from MySQL table", e)


    def close(self):
        try:

            self.connection.close()
            self.cursor.close()

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



