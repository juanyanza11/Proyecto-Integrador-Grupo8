"""
			---------------------------
		----	||	ROYECTO INTEGRADOR	||----
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

"""

#librerias que necesitamos para menejo de entities_str

import pandas as pd
import json 
data = pd.read_csv("ods_1_2_definitivo.csv", sep = ",", encoding = "utf-8") # Abriendo el csv como dataframe

data2 = data[['id_str','entities_str']] # obtenemos id_str con entities_str para incorporar con el modelo BD
dataFinal = data2.to_dict("records") # Transformamos a diccionario el DF
#print(dataFinal)

# Lista compresa que lo recorre por cada linea
lista = [{'id_str': l['id_str'], 'entities_str':json.loads(l['entities_str'])} for l in dataFinal if l["entities_str"].__class__ is str]

#print(lista)

# Columna entities con el JSON
entidades = list(map(lambda x: x['entities_str'], lista))
# Objeto Hashtag
hashtags = list(map(lambda x: x['hashtags'], entidades))
# id_str para relacionar con la tabla TWEETs
id_str = list(map(lambda x: x['id_str'], lista))
# Unión de id con objeto hashtags
union = list(zip(id_str, hashtags))
#print(union[1])

archivo = open("data/data_hashtags.csv","a")

# Encabezados para BD
archivo.write("%s;%s\n"%("ids", "hashtags"))
for l in union:
	for x in l[1]:
		cadena = [l[0], x['text']]
		# Exporta todos los ids con los hashtags de un tweet
		archivo.write("%s;%s\n"%(l[0], x['text'])) 
archivo.close()
