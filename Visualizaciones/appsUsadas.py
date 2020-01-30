"""
			---------------------------
			||	ROYECTO INTEGRADOR	||
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza
Se obtienen las 10 Apps mas utilizadas
"""
#  lista de librerias utilizadas
import pandas as pd
from collections import Counter
#  se lee el dataset y se lo trabaja como diccionario 
data = pd.read_csv("data/ods_1_2_DEF.csv", sep = ",", encoding = "utf-8")
data_record =data.to_dict("records")
#  se obtiene unicamente datos de la columna que deseamos
source = list(map(lambda x: x['SourceNew'], data_record))

#  Cuenta los datos de source y los 10 mas altos los obtiene
lista = Counter(source).most_common(10)
#  almacenos datos en data
data = pd.DataFrame(lista)
print(data)

#  creamos archivo .csv
data.to_csv("data/data_apps.csv", header=['Apps', 'Numero'], index=False)