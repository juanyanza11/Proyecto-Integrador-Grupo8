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
data = pd.read_csv("ods_1_2_definitivo.csv", sep = ",", encoding = "utf-8")

# obtenemos id_str con entities_str para incorporar con el modelo BD
data2 = data[['id_str','entities_str']]

# Transofrmamos de DF a diccionario
dataFinal = data2.to_dict("records")

#print(dataFinal)
lista = [{'id_str': l['id_str'], 'entities_str':json.loads(l['entities_str'])} for l in dataFinal if l["entities_str"].__class__ is str]

#print(lista)

# Columna entities con el JSON
entidades = list(map(lambda x: x['entities_str'], lista))

# Objeto user_mentions
user_mentions = list(map(lambda x: x['user_mentions'], entidades))

# id_str para relacionarlo en BD
id_str = list(map(lambda x: x['id_str'], lista))

# Unión de id con objeto hashtags
union = list(zip(id_str, user_mentions))

#print(entidades)
archivo = open("data/data_user_men.csv","a", encoding="utf-8")
archivo.write("%s\t%s\t%s\t%s\n"%("ids", "screen_name","name","id_mentions"))
for l in union:
	for x in l[1]:
		archivo.write("%s\t%s\t%s\t%s\n"%(l[0], x['screen_name'],x['name'],x['id']))
archivo.close()
