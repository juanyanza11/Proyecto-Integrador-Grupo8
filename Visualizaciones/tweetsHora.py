from collections import Counter
import pandas as pd
import datetime

data = pd.read_csv("data/ods_1_2_definitivo.csv", sep = ",", encoding = "utf-8")
data_record = data.to_dict("records")

texto = list(filter(lambda x: 'RT @' in x['textoNew'], data_record))

texto2 = list(filter(lambda x: 'RT @' != x['textoNew'][0:4], data_record))

#  se obtiene datos de unicamente Retweets
listaTweet = list(map(lambda x: x['time'],texto2)) 
fechasTweet = list(map(lambda x:datetime.datetime.strptime(str(x), '%d/%m/%Y %H:%M:%S'),listaTweet))
fechasT = list(map(lambda x:x.hour, fechasTweet))



#  se obtiene datos de unicamente Retweets
listareTweet = list(map(lambda x: x['time'],texto)) 
fechasreTweet = list(map(lambda x:datetime.datetime.strptime(str(x), '%d/%m/%Y %H:%M:%S'),listareTweet))
fechasreT = list(map(lambda x:x.hour, fechasreTweet))

# se obtiene las ocurrencias que más se repiten
reTweet = Counter(fechasreT).items() 
tweet = Counter(fechasT).items() 

# se pasa la lista a dataFrame
data1 = pd.DataFrame(reTweet)
data2 = pd.DataFrame(tweet)

#  creacion de archivos
data1.to_csv("data/data_horasreTweet.csv", header=['hora', 'numero'], index=False)
data2.to_csv("data/data_horasTweet.csv", header=['hora', 'numero'], index=False)