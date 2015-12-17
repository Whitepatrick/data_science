from imdb import IMDb
import pandas as pd
import numpy as np
import time as t

ia = IMDb('http')
sp = ia.get_movie('0092455')
ia.update(sp, 'episodes rating')
#print sp.get('episodes rating')
#print sp[1]

key_words = ia.get_movie_infoset()
for word in key_words:
    print word
    t.sleep(1)
