# ETL_Coordinates
Extraindo coordenadas de um arquivo .txt, obtendo informações sobre essas coordenadas e carregando-as em um DB.

# Informações
  ## Bibliotecas  
  ### Postgres 11
  - https://www.postgresql.org/download/linux/ubuntu/
  - $ sudo apt-get install postgresql-11
  
  ### Python SQL script (ddl)
  - $ sudo apt-get install libpq-dev
  - $ sudo apt-get install python-psycopg2
  - $ pip3 install sqlalchemy

  ### API para Reverse Geocoding
  - geopy
  - mapquest (https://developer.mapquest.com/user/me/apps)
  
  ### Para uso geral
  - Pandas
  - glob
  - multiprocessing
  - time
    
  ## Passo a passo
  
  ### Criando o DB
  - https://www.fullstackpython.com/blog/postgresql-python-3-psycopg2-ubuntu-1604.html
  - $ createdb testeiris

  ### Criando novo usuário (padrão: postgres)
  - $ sudo -i -u postgres ou $sudo -u postgres psql
  - $ createuser [novo usuario] -P --interactive

  
