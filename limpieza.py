"""
			---------------------------
		----	||	ROYECTO INTEGRADOR	||----
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

"""
import pandas as pd # Importacion de libreria para manejo de datos csv
import datetime # Datetime usado para asignar la fecha del sistema 
fecha = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S') # Formato para la base de datos

data = pd.read_csv("data/ods_1_2_limpieza777.csv")
data.dtypes # Tipos de datos
data.keys() # Llaves o columnas
data.geo_coordinates.isnull().sum() # Registros de coordenadas que son campos nulos
data[data['geo_coordinates'].isnull()]

data.time.fillna(fecha, inplace=True) # Campos de time con nulos

data.loc[(data.time == 'en'),'time'] = fecha # Reemplazamos a los campos nulos la fecha del sistema en "en"

data.geo_coordinates.fillna('loc: 00.000,00.000', inplace=True) # Formato de coordenadas campos vacios 

data.in_reply_to_user_id_str.fillna(0, inplace=True) # Asignar 0 a los id que no tienen respuesta

data.in_reply_to_screen_name.fillna('', inplace=True) # Asignar vacio al nombre que aparece en tweet

data.in_reply_to_status_id_str.fillna(0, inplace=True) # Asignar 0 a los id que no tienen status

data.user_followers_count.fillna(0, inplace=True) # Asignar 0 a los que no tienen seguidores

data.user_friends_count.fillna(0, inplace=True) # Asignar 0 a los que no tienen seguidos

data.user_location.fillna('', inplace=True) # Asignar cadena vacia a user location

data.profile_image_url.fillna('', inplace=True) # Asignar cadena vacia a profile_image

data.status_url.fillna('', inplace=True) # Asignar cadena vacia a status

data.entities_str.fillna('', inplace=True) # Asignar cadena vacia entities_str

data.source.fillna('', inplace=True) # Asignar cadena vacia a source

data.from_user_id_str.fillna(0, inplace=True) # Asignar cadena from_user_id_str

data.user_lang.fillna('', inplace=True) # Asignar cadena vacia a user_lang

data.created_at.fillna('', inplace=True) # Asignar cadena vacia a profile_image

# Campos Nulos en ods_1_2
print(data.geo_coordinates.isnull().sum())

print(data.in_reply_to_user_id_str.isnull().sum())

print(data.in_reply_to_screen_name.isnull().sum())

print(data.in_reply_to_status_id_str.isnull().sum())

print(data.user_followers_count.isnull().sum())

print(data.user_friends_count.isnull().sum())

print(data.user_location.isnull().sum())

print(data.profile_image_url.isnull().sum())

print(data.status_url.isnull().sum())

print(data.entities_str.isnull().sum())

print(data.source.isnull().sum())

print(data.from_user_id_str.isnull().sum())

print(data.user_lang.isnull().sum())

print(data.time.isnull().sum())

print(data.created_at.isnull().sum())

# Columnas sin nulos

print(data.text.isnull().sum())

print(data.from_user.isnull().sum())

print(data.id_str.isnull().sum())

data.to_csv("ods_1_2_limpieza.csv", index=False)