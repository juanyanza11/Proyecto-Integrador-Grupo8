"""
			---------------------------
		----	||	ROYECTO INTEGRADOR	||----
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

Eliminando Duplicados
"""

import pandas as pd # Libreria manejo de datos

# Abrir el archivo como dataframe
data = pd.read_csv("data/ods_1_2_limpDef777.csv", sep =',', encoding = "utf-8")

#print(data.duplicated().sum()) #Imprime todos los duplicados
df = data.drop_duplicates('id_str')

df
print(df.duplicated().sum()) # Valida si tiene nulos = 0


#df.to_csv("ods_1_2_DEF.csv", index=False)

