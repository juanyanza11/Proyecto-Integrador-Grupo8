"""
			---------------------------
			||	ROYECTO INTEGRADOR	||
			---------------------------

Docente: Rene Elizalde
Integrantes: - Roberto Narvaez
			 - Juan Yanza

Se obtiene Los tweets y retweets por dia
"""
#  lista de bibliotecas utilizadas
from collections import Counter
import pandas as pd
import datetime
#  se lee el dataset y se lo trata como diccionario
data = pd.read_csv("data/ods_1_2_definitivo.csv", sep = ",", encoding = "utf-8")
data_record = data.to_dict("records")
#  filtramos unicamente los Retweets
texto = list(filter(lambda x: 'RT @' in x['textoNew'], data_record))
#  filtramos unicamente los Tweets
texto2 = list(filter(lambda x: 'RT @' != x['textoNew'][0:4], data_record))

#  se obtiene datos de unicamente tweets
listaTweet = list(map(lambda x: x['time'],texto2)) 
fechasTweet = list(map(lambda x:datetime.datetime.strptime(\
	str(x), '%d/%m/%Y %H:%M:%S'),listaTweet))
fechasT = list(map(lambda x:x.day, fechasTweet))



#  se obtiene datos de unicamente Retweets
listareTweet = list(map(lambda x: x['time'],texto)) 
fechasreTweet = list(map(lambda x:datetime.datetime.strptime(\
	str(x), '%d/%m/%Y %H:%M:%S'),listareTweet))
fechasreT = list(map(lambda x:x.day, fechasreTweet))

# se obtiene las ocurrencias que más se repiten
reTweet = Counter(fechasreT).items() 
tweet = Counter(fechasT).items() 

# se pasan las lista a dataFrame
data1 = pd.DataFrame(reTweet)
data2 = pd.DataFrame(tweet)

#  creacion de archivos
data1.to_csv("data/data_diasreTweet.csv", header=['dia', 'numero'], index=False)
data2.to_csv("data/data_diasTweet.csv", header=['dia', 'numero'], index=False)
