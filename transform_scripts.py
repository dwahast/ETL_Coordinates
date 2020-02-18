import multiprocessing
import geopy
import pandas as pd
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter

#https://developer.mapquest.com/user/me/apps
#mapquest
CONSUMER_KEY = 'zddGiPAGZEBPTSKYphGuIhSixhyWTcuJ'

df_columns = ["latitude","longitude","rua","numero","bairro","cidade","cep","estado","pais"]
geopy_columns = ["road","house_number","suburb","city","postcode","state","country"]


def transform_data(coordinates):    
    print("Transformando dados... \n--Aguarde, Requisições à API.")
    #Entrada: Lista com coordenadas agrupadas em listas [[coord1_lat,coord1_lng],[coord2_lat,coord2_lng]]
    #Sáida DataFrame pandas, com as informações obtidas de cada coordenada
    
    #Processo é paralelizada de acordo com as threads disponíveis, visando
    #obter melhor performance na obtenção das informações através da API
    
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    dict_temp = pool.map(get_location, coordinates)

    df_temp = pd.DataFrame(data=dict_temp)
    
    #Remove as linhas repetidas baseadas na latitudes e longitude, são removidas as linhas com menos valores
    df_temp['count'] = pd.isnull(df_temp).sum(1)
    df_temp = df_temp.sort_values(['count']).drop_duplicates(subset=['latitude','longitude'],keep='first').drop('count',1)
    df_temp.sort_index(inplace=True)
    
    #Remove as linhas as quais o subset é nulo.
    df_temp.dropna(subset=['pais','estado','cidade','bairro'], inplace=True)
    
    df_temp.set_index(['latitude','longitude'], inplace=True)
        
    return df_temp


def get_location(coord):
    
    dict_location = {}
    
    if (coord[0] != None) and (coord[1] != None):
        dict_location['latitude'] = coord[0].strip()
        dict_location['longitude'] = coord[1].strip()
    
        try:
            #https://developer.mapquest.com/user/me/apps
            geolocator = geopy.geocoders.OpenMapQuest(api_key=CONSUMER_KEY)
            RateLimiter(geolocator.reverse, min_delay_seconds=1)
            #geolocator = geopy.geocoders.GoogleV3(api_key = "") 
            location = geolocator.reverse(str(coord[0]) + ", " + str(coord[1]), timeout=10)

        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s"%(coord[0]+coord[1], e))

        for i in range(2,len(df_columns)):

            try:
                dict_location[df_columns[i]] = location.raw['address'][geopy_columns[i-2]]
            except:
                dict_location[df_columns[i]] = None
    
    return dict_location