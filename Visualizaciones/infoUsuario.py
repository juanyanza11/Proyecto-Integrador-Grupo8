
from functools import reduce
from itertools import *
from collections import Counter
import pandas as pd
data = pd.read_csv("data/ods_1_2_definitivo.csv", sep = ",", encoding='utf-8')
data_record = data.to_dict("records")

#  filtramos unicamente los ReTweets
retweet = list(map(lambda x: 'RT @' in x['textoNew'], data_record))
#  filtramos unicamente los Tweets
tweet = list(map(lambda x: 'RT @' != x['textoNew'][0:4], data_record))
listaRT = list(zip(retweet, tweet))

#  obtengo datos de usuario
listaUsuarios = list(map(lambda x: (x['from_user'], int(x['user_followers_count']), int(x['user_friends_count'])), data_record))


# creo la estructura que deseo junto si tiene o no tiene Tweet/Retweet
data1 = pd.DataFrame(listaUsuarios, columns=['from_user','user_followers_count','user_friends_count'])
data2 = pd.DataFrame(listaRT, columns = ['retweet','tweet'])
#  se concatenan los dataframes para asi crear un csv con los registros
dataFinal = pd.concat([data1, data2], axis = 1)

dataFinal.to_csv("data/data_infoUsu.csv", header=['from_user',\
	'user_followers_count','user_friends_count','retweet','tweet'], index=False)

