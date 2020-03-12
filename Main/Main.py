'''def estudo():
    from Connetion import Dba
    valor = Dba.estudo()
    valor.setValor('hahah')
    print(valor.getValor())'''
if __name__ == '__main__':
    from Connetion import testing
    conenect = testing.dba()
    conenect.select()
    conenect.close()


def create():

    '''Função destinada a passar a query para a função da classe dba '''

    query = '''CREATE TABLE id_dlc (
    id_dlc int (100000)not null ,
    tipo int (100) not null);
    
    create table dlc (
	    id_dlc int not null,
        cod_dlc int not null,
        nome_dlc int not null); 
        '''
    conenect = testing.dba()
    conenect.create(query)
    conenect.close()








