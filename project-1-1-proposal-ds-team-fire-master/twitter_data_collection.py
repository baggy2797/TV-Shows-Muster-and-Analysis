import pymongo
#from pymongo import collection as Collection
from pymongo import MongoClient
import json
import twitter  
import tweepy

count = 2000

CONSUMER_KEY = 'TLMs4TpJ1rv1YGFAXE1lqm86b'

CONSUMER_SECRET = 'HgxcdW0A7lRkOiHsIVcK0gNcraIlLNcgxdhc1uQCasOsSAwjAi'

OAUTH_TOKEN = '243476385-vsivQzot5ndxNenbI6hJZJbFXgaSfECLSwmfUNnS'

OAUTH_TOKEN_SECRET = 'ODTaYpD24DCyV1BmVG2CXwNml8PZbPnqO7qNlcSjW0wdM'


auth = twitter.oauth.OAuth(OAUTH_TOKEN,
                            OAUTH_TOKEN_SECRET,
                            CONSUMER_KEY,
                            CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

api = tweepy.API(auth)

#Opening the mongo client
client = MongoClient()

#initializing the database
database = client.A_new_final



#sample lists
sample_emilyinparis = []
sample_theblacklist = []
sample_thecrown = []
sample_thebossbabybackinbusiness = []
sample_Scam1992OnSonyLIV = []
sample_mirzapur2 = []
sample_mandalorian = []
sample_biggboss14 = []
sample_ateacher = []
sample_greysanatomy = []
sample_thequeensgambit = []
sample_youngsheldon = []
sample_thewalkingdead = []
sample_theoffice = []
sample_schittscreek = []
sample_ToTheLake = []
sample_TheHauntingofBlyManor = []
sample_Barbarians = []
sample_LuciferNetflix = []
sample_Friends25 = []

#emptylist for the show
global_list_emilyinparis = []
global_list_greysanatomy = []
global_list_theblacklist = []
global_list_thecrown = []
global_list_thebossbabybackinbusiness = []
global_list_Scam1992OnSonyLIV = []
global_list_mirzapur2 = []
global_list_mandalorian = []
global_list_biggboss14 = []
global_list_ateacher = []
global_list_thequeensgambit = []
global_list_youngsheldon = []
global_list_thewalkingdead = []
global_list_theoffice = []
global_list_schittscreek = []
global_list_ToTheLake = []
global_list_TheHauntingofBlyManor = []
global_list_Barbarians = []
global_list_LuciferNetflix = []
global_list_Friends25 = []

#tweet_cursor = theoffice_final.find()

#print(tweet_cursor.count())

#user_cursor = theoffice_final.distinct("user.id")
#print(len(user_cursor))



#1)emilyinparis

#################################################################################################################################
#Name of the show
q = "#EmilyInParis"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_emilyinparis.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue
    


for i in range( len(global_list_emilyinparis)) : 
    sample_emilyinparis.append({ 'created_at':global_list_emilyinparis[i]['created_at'],
                    'id':global_list_emilyinparis[i]['id'],
                    'id_str':global_list_emilyinparis[i]['id_str'],
                    'text' : global_list_emilyinparis[i]['text'],
                    'source' : global_list_emilyinparis[i]['source'],
                    'user' : global_list_emilyinparis[i]['user'],
                    'coordinates' : global_list_emilyinparis[i]['coordinates'],
                    'place' : global_list_emilyinparis[i]['place'],
                    'retweet_count' : global_list_emilyinparis[i]['retweet_count'],
                    'favorite_count' : global_list_emilyinparis[i]['favorite_count'],
                    'entities': global_list_emilyinparis[i]['entities'],
                    'favorited' : global_list_emilyinparis[i]['favorited'],
                    'retweeted' : global_list_emilyinparis[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
eip = database.emilyinparis


eip.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_emilyinparis)) :
    try:
        holder = sample_emilyinparis[i]
        #Sending the tweet to the collection
        eip.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue


#2)greysanatomy

#################################################################################################################################

#Name of the show
q = "#GreysAnatomy"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_greysanatomy.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_greysanatomy)) : 
    sample_greysanatomy.append({ 'created_at':global_list_greysanatomy[i]['created_at'],
                    'id':global_list_greysanatomy[i]['id'],
                    'id_str':global_list_greysanatomy[i]['id_str'],
                    'text' : global_list_greysanatomy[i]['text'],
                    'source' : global_list_greysanatomy[i]['source'],
                    'user' : global_list_greysanatomy[i]['user'],
                    'coordinates' : global_list_greysanatomy[i]['coordinates'],
                    'place' : global_list_greysanatomy[i]['place'],
                    'retweet_count' : global_list_greysanatomy[i]['retweet_count'],
                    'favorite_count' : global_list_greysanatomy[i]['favorite_count'],
                    'entities': global_list_greysanatomy[i]['entities'],
                    'favorited' : global_list_greysanatomy[i]['favorited'],
                    'retweeted' : global_list_greysanatomy[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
ga = database.greysanatomy


ga.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_greysanatomy)) :
    try:
        holder = sample_greysanatomy[i]
        #Sending the tweet to the collection
        ga.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#3)theblacklist

#################################################################################################################################

#Name of the show
q = "#TheBlacklist"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_theblacklist.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_theblacklist)) : 
    sample_theblacklist.append({ 'created_at':global_list_theblacklist[i]['created_at'],
                    'id':global_list_theblacklist[i]['id'],
                    'id_str':global_list_theblacklist[i]['id_str'],
                    'text' : global_list_theblacklist[i]['text'],
                    'source' : global_list_theblacklist[i]['source'],
                    'user' : global_list_theblacklist[i]['user'],
                    'coordinates' : global_list_theblacklist[i]['coordinates'],
                    'place' : global_list_theblacklist[i]['place'],
                    'retweet_count' : global_list_theblacklist[i]['retweet_count'],
                    'favorite_count' : global_list_theblacklist[i]['favorite_count'],
                    'entities': global_list_theblacklist[i]['entities'],
                    'favorited' : global_list_theblacklist[i]['favorited'],
                    'retweeted' : global_list_theblacklist[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
tb = database.theblacklist


tb.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_theblacklist)) :
    try:
        holder = sample_theblacklist[i]
        #Sending the tweet to the collection
        tb.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue

#4)thecrown

#################################################################################################################################

#Name of the show
q = "#TheCrown"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_thecrown.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_thecrown)) : 
    sample_thecrown.append({ 'created_at':global_list_thecrown[i]['created_at'],
                    'id':global_list_thecrown[i]['id'],
                    'id_str':global_list_thecrown[i]['id_str'],
                    'text' : global_list_thecrown[i]['text'],
                    'source' : global_list_thecrown[i]['source'],
                    'user' : global_list_thecrown[i]['user'],
                    'coordinates' : global_list_thecrown[i]['coordinates'],
                    'place' : global_list_thecrown[i]['place'],
                    'retweet_count' : global_list_thecrown[i]['retweet_count'],
                    'favorite_count' : global_list_thecrown[i]['favorite_count'],
                    'entities': global_list_thecrown[i]['entities'],
                    'favorited' : global_list_thecrown[i]['favorited'],
                    'retweeted' : global_list_thecrown[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
tc = database.thecrown


tc.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_thecrown)) :
    try:
        holder = sample_thecrown[i]
        #Sending the tweet to the collection
        tc.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#5)thebossbabybackinbusiness

#################################################################################################################################


#Name of the show
q = "#bossbabybackinbusiness"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_thebossbabybackinbusiness.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_thebossbabybackinbusiness)) : 
    sample_thebossbabybackinbusiness.append({ 'created_at':global_list_thebossbabybackinbusiness[i]['created_at'],
                    'id':global_list_thebossbabybackinbusiness[i]['id'],
                    'id_str':global_list_thebossbabybackinbusiness[i]['id_str'],
                    'text' : global_list_thebossbabybackinbusiness[i]['text'],
                    'source' : global_list_thebossbabybackinbusiness[i]['source'],
                    'user' : global_list_thebossbabybackinbusiness[i]['user'],
                    'coordinates' : global_list_thebossbabybackinbusiness[i]['coordinates'],
                    'place' : global_list_thebossbabybackinbusiness[i]['place'],
                    'retweet_count' : global_list_thebossbabybackinbusiness[i]['retweet_count'],
                    'favorite_count' : global_list_thebossbabybackinbusiness[i]['favorite_count'],
                    'entities': global_list_thebossbabybackinbusiness[i]['entities'],
                    'favorited' : global_list_thebossbabybackinbusiness[i]['favorited'],
                    'retweeted' : global_list_thebossbabybackinbusiness[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
tbbbib = database.thebossbabybackinbusiness


tbbbib.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_thebossbabybackinbusiness)) :
    try:
        holder = sample_thebossbabybackinbusiness[i]
        #Sending the tweet to the collection
        tbbbib.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue
    


#6) Scam1992OnSonyLIV

#################################################################################################################################

#Name of the show
q = "#Scam1992OnSonyLIV"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_Scam1992OnSonyLIV.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_Scam1992OnSonyLIV)) : 
    sample_Scam1992OnSonyLIV.append({ 'created_at':global_list_Scam1992OnSonyLIV[i]['created_at'],
                    'id':global_list_Scam1992OnSonyLIV[i]['id'],
                    'id_str':global_list_Scam1992OnSonyLIV[i]['id_str'],
                    'text' : global_list_Scam1992OnSonyLIV[i]['text'],
                    'source' : global_list_Scam1992OnSonyLIV[i]['source'],
                    'user' : global_list_Scam1992OnSonyLIV[i]['user'],
                    'coordinates' : global_list_Scam1992OnSonyLIV[i]['coordinates'],
                    'place' : global_list_Scam1992OnSonyLIV[i]['place'],
                    'retweet_count' : global_list_Scam1992OnSonyLIV[i]['retweet_count'],
                    'favorite_count' : global_list_Scam1992OnSonyLIV[i]['favorite_count'],
                    'entities': global_list_Scam1992OnSonyLIV[i]['entities'],
                    'favorited' : global_list_Scam1992OnSonyLIV[i]['favorited'],
                    'retweeted' : global_list_Scam1992OnSonyLIV[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
scam1992 = database.Scam1992OnSonyLIV

scam1992.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_Scam1992OnSonyLIV)) :
    try:
        holder = sample_Scam1992OnSonyLIV[i]
        #Sending the tweet to the collection
        scam1992.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#7) mandalorian

#################################################################################################################################

#Name of the show
q = "#TheMandalorian"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_mandalorian.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_mandalorian)) : 
    sample_mandalorian.append({ 'created_at':global_list_mandalorian[i]['created_at'],
                    'id':global_list_mandalorian[i]['id'],
                    'id_str':global_list_mandalorian[i]['id_str'],
                    'text' : global_list_mandalorian[i]['text'],
                    'source' : global_list_mandalorian[i]['source'],
                    'user' : global_list_mandalorian[i]['user'],
                    'coordinates' : global_list_mandalorian[i]['coordinates'],
                    'place' : global_list_mandalorian[i]['place'],
                    'retweet_count' : global_list_mandalorian[i]['retweet_count'],
                    'favorite_count' : global_list_mandalorian[i]['favorite_count'],
                    'entities': global_list_mandalorian[i]['entities'],
                    'favorited' : global_list_mandalorian[i]['favorited'],
                    'retweeted' : global_list_mandalorian[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
mand = database.mandalorian

mand.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_mandalorian)) :
    try:
        holder = sample_mandalorian[i]
        #Sending the tweet to the collection
        mand.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#8) mirzapur2

#################################################################################################################################

#Name of the show
q = "#Mirzapur2"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_mirzapur2.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_mirzapur2)) : 
    sample_mirzapur2.append({ 'created_at':global_list_mirzapur2[i]['created_at'],
                    'id':global_list_mirzapur2[i]['id'],
                    'id_str':global_list_mirzapur2[i]['id_str'],
                    'text' : global_list_mirzapur2[i]['text'],
                    'source' : global_list_mirzapur2[i]['source'],
                    'user' : global_list_mirzapur2[i]['user'],
                    'coordinates' : global_list_mirzapur2[i]['coordinates'],
                    'place' : global_list_mirzapur2[i]['place'],
                    'retweet_count' : global_list_mirzapur2[i]['retweet_count'],
                    'favorite_count' : global_list_mirzapur2[i]['favorite_count'],
                    'entities': global_list_mirzapur2[i]['entities'],
                    'favorited' : global_list_mirzapur2[i]['favorited'],
                    'retweeted' : global_list_mirzapur2[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
m2 = database.mirzapur2

m2.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_mirzapur2)) :
    try:
        holder = sample_mirzapur2[i]
        #Sending the tweet to the collection
        m2.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#9) biggboss14

#################################################################################################################################

#Name of the show
q = "#BiggBoss14"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_biggboss14.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_biggboss14)) : 
    sample_biggboss14.append({ 'created_at':global_list_biggboss14[i]['created_at'],
                    'id':global_list_biggboss14[i]['id'],
                    'id_str':global_list_biggboss14[i]['id_str'],
                    'text' : global_list_biggboss14[i]['text'],
                    'source' : global_list_biggboss14[i]['source'],
                    'user' : global_list_biggboss14[i]['user'],
                    'coordinates' : global_list_biggboss14[i]['coordinates'],
                    'place' : global_list_biggboss14[i]['place'],
                    'retweet_count' : global_list_biggboss14[i]['retweet_count'],
                    'favorite_count' : global_list_biggboss14[i]['favorite_count'],
                    'entities': global_list_biggboss14[i]['entities'],
                    'favorited' : global_list_biggboss14[i]['favorited'],
                    'retweeted' : global_list_biggboss14[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
bb14 = database.biggboss14

bb14.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_biggboss14)) :
    try:
        holder = sample_biggboss14[i]
        #Sending the tweet to the collection
        bb14.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#10) ateacher

#################################################################################################################################

#Name of the show
q = "#ateacher"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_ateacher.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_ateacher)) : 
    sample_ateacher.append({ 'created_at':global_list_ateacher[i]['created_at'],
                    'id':global_list_ateacher[i]['id'],
                    'id_str':global_list_ateacher[i]['id_str'],
                    'text' : global_list_ateacher[i]['text'],
                    'source' : global_list_ateacher[i]['source'],
                    'user' : global_list_ateacher[i]['user'],
                    'coordinates' : global_list_ateacher[i]['coordinates'],
                    'place' : global_list_ateacher[i]['place'],
                    'retweet_count' : global_list_ateacher[i]['retweet_count'],
                    'favorite_count' : global_list_ateacher[i]['favorite_count'],
                    'entities': global_list_ateacher[i]['entities'],
                    'favorited' : global_list_ateacher[i]['favorited'],
                    'retweeted' : global_list_ateacher[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
at = database.ateacher 

at.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_ateacher)) :
    try:
        holder = sample_ateacher[i]
        #Sending the tweet to the collection
        at.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#11) thequeensgambit

#################################################################################################################################

#Name of the show
q = " #TheQueensGambit"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_thequeensgambit.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_thequeensgambit)) : 
    sample_thequeensgambit.append({ 'created_at':global_list_thequeensgambit[i]['created_at'],
                    'id':global_list_thequeensgambit[i]['id'],
                    'id_str':global_list_thequeensgambit[i]['id_str'],
                    'text' : global_list_thequeensgambit[i]['text'],
                    'source' : global_list_thequeensgambit[i]['source'],
                    'user' : global_list_thequeensgambit[i]['user'],
                    'coordinates' : global_list_thequeensgambit[i]['coordinates'],
                    'place' : global_list_thequeensgambit[i]['place'],
                    'retweet_count' : global_list_thequeensgambit[i]['retweet_count'],
                    'favorite_count' : global_list_thequeensgambit[i]['favorite_count'],
                    'entities': global_list_thequeensgambit[i]['entities'],
                    'favorited' : global_list_thequeensgambit[i]['favorited'],
                    'retweeted' : global_list_thequeensgambit[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
tqg = database.thequeensgambit

tqg.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_thequeensgambit)) :
    try:
        holder = sample_thequeensgambit[i]
        #Sending the tweet to the collection
        tqg.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#12) youngsheldon

#################################################################################################################################

#Name of the show
q = "#YoungSheldon"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_youngsheldon.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_youngsheldon)) : 
    sample_youngsheldon.append({ 'created_at':global_list_youngsheldon[i]['created_at'],
                    'id':global_list_youngsheldon[i]['id'],
                    'id_str':global_list_youngsheldon[i]['id_str'],
                    'text' : global_list_youngsheldon[i]['text'],
                    'source' : global_list_youngsheldon[i]['source'],
                    'user' : global_list_youngsheldon[i]['user'],
                    'coordinates' : global_list_youngsheldon[i]['coordinates'],
                    'place' : global_list_youngsheldon[i]['place'],
                    'retweet_count' : global_list_youngsheldon[i]['retweet_count'],
                    'favorite_count' : global_list_youngsheldon[i]['favorite_count'],
                    'entities': global_list_youngsheldon[i]['entities'],
                    'favorited' : global_list_youngsheldon[i]['favorited'],
                    'retweeted' : global_list_youngsheldon[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
ys = database.youngsheldon

ys.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_youngsheldon)) :
    try:
        holder = sample_youngsheldon[i]
        #Sending the tweet to the collection
        ys.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue



#13) thewalkingdead

#################################################################################################################################

#Name of the show
q = " #TheWalkingDead"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_thewalkingdead.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_thewalkingdead)) : 
    sample_thewalkingdead.append({ 'created_at':global_list_thewalkingdead[i]['created_at'],
                    'id':global_list_thewalkingdead[i]['id'],
                    'id_str':global_list_thewalkingdead[i]['id_str'],
                    'text' : global_list_thewalkingdead[i]['text'],
                    'source' : global_list_thewalkingdead[i]['source'],
                    'user' : global_list_thewalkingdead[i]['user'],
                    'coordinates' : global_list_thewalkingdead[i]['coordinates'],
                    'place' : global_list_thewalkingdead[i]['place'],
                    'retweet_count' : global_list_thewalkingdead[i]['retweet_count'],
                    'favorite_count' : global_list_thewalkingdead[i]['favorite_count'],
                    'entities': global_list_thewalkingdead[i]['entities'],
                    'favorited' : global_list_thewalkingdead[i]['favorited'],
                    'retweeted' : global_list_thewalkingdead[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
twd = database.thewalkingdead

twd.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_thewalkingdead)) :
    try:
        holder = sample_thewalkingdead[i]
        #Sending the tweet to the collection
        twd.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue
    


#14) schittscreek

#################################################################################################################################

#Name of the show
q = " #SchittsCreek"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_schittscreek.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_schittscreek)) : 
    sample_schittscreek.append({ 'created_at':global_list_schittscreek[i]['created_at'],
                    'id':global_list_schittscreek[i]['id'],
                    'id_str':global_list_schittscreek[i]['id_str'],
                    'text' : global_list_schittscreek[i]['text'],
                    'source' : global_list_schittscreek[i]['source'],
                    'user' : global_list_schittscreek[i]['user'],
                    'coordinates' : global_list_schittscreek[i]['coordinates'],
                    'place' : global_list_schittscreek[i]['place'],
                    'retweet_count' : global_list_schittscreek[i]['retweet_count'],
                    'favorite_count' : global_list_schittscreek[i]['favorite_count'],
                    'entities': global_list_schittscreek[i]['entities'],
                    'favorited' : global_list_schittscreek[i]['favorited'],
                    'retweeted' : global_list_schittscreek[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
scr = database.schittscreek

scr.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_schittscreek)) :
    try:
        holder = sample_schittscreek[i]
        #Sending the tweet to the collection
        scr.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue


#15) theoffice

#################################################################################################################################

#Name of the show
q = " #TheOffice"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_theoffice.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_theoffice)) : 
    sample_theoffice.append({ 'created_at':global_list_theoffice[i]['created_at'],
                    'id':global_list_theoffice[i]['id'],
                    'id_str':global_list_theoffice[i]['id_str'],
                    'text' : global_list_theoffice[i]['text'],
                    'source' : global_list_theoffice[i]['source'],
                    'user' : global_list_theoffice[i]['user'],
                    'coordinates' : global_list_theoffice[i]['coordinates'],
                    'place' : global_list_theoffice[i]['place'],
                    'retweet_count' : global_list_theoffice[i]['retweet_count'],
                    'favorite_count' : global_list_theoffice[i]['favorite_count'],
                    'entities': global_list_theoffice[i]['entities'],
                    'favorited' : global_list_theoffice[i]['favorited'],
                    'retweeted' : global_list_theoffice[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
toff = database.theoffice

toff.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_theoffice)) :
    try:
        holder = sample_theoffice[i]
        #Sending the tweet to the collection
        toff.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue


#16) ToTheLake
#################################################################################################################################

#Name of the show
q = " #ToTheLake"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_ToTheLake.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_ToTheLake)) : 
    sample_ToTheLake.append({ 'created_at':global_list_ToTheLake[i]['created_at'],
                    'id':global_list_ToTheLake[i]['id'],
                    'id_str':global_list_ToTheLake[i]['id_str'],
                    'text' : global_list_ToTheLake[i]['text'],
                    'source' : global_list_ToTheLake[i]['source'],
                    'user' : global_list_ToTheLake[i]['user'],
                    'coordinates' : global_list_ToTheLake[i]['coordinates'],
                    'place' : global_list_ToTheLake[i]['place'],
                    'retweet_count' : global_list_ToTheLake[i]['retweet_count'],
                    'favorite_count' : global_list_ToTheLake[i]['favorite_count'],
                    'entities': global_list_ToTheLake[i]['entities'],
                    'favorited' : global_list_ToTheLake[i]['favorited'],
                    'retweeted' : global_list_ToTheLake[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
ttlake = database.ToTheLake

ttlake.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_ToTheLake)) :
    try:
        holder = sample_ToTheLake[i]
        #Sending the tweet to the collection
        ttlake.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue


#17) TheHauntingofBlyManor

#################################################################################################################################

#Name of the show
q = " #TheHauntingofBlyManor"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_TheHauntingofBlyManor.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_TheHauntingofBlyManor)) : 
    sample_TheHauntingofBlyManor.append({ 'created_at':global_list_TheHauntingofBlyManor[i]['created_at'],
                    'id':global_list_TheHauntingofBlyManor[i]['id'],
                    'id_str':global_list_TheHauntingofBlyManor[i]['id_str'],
                    'text' : global_list_TheHauntingofBlyManor[i]['text'],
                    'source' : global_list_TheHauntingofBlyManor[i]['source'],
                    'user' : global_list_TheHauntingofBlyManor[i]['user'],
                    'coordinates' : global_list_TheHauntingofBlyManor[i]['coordinates'],
                    'place' : global_list_TheHauntingofBlyManor[i]['place'],
                    'retweet_count' : global_list_TheHauntingofBlyManor[i]['retweet_count'],
                    'favorite_count' : global_list_TheHauntingofBlyManor[i]['favorite_count'],
                    'entities': global_list_TheHauntingofBlyManor[i]['entities'],
                    'favorited' : global_list_TheHauntingofBlyManor[i]['favorited'],
                    'retweeted' : global_list_TheHauntingofBlyManor[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
thobm = database.TheHauntingofBlyManor

thobm.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_TheHauntingofBlyManor)) :
    try:
        holder = sample_TheHauntingofBlyManor[i]
        #Sending the tweet to the collection
        thobm.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue
    


#18) Barbarians

#################################################################################################################################

#Name of the show
q = "#Barbarians"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_Barbarians.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_Barbarians)) : 
    sample_Barbarians.append({ 'created_at':global_list_Barbarians[i]['created_at'],
                    'id':global_list_Barbarians[i]['id'],
                    'id_str':global_list_Barbarians[i]['id_str'],
                    'text' : global_list_Barbarians[i]['text'],
                    'source' : global_list_Barbarians[i]['source'],
                    'user' : global_list_Barbarians[i]['user'],
                    'coordinates' : global_list_Barbarians[i]['coordinates'],
                    'place' : global_list_Barbarians[i]['place'],
                    'retweet_count' : global_list_Barbarians[i]['retweet_count'],
                    'favorite_count' : global_list_Barbarians[i]['favorite_count'],
                    'entities': global_list_Barbarians[i]['entities'],
                    'favorited' : global_list_Barbarians[i]['favorited'],
                    'retweeted' : global_list_Barbarians[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
bbr = database.Barbarians

bbr.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_Barbarians)) :
    try:
        holder = sample_Barbarians[i]
        #Sending the tweet to the collection
        bbr.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue
    

# 19) LuciferNetflix

#################################################################################################################################

#Name of the show
q = "#LuciferNetflix"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_LuciferNetflix.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_LuciferNetflix)) : 
    sample_LuciferNetflix.append({ 'created_at':global_list_LuciferNetflix[i]['created_at'],
                    'id':global_list_LuciferNetflix[i]['id'],
                    'id_str':global_list_LuciferNetflix[i]['id_str'],
                    'text' : global_list_LuciferNetflix[i]['text'],
                    'source' : global_list_LuciferNetflix[i]['source'],
                    'user' : global_list_LuciferNetflix[i]['user'],
                    'coordinates' : global_list_LuciferNetflix[i]['coordinates'],
                    'place' : global_list_LuciferNetflix[i]['place'],
                    'retweet_count' : global_list_LuciferNetflix[i]['retweet_count'],
                    'favorite_count' : global_list_LuciferNetflix[i]['favorite_count'],
                    'entities': global_list_LuciferNetflix[i]['entities'],
                    'favorited' : global_list_LuciferNetflix[i]['favorited'],
                    'retweeted' : global_list_LuciferNetflix[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
ln = database.LuciferNetflix

ln.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_LuciferNetflix)) :
    try:
        holder = sample_LuciferNetflix[i]
        #Sending the tweet to the collection
        ln.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue

#20) #Friends25

#################################################################################################################################

#Name of the show
q = "#Friends25"

#search the show's tweets using API
search_hashtag = twitter_api.search.tweets(count=count,q=q)

#saving
stat_hashtag = search_hashtag["statuses"]

#initializing the list
since_id_new = stat_hashtag [-1]['id']

#appending the tweets to the global list
for tweet in stat_hashtag:
    try:
        global_list_Friends25.append(tweet)     
    except pymongo.errors.DuplicateKeyError:
        continue


for i in range( len(global_list_Friends25)) : 
    sample_Friends25.append({ 'created_at':global_list_Friends25[i]['created_at'],
                    'id':global_list_Friends25[i]['id'],
                    'id_str':global_list_Friends25[i]['id_str'],
                    'text' : global_list_Friends25[i]['text'],
                    'source' : global_list_Friends25[i]['source'],
                    'user' : global_list_Friends25[i]['user'],
                    'coordinates' : global_list_Friends25[i]['coordinates'],
                    'place' : global_list_Friends25[i]['place'],
                    'retweet_count' : global_list_Friends25[i]['retweet_count'],
                    'favorite_count' : global_list_Friends25[i]['favorite_count'],
                    'entities': global_list_Friends25[i]['entities'],
                    'favorited' : global_list_Friends25[i]['favorited'],
                    'retweeted' : global_list_Friends25[i]['retweeted']
                    })

#print(sample_emilyinparis)

#collection for the show 
f25 = database.Friends25

f25.create_index([   ("id",pymongo.ASCENDING)],
                                    unique=True)

#inserting each tweet after fetching the required fields to the collection
for i in range(len(sample_Friends25)) :
    try:
        holder = sample_Friends25[i]
        #Sending the tweet to the collection
        f25.insert_one(holder)
    except pymongo.errors.DuplicateKeyError:
        continue
