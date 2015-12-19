import imdb
import time as t
import numpy as np
import pandas as pd
#tng series movie id '0092455'
# 7 seasons total
# episode count is 1:25, 2:22, 3:26, 4:26, 5:26, 6:26, 7:26
# tv ratings thread - http://sourceforge.net/p/imdbpy/mailman/message/25376790/
# docs w/ tv stuff - http://imdbpy.sourceforge.net/docs/README.series.txt

ia = imdb.IMDb()
tng = ia.get_movie('0092455')
# returns dict with {season: ep_1, ep_2, .., ep_n}
ia.update(tng, 'episodes')
seasons = tng['episodes']

season_1 = seasons[1]
season_2 = seasons[2]
season_3 = seasons[3]
season_4 = seasons[4]
season_5 = seasons[5]
season_6 = seasons[6]
season_7 = seasons[7]

ratings = {}
for key, value in season_1.iteritems():
    ia.update(value)
    ratings[key] = value.get('rating')

for key, value in ratings.iteritems():
    print key, value

#for key, value in season_1.iteritems():
#    ia.update(value)
#    print value.get('rating')
