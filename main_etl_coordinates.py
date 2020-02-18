from db_scripts import print_table_db, get_connection_db, append_df_in_db, load_data
from extract_scripts import extract_data, extract_lat_lng
from transform_scripts import get_location, transform_data

import pandas as pd
import multiprocessing
import glob
import time

#Caminho onde se encontram os arquivos .txt contendo as informações de coordenadas
path_master='../ETL_Coordinates/Arquivos Extração'

files = [f for f in glob.glob(path_master + "**/*.txt", recursive=True)]

if len(files) > 0:
    print("\nProcesso de ETL iniciado:\n\n")
    files.sort()

    start = time.time()

    #O processo de extração tem como parametro uma lista de caminho de arquivos
    #a serem extraidas as coordenadas, retornando uma lista com todas as coordenadas
    #de todos os arquivos passados inicialmente (esse processo é feito paralelamente)
    coordinates = extract_data(files)

    #O processe de transformação dos dados tem como parametro a lista de coordenadas
    #as quais serão obtidas as informações como rua, bairro, etc. retornando um dataframe pandas
    df_locations = transform_data(coordinates)

    #O processo de carregamento é feito através da inserção do dataframe em uma tabela prédefinida
    #onde são adicionados os dados ao fim da tabela se ela já existe como também criando a tabela caso não.
    #Esse código pode ser executado diversas vezes com arquivos diferentes como uma única vez com todos os arquivos.
    load_data(df_locations)

    end = time.time()
    
    tempo_total = end - start
    if(float() > 60.0):
        print("\n\nTempo total decorrido:",tempo_total / 60,"m")
    else:
        print("\n\nTempo total decorrido:",tempo_total,"s")

else:
    print("Nenhum arquivo encontrado.")

    