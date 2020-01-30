"""
			---------------------------
		----	||	ROYECTO INTEGRADOR	||----
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza
obtener numero de media en cada Tweet
"""
import pandas as pd
import json 
from itertools import *
from collections import Counter
data = pd.read_csv("data/ods_1_2_definitivo.csv", sep = ",", encoding = "utf-8")

data2 = data[['id_str','entities_str']]
dataFinal = data2.to_dict("records")
#print(dataFinal)
lista = [{'id_str': l['id_str'], 'entities_str':json.loads(l['entities_str'])} for l in dataFinal if l["entities_str"].__class__ is str]

entidades = list(map(lambda x: x['entities_str'], lista))

listaEntidades = list(map(lambda x: 'media' in x, entidades))


#  contabilizo los registros con o sin media
listaFinal = Counter(listaEntidades)


#  creo el archivo y le escribo los datos obtenidos
archivo = open("data/data_ContMedia.csv", "a")
archivo.write("Numero,Medias\n")
archivo.write("1,%s\n2,%s"%(listaFinal[0],listaFinal[1]))
