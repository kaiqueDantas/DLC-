'''def estudo():
    from Connetion import Dba
    valor = Dba.estudo()
    valor.setValor('hahah')
    print(valor.getValor())'''

if __name__ == '__main__':
    from Connetion import testing
    connection = testing.dba()
    #connection.insert()

    print(str(connection.select()))


