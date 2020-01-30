
from functools import reduce
from itertools import *
from collections import Counter
import pandas as pd
data = pd.read_csv("data/ods_1_2_definitivo.csv", sep = ",", encoding='utf-8')
data_record = data.to_dict("records")

#  filtramos unicamente los ReTweets
texto = list(map(lambda x: 'RT @' in x['textoNew'], data_record))
#  filtramos unicamente los Tweets
texto2 = list(map(lambda x: 'RT @' != x['textoNew'][0:4], data_record))

#  obtengo datos de usuario
listaUsuarios = list(map(lambda x: ("%s,%d,%d")%(x['from_user'], \
	int(x['user_followers_count']), int(x['user_friends_count']), data_record))


# creo la estructura que deseo junto si tiene o no tiene Tweet/Retweet
listaFinal = list(zip(listaUsuarios,texto,texto2))


listaCant = list(map(lambda x: [x[0], list(x[1])], 
	groupby(data_record, lambda x: x[])))


lista777 = Counter(listaFinal)
print() 

"""
dataFinal = pd.DataFrame(listaUsuarios, columns=['from_user','user_lang', 'from_user_id_str', \
	'profile_image_url','user_followers_count','user_friends_count', 'user_location'])
	"""