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
import math

data = pd.read_csv("data/data_users.csv", sep = ",", encoding = "utf-8")
data_record = data.to_dict("records")

lista1 = list(map(lambda x: x['user_followers_count'], data_record)) # Numero de seguidores
lista2 = list(map(lambda x: x['user_friends_count'], data_record)) # Numero de seguidos
mediaF = round(sum(lista1)/len(lista1)) # media seguidores
mediaFl = round(sum(lista2)/len(lista2)) # media seguidos

deF = list(map(lambda x: math.sqrt((x['user_followers_count'] - mediaF)**2/ len(x)), data_record))  # DESVIACION ESTANDAR X raiz
deFl = list(map(lambda x: math.sqrt((x['user_friends_count'] - mediaFl)**2/ len(x)), data_record))  # DESVIACION ESTANDAR Y raiz

#print(deF) # DESVIACION ESTANDAR X
#print(deFl) # DESVIACION ESTANDAR X

cov = (sum(lista1) * sum(lista2)) - (mediaFl * mediaF) /len(lista1) # ambos len son iguales || COVARIANZA(X,Y)

#cov = (sum(lista1) * sum(lista2)) - (mediaFl*mediaF)/len(lista1) # ambos len son iguales || COVARIANZA(X,Y)

ccp = cov/(sum(deF)*sum(deFl))
"""
print(lf)
print(len(lista1))
print(len(lista2))
print(cov)
"""
print(ccp)
print(math.sqrt(9))
