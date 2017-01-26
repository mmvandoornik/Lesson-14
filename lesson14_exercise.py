from twython import Twython
import simplekml
import json
import datetime
import os

#set working directory
os.chdir('./data')

##codes to access twitter API. 
APP_KEY = 'FQgxCbYykk3TkXOd60mBCzUNU'
APP_SECRET = '3qH3krvM6jPNNGLjALEgKMwTnT5EpOLLML5eScBAdiQ2dFQpvv'
OAUTH_TOKEN = '824525944048193537-RVQJ92Xma1P0YAFc9plCrlggvjMvPt2'
OAUTH_TOKEN_SECRET = 'av7ljuUR63ATJf4enCjY8hMCwUHxYzYpZtWD1LRMrxZfV'

##initiating Twython object 
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Tweets are searched 3 km around Heathrow Airport with the keyword 'goodbye'. This gave only 2 results. 
search_results = twitter.search(q='goodbye', geocode='51.4775,-0.4613888888888889,3km')

## The search results are written to a tab deliited CSV file and the coordinates are added to a list
coordlist = []
for tweet in search_results["statuses"]:
    username =  tweet['user']['screen_name']
    tweettext = tweet['text'] 
    coordinates = tweet['coordinates']
    if coordinates != None:
        coord = coordinates['coordinates']
    output_file = 'result.csv' 
    target = open(output_file, 'a')    
    print username
    target.write(username)
    target.write('\t')
    print tweettext
    target.write(tweettext.encode("utf-8"))
    target.write('\t')
    if coordinates != None:
        print coord
        target.write(str(coord))
        coordlist += [coord]
    target.write('\n')
    print '==========================='
target.close()

#a function is made to make a KML file from the coordinates of a list of lists
def makeKML(locations):
    kml = simplekml.Kml()
    for i in locations:
        kml.newpoint(coords=[(i[0],i[1])])
    kml.save("tweets.kml")

# the KML file is created for the tweets that were searched
makeKML(coordlist)