"""
			---------------------------
			||	ROYECTO INTEGRADOR	||
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza
Limpieza saltos de línea

"""

import pandas as pd
data = pd.read_csv("ods_1_2_limpieza.csv", sep = ",", encoding = "utf-8") # Abriendo el csv con pandas (dataframe)
data_record =data.to_dict("records") # Transformando el dataframe en diccionario
# 
texto = list(map(lambda x: x["text"], data_record)) # Llave de text "tweet como tal"

texto2 = list(map(lambda x: x.replace('\r', ''), texto)) # Casos con salto de linea o tab

# Cuando exista un salto de linea, dos incluso tres

textoFinal = list(map(lambda x: x.replace('\n', '') or x.replace('\n\n', '')\
 or x.replace('\n\n\n', ''), texto2))

print(textoFinal[0])

data['textoNew'] = textoFinal # Creamos la columna con el nuevo text
del data['text'] # Borramos el text que contenia saltos de linea innecesarios

data.to_csv("data777.csv", index=False)
