"""
			---------------------------
			||	ROYECTO INTEGRADOR	||
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza
Se obtienen la distirbucion de URLs
"""
"""
			---------------------------
			||	ROYECTO INTEGRADOR	||
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

Se obtiene Los urls mas comunes
"""
#  lista de librerias utilizadas
from functools import reduce
from itertools import *
from collections import Counter
import pandas as pd

# Lectura de archivo 
data = pd.read_csv("data/data_url.csv", sep = ";", encoding='utf-8')
data_record = data.to_dict("records")

# Extracción de columna hashtags
lista = list(map(lambda x: x['url'],data_record))

# Se obtienen los 10 hashtags más usados
listaFinal = Counter(lista).most_common(10) 

# Conversion de lista a DataFrame
data1 = pd.DataFrame(listaFinal)

# Exportación de archivo csv
data1.to_csv("data/data_urlVis.csv", header=['url', 'numero'], index=False)