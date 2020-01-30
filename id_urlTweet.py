"""
			---------------------------
		----	||	ROYECTO INTEGRADOR	||----
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

--> AUXILIAR URLS TWEET <--
"""


#librerias que necesitamos para menejo de entities_str
import pandas as pd
import json 
data = pd.read_csv("ods_1_2_definitivo.csv", sep = ",", encoding = "utf-8")

data2 = data[['id_str','entities_str']]
dataFinal = data2.to_dict("records")
#print(dataFinal)

# Lista compresa que lo recorre por cada linea
lista = [{'id_str': l['id_str'], 'entities_str':json.loads(l['entities_str'])} for l in dataFinal if l["entities_str"].__class__ is str]
# Lista compresa que lo recorre por cada linea

# Columna entities con el JSON
entidades = list(map(lambda x: x['entities_str'], lista))

# id_str para relacionar con la tabla TWEETs
id_str = list(map(lambda x: x['id_str'], lista))

# Unión de id con entidades
union = list(zip(id_str, entidades))

archivo = open("data/auxiliar_urlTweet.csv","a")

# Encabezados para BD
archivo.write("%s;%s;%s;%s\n"%("ids_str","url", "expanded_url", "display_url",))

for l in union:
	enti = l[1]
	if 'media' in enti.keys():
		for x in enti['urls']:
			archivo.write("%s;%s;%s;%s\n"%(l[0], x['url'],x['expanded_url'],\
				x['display_url'],))
			
archivo.close()