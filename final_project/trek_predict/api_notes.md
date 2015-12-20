## Trek Stuff

|Series|IMDb ID|Dates|Seasons|
```
tos = '0060028', '66'-'69', 3
tng : '0092455', '87'-'94', 7
ani : '0069637', '73'-'75', 1
ds9 : '0106145', '93'-'99', 7
voy : '0112178', '95'-'01', 7
ent : '0244365', '01'-'05', 4
```
# IMDbPY  
- Source - http://sourceforge.net/p/imdbpy/  

# Rotten Tomatoes
- Source - https://github.com/zachwill/rottentomatoes  

#Hulu ?
- Source - https://github.com/michaelhelmick/hulu
import imdb
import time as t
import numpy as np
import pandas as pd

tos = '0060028', '66'-'69', 'done'
tng = '0092455', '87'-'94', 'done'
ani = '0069637', '73'-'75', 'done'
ds9 = '0106145', '93'-'99', 'done'
voy = '0112178', '95'-'01', 'done'
ent = '0244365', '01'-'05', ''
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
