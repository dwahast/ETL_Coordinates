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
  - Após a instalação do Servidor Postgres é necessário a criação do Database e de um Usuário de acesso, o qual deve ser inserido no código na chamada da função get_connection_db(), onde está especificado a nomenclatura dos parâmetros.
    
  ### Criando o DB
  - https://www.fullstackpython.com/blog/postgresql-python-3-psycopg2-ubuntu-1604.html
  - $ createdb testeiris

  ### Criando novo usuário (default: user:douglas, password:123)
  - $ sudo -i -u postgres ou $sudo -u postgres psql
  - $ createuser [novo usuario] -P --interactive

  ### Execução do código
  - Após terem sido satisfeitas as etapas anteriores, para a etapa de execução do código, é necessária a identificação do diretório contendo os arquivos ".txt" onde de todos os arquivos, desse formato, presentes no diretório informado na váriavel path_master serão extraídas as informações de coordenadas.
  
  
