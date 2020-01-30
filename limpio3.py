"""
			---------------------------
			||	ROYECTO INTEGRADOR	||
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza
Sacar las plataformas de twitter eliminando <a href> y <a>

"""

import pandas as pd # Libreria para manejo de datos

data = pd.read_csv("data/data777.csv", sep = ",", encoding = "utf-8")
data_record =data.to_dict("records") # De dataframe a diccionario 

source = list(map(lambda x: x['source'], data_record)) # Ingresamos a la columna Source
source1 = list(map(lambda x: x.split(">"),source)) # Separamos todo lo que tenga > en cadena
source2 = list(map(lambda x: x[1],source1)) # Cadenas 'Twitter for Android</a'
source3 = list(map(lambda x: x.split("<"),source2)) # Elimina </a
sourceFinal = list(map(lambda x: x[0],source3)) # ["Twitter for android", "</a"]

#print(sourceFinal)

del data['source']

data['SourceNew'] = sourceFinal # Agregamos el nuevo source al dataframe
data.to_csv('ods_1_2_limpieza777.csv', index = False) # Transformamos a csv y exportamos