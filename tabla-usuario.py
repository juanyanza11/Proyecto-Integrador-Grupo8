"""
			---------------------------
		----	||	ROYECTO INTEGRADOR	||----
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

--> AUXILIAR TABLA USUARIOS --<
"""

import pandas as pd
data = pd.read_csv("ods_1_2_definitivo.csv", sep = ",", encoding = "utf-8")
data_record = data.to_dict("records")

# Lista con todas las entidades para la tabla USUARIO DE BD
listaUsuarios = list(map(lambda x: [x['from_user'], x['user_lang'], x['from_user_id_str'], \
	x['profile_image_url'], int(x['user_followers_count']), int(x['user_friends_count']), x['user_location']], data_record))

# La lista la pasamos a dataframe para poder exportarla como .csv
dataFinal = pd.DataFrame(listaUsuarios, columns=['from_user','user_lang', 'from_user_id_str', \
	'profile_image_url','user_followers_count','user_friends_count', 'user_location'])


# Eliminamos los usuarios duplicados
df = dataFinal.drop_duplicates('from_user')

# Definimos el encabezado para BD
df.to_csv("data/data_users.csv", header=['from_user','user_lang', 'from_user_id_str', \
	'profile_image_url','user_followers_count','user_friends_count', 'user_location'], index=False)