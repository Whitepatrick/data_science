import imdb
import json

ia = imdb.IMDb()
show = ia.get_movie('0244365')
ia.update(show, 'episodes')
show_seasons = show['episodes']

def get_ratings(season_i):
    ratings = {}
    for key, value in season_i.iteritems():
        ia.update(value)
        ratings[key] = value.get('rating')

    return ratings

show_ratings = {}
for i in range(1, len(show_seasons) + 1):
    season_key = "season_" + str(i)
    show_ratings[season_key] = get_ratings(show_seasons[i])

print show_ratings
#with open('st_ent.json', 'w') as fp:
#    json.dump(show_ratings, fp)

#def get_ratings(season_hash):
#    season_hash
#    for key, value in season_hash.iteritems():
#        ia.update(value)
#        ratings[key] = value.get('rating')

#all_ratings = {}
#for season in show_seasons:
#    season_ratings = get_ratings(season)
#    all_ratings[season] = season_ratings

#print all_ratings
