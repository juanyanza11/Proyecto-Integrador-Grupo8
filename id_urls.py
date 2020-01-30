"""
			---------------------------
		----	||	ROYECTO INTEGRADOR	||----
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

--> CSVs auxiliares URLS <--
"""

"""

	librerias que necesitamos para menejo de entities_str

"""
import pandas as pd
import json 
data = pd.read_csv("data/ods_1_2.csv", sep = ",")

data2 = data[['id_str','entities_str']]
dataFinal = data2.to_dict("records")
#print(dataFinal)

# Lista compresa que lo recorre por cada linea
lista = [{'id_str': l['id_str'], 'entities_str':json.loads(l['entities_str'])} for l in dataFinal if l["entities_str"].__class__ is str]
#print(lista)

# Columna entities con el JSON
entidades = list(map(lambda x: x['entities_str'], lista))

# Objeto URLS
urls = list(map(lambda x: x['urls'], entidades))

# id_str para relacionar con la tabla TWEETs
id_str = list(map(lambda x: x['id_str'], lista))

# Unión de id con entidades
union = list(zip(id_str, urls))
#print(entidades)

archivo = open("data/data_url.csv","a", encoding="utf-8")
# Encabezados para BD

archivo.write("%s;%s\n"%("ids","url"))#,"media_url_https","expanded_url","display_url","url","type"))
# Accedemos a la union con zip, al objeto media y abstraemos las llaves con un for
for l in union:
	for x in l[1]:
		archivo.write("%s;%s\n"%(l[0], x['url']))
archivo.close()

#print(urls)
