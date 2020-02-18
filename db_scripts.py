import psycopg2
from sqlalchemy import create_engine


def print_table_db(table):
    conn = get_connection_db()
    try:
        rows = conn.execute('SELECT * FROM {};'.format(table))
        for n,r in enumerate(rows):
            print(n,r)
    except:
        print("Tabela nao existe")


def remove_df_db_dup(df,db_rows):
    print("--Removendo duplicados presentes no dataframe e database...")
    for i in db_rows:
        try:
            df = df.drop((i[0],i[1]))
        except Exception:
            pass

    return df

def get_connection_db(host_ = 'localhost', dbname_ = 'testeiris', user_ = 'douglas', password_ = '123'):
    try:
        return create_engine(
            'postgresql+psycopg2://{}:{}@{}/{}'.format(user_,password_,host_,dbname_)
            )

    except Exception as e:
        print(e)
        return None


def append_df_in_db(df,conn):
    try:
        df = remove_df_db_dup(df,conn.execute("SELECT * FROM locations"))
        df.to_sql('locations', con = conn, if_exists = 'append', chunksize = 1, index=True)
        print("--Adicionado Novos Valores na Tabela.")
    except:
        try:
            df.to_sql('locations', con = conn, if_exists = 'append', chunksize = 1, index=True)
            conn.execute('ALTER TABLE locations ADD PRIMARY KEY (latitude, longitude);')
            print("--Primeira inserção de valores na tabela.")
        except Exception as e:
            print("--Exeception message:\n",e)

def load_data(df):
    print("Carregando dados no DB...")
    #para utilização é necessário ter um DB.
    #os paramentros de conexão ao DB "get_connection_db(parametros)" podem ser alterados
    #host_ = 'localhost', dbname_ = 'testeiris', user_ = 'douglas', password_ = '123'
    conn = get_connection_db()
    append_df_in_db(df, conn)
    conn.dispose()
