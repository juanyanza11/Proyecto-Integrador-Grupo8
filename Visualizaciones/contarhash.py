"""
			---------------------------
			||	ROYECTO INTEGRADOR	||
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

"""

#Librerias utilizadas para manejo de datos

from functools import reduce
from itertools import *
from collections import Counter
import pandas as pd
data = pd.read_csv("data/data_hashtags.csv", sep = ";", encoding='latin-1')
#print(data)

data_record = data.to_dict("records")
#print(data_record[0].keys())

lista = list(map(lambda x: x['hashtags'],data_record))
#print(lista)

#print("--------------------------------")
# se obtiene las ocurrencias que más se repiten
lista_2 = Counter(lista).most_common(10) # CUenta los 10 hashtags que más se repiten
#print(lista_2)

# se pasa la lista a dataFrame
data = pd.DataFrame(lista_2)

# Guardamos el csv con pandas
data.to_csv("data/hashtags_count.csv", header=['hashtag', 'numero'], index=False)
