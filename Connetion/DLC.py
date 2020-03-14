from aifc import Error

import pymysql



class BancoDlc:

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

    def update(self):

        '''Função destinada a alteração de dados '''
        try:
            query = ';'
            self.cursor.execute(query)
            self.connection.commit()
            self.select()
            self.close()

        except Exception as e:
            print('Error message in the database : ',e)

    def create(self):
        try:

            self.cursor.execute('')

        except Exception as e:
            print('Error message in the database : ',e)

    def delete(self, query):
        try:

            self.cursor.execute(query)

        except Exception as e:
            print('Error message in the database : ',e)

    def insert(self):

       lista = list()
        
       for i in range(3):
           valor = f'{};'
           lista.append(valor)

        try:



            self.cursor.execute(f"""INSERT INTO dlc (id_dlc, cod_dlc, nome_dlc) 
                           VALUES 
                           ({lista}) """)
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

            '''self.curso.rowcount retorna a quantidade de linhas executadas '''
            print("Total number of rows in Laptop is: ", self.cursor.rowcount)

            print("\nPrinting each laptop record")

            '''Me retorna o banco de dados inteiro'''
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



