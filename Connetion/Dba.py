class estudo:

    valor = 'olá'

    '''função de construtor da instância, sempre que for estanciado uma classem, esses parâmetros servem para pegar o valor
    do metodo'''
    def __init__(self, nome='', idade =''):
        #Self serve para referênciar a instância da classe
        self.nome = nome
        self.idade = idade


    '''pegar o atributo da classe e retorna o valor'''
    def getValor(self):
        return self.valor

    '''Altera o valor do atributo da classe'''
    def setValor(self, valor):

        self.valor = valor

    def connection(self):
        print(self.server)


    def getName(self):

        pass

    def getMail(self):
        pass

    def getData(self):
        pass

    def close(self):
        pass


class SQLManager (object):

    def __init__(self):
        """
        :return:
        """
        self.query = ""

    def order_with_separator(self, array, bet="`", sep=","):
        """
        Order array as a string with the selected separator
        :param array:
        :return:
        """
        string = ""
        for i in range(len(array)):
            if i != len(array) - 1:
                string += bet + str(array[i]) + bet + sep + " "
            else:
                string += bet + str(array[i]) + bet
        return string

    def query_where(self, where):
        """
        Create a query for the where statement
        :param where: list with the where statement
        :return:
        """
        query = "WHERE"

        # We go throw the where statement
        for data in where:
            # We add the data column
            query += " `" + data[0] + "`"

            # We add the comparison
            query += " " + data[1]

            # We add the value
            if data[2] == "NULL":
                query += " " + data[2]
            else:
                query += " '" + str(data[2]) + "'"

            # Then we add link between statement
            query += " " + data[3]

        # We return the query
        return query

    def query_insert(self, table, columns, values):
        """
        Insert a new data into the table
        :param table: string table name
        :param columns:
        :param values:
        :return:
        """
        # First we add the insert into statement
        self.query = "INSERT INTO `" + table + "`"

        # Then we go throw each column and add the column name
        self.query += "(" + self.order_with_separator(columns) + ")"

        # Then we go throw the values and add then
        self.query += " VALUES (" + self.order_with_separator(values, bet="'") + ")"

    def query_update(self, table, columns, values, where):
        """
        Update the table query
        :param table: string with table name
        :param columns: string/list with columns values
        :param values: string/list with values
        :param where: list with where statement
        :return:
        """
        # We create the new query
        self.query = "UPDATE `" + table + "`"

        # We connect the columns and the values into one list
        concat = ["`"+columns[i]+"`='"+values[i]+"'" for i in range(len(columns))]

        # Then we add to the query this values
        self.query += " SET " + self.order_with_separator(concat, bet="")

        # Finally we add the where
        self.query += " " + self.query_where(where)

    def query_delete(self, table, where):
        """
        Delete query constructor
        :param table: string table
        :param where: list of where
        :return:
        """
        # Start the new query
        self.query += "DELETE FROM `" + table + "`"

        # Add the where statement
        self.query += " " + self.query_where(where)

    def query_select(self, table, columns, where=None, order=None, desc=True):
        """
        Create the select query
        :param table: string with table name
        :param columns: string/list with columns to be queried
        :param where: list with conditions for where
        :param order: string with the column name to order
        :param desc: boolean if the data should asc or desc
        :return:
        """
        # We start the query as select
        self.query = "SELECT"

        # Then we should check the columns to see what we should run
        if columns == "*":
            self.query += " *"
        else:
            # If it is a list we add each column to the query
            self.query += " " + self.order_with_separator(columns)

        # Then we add the statement from table
        self.query += " FROM `" + table + "`"

        # If the where is not none we add the where query
        if where is not None:
            self.query += " " + self.query_where(where)

        # If the order is not empty we add the order
        if order is not None:
            self.query += "ORDER BY " + order

            # If the desc is true
            if desc:
                self.query += " DESC"
            else:
                self.query += " ASC"

    def query_columns(self, table):
        """
        Get the query for the columns of the table
        :param table:
        :return:
        """
        self.query = "DESCRIBE `" + table + "`"

    def custom_query(self, query):
        """
        Set a custom query
        :param query: string custom query
        :return:
        """
        self.query = query

import  as mdb
from SQLManager import SQLManager

__author__ = 'pedro'


class MySQLManager(SQLManager):
    def __init__(self, host, login, password, database):
        # Create the basic database configuration
        self.host = host
        self.login = login
        self.password = password
        self.database = database

        # Set the connected to false
        self.connected = False

        # Set the connection to None
        self.connection = None

        # We set the cursor to none
        self.cursor = None

    def connect_to_database(self):
        """
        Connect to database using current configuration
        :return:
        """
        # Try to connect to the database
        try:
            self.connection = mdb.connect(self.host, self.login, self.password, self.database)
        except:
            raise Exception("Unable to Connect to the Database")
        else:
            self.connected = True
            self.cursor = self.connection.cursor()

    def query_insert(self, table, columns, values):
        """
        Insert a new data into the table
        :param table: string table name
        :param columns:
        :param values:
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # First we set the query
        super().query_insert(table, columns, values)

        # Then we try to do the query
        self.query_without_result()

    def query_update(self, table, columns, values, where):
        """
        Update the table query
        :param table: string with table name
        :param columns: string/list with columns values
        :param values: string/list with values
        :param where: list with where statement
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # First we set the query
        super().query_update(table, columns, values, where)

        # Then we try to do the query
        self.query_without_result()

    def query_delete(self, table, where):
        """
        Delete query constructor
        :param table: string table
        :param where: list of where
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # First we set the query
        super().query_delete(table, where)

        # Then we try to do the query
        self.query_without_result()

    def query_select(self, table, columns, where=None, order=None, desc=True):
        """
        Query a selection of data
        :param table: string with table name
        :param columns: string/list with columns to be queried
        :param where: list with conditions for where
        :param order: string with the column name to order
        :param desc: boolean if the data should asc or desc
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # Then we proceed to create the query
        super().query_select(table, columns, where, order, desc)

        # Now we can get the result of the query
        result = self.query_with_result()

        # If we are selecting all columns
        if columns == "*":
            # Then we query the columns for the table
            columns = self.query_columns_names(table)

        # With the result and columns names we can create an array of dictionary with
        # the values we want
        return [{columns[j]: result[i][j] for j in range(len(columns))} for i in range(len(result))]

    def query_columns_names(self, table):
        """
        Query the columns from the table
        :param table:
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # We create the query
        super().query_columns(table)

        # Then we execute the query for the columns
        result = self.query_with_result()

        # Then we get the columns names
        return [r[0] for r in result]

    def query_without_result(self):
        """
        Try to do a query without returning a result
        :return:
        """
        try:
            self.cursor.execute(self.query)
        except:
            raise Exception("Fail to Execute Database Query")
        else:
            self.connection.commit()

    def query_with_result(self):
        """
        Try to do a query with a result
        :return:
        """
        try:
            self.cursor.execute(self.query)
        except:
            raise Exception("Fail to Execute Database Query")
        else:
            return self.cursor.fetchall()