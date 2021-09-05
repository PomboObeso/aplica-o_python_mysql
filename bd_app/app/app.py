import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:1234@localhost:3306/tenis')

dw = pd.read_sql_table('tenis.tenista',engine)

dw.head()

def lerTenistasAtivoDB():   
    # carrega e atribui a uma variavel a query feita.   
    df = pd.read_sql("SELECT * FROM tenista WHERE esta_ativo = 1",engine, columns=["nome","apelido","ano_nasc"])
    # mostra os itens buscados atraves da query acima
    df.head()

def inserirTenistaDB():
    script_insert = """
                    INSERT INTO tenista 
                        (id,nome, apelido, ano_nasc, cidade_nascimento, cidade_moradia, esta_ativo,id_padrinho) 
                    VALUES 
                        (8,'Ana', 'Aninha', 1999, 'Tatuapé','Ingá',1,3),
                        (9,'Maria Clara', 'Clarinha', 1998, 'Junqueiro','Arapiraca',1,1),
                        (10,'Virginio', 'Vini', 1972, 'Campo dos Jordão','Jaboatão',1,4),
                        (11,'Reginaldo', 'Naldo', 1969, 'João Pessoa','Fortaleza',1,2),
                        (12,'Arthur', 'Arturito', 1996, 'Porto Alegre','Bagé',1,5);  
                    """
    pd.insert_sql(script_insert, engine)
    pd.commit()
def removeTenistaDB():
    script_remove = """
                    DELETE FROM torneio WHERE id = 5;                    
                    """

    pd.remove_sql(script_remove)
    pd.commit()                

def torneiosDisputadoTenista():
    script_all ="""
                SELECT nome, count(nome) AS 'torneios_jogados' FROM \
                    tenista, participar WHERE id = id_tenista GROUP BY nome;
                """
    df = pd.read_sql_query(script_all,engine)
    df.head()
    
def idadeRolandGarros():

    script_age ="""
                SELECT DISTINCT nome, 2021 - ano_nasc AS idade \
                    FROM tenis.tenista, tenis.participar \
                    WHERE id = id_tenista AND id_torneio = 4;
                """
    df = pd.read_sql_query(script_age, engine)
    df.head()


lerTenistasAtivoDB()
inserirTenistaDB()
removeTenistaDB()
torneiosDisputadoTenista()
idadeRolandGarros()