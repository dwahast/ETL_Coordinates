import multiprocessing

def extract_data(files):
    print("Extraindo Dados...")
    #Entrada: Lista de caminhos de arquivos para leitura
    #Saída: Lista com todas coordenadas de todos os arquivos lidos
    
    #lança para o maior número de processos possíveis para se tornar mais eficiente para leitura de diversos arquivos 
    #***cada thread assume um arquivo***
    
    coordinates = []
    
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    coordinates_temp = pool.map(extract_lat_lng, files)
    
    for f in coordinates_temp:
        coordinates += f
        
    print("--Número de Coordendas total", len(coordinates))

    return coordinates
    

def extract_lat_lng(file):
    
    f = open(file,'r')
    
    coord = []
    lat = None
    lng = None
    
    for line in f:
        
        if ("Latitude" in line) and lat == None:
            #Talvez essa solução não seja a mais segura (utilizar o S para dividir a linha)
            lat = line.split("S")[1].split("\n")[0]
        if ("Longitude" in line) and (lng == None):
            #Talvez essa solução não seja a mais segura (utilizar o W para dividir a linha)
            lng = line.split("W")[1].split("\n")[0]
            
            coord.append([lat,lng])
            
            lat = None
            lng = None

    print("--Finished Path:",file)
    
    return coord