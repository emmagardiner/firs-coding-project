import test
import json
import tweepy
import webbrowser
import sys
import math

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
    
pos_ws = []
f = open('positive-words.txt', 'r')
for l in f.readlines()[35:]:
    pos_ws.append(unicode(l.strip()))
#f.close()

neg_ws = []
g = open('negative-words.txt', 'r')
for l in g.readlines()[35:]:
    neg_ws.append(unicode(l.strip()))

rac_ws = []
h = open('racist-words.txt', 'r')
for l in h.readlines()[4:]:
	rac_ws.append(unicode(l.strip()))

API_KEY = "clLqbnWrloNL5FNEgJC4Oxnyb"
API_SECRET = "auNdWWFQ7QWpnHTpP3TSbCKAXYZ4mhQWasZzruGyztdkDmrl0Z"
access_token = "2275236163-pCkdcRGRdsw059LnaRe94itRGALI2Id5sU1s0SB"
access_token_secret = "xWh9j9mcEF4ZotGNcDXeNuX55ZuACN60eIovgbuGMNgTc"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

obama = api.search(q="obama",count=100)

obama_tweets = []
obama_tweets = [tweet.text.encode(sys.stdout.encoding, 'replace') for tweet in obama]

romney = api.search(q="romney",count=100)

romney_tweets = []
romney_tweets = [tweet.text.encode(sys.stdout.encoding, 'replace') for tweet in romney]

#------------------------------------------------------

class Tweet_Holder():
    """object representing one tweet"""
    def __init__(self, tweet):
		self.text = tweet

    def positive(self):
        L =[]
        t = self.text.split()
        for word in t:
        	if word in pos_ws:
        		L.append(word)
        	else:
        		pass
        return len(L)
                   
    def negative(self):
        L2 =[]
        t2 = self.text.split()
        for word in t2:
        	if word in neg_ws:
        		L2.append(word)
        	else:
        		pass
        return len(L2)
    
    def racist(self):
        L3 =[]
        t3 = self.text.split()
        for word in t3:
        	if word in rac_ws:
        		L3.append(word)
        	else:
        		pass
        return len(L3)
    		
    def get_positive_words(self):
    	L4 =[]
        t4 = self.text.split()
        for word in t4:
        	if word in pos_ws:
        		L4.append(word)
        	else:
        		pass
        return L4
    	
    def get_negative_words(self):
    	L5 =[]
        t5 = self.text.split()
        for word in t5:
        	if word in neg_ws:
        		L5.append(word)
        	else:
        		pass
        return L5
    
    def get_racist_words(self):
    	L6 = []
    	t6 = self.text.split()
    	for word in t6:
    		if word in rac_ws:
    			L6.append(word)
    		else:
    			pass
    	return L6
    
	def __str__(self):
		return self.text

        
sample_tweet = "Some people adore Obama and think he is an all-around agreeable man while others think he is despicable"
sample = Tweet_Holder(sample_tweet)
test.testEqual(sample.positive(), 3)
test.testEqual(sample.negative(), 1)
test.testEqual(len(sample.get_positive_words()), 3)
test.testType(sample.racist(), 'int')

obama_tweet_holders = []
for tweet in obama_tweets:
	obama_tweet_holders.append(Tweet_Holder(tweet))

romney_tweet_holders = []
for tweet in romney_tweets:
	romney_tweet_holders.append(Tweet_Holder(tweet))

sample_list = []
sample_list.append(sample)


obama_num_rac_words = []
obama_num_pos_words = []
obama_num_neg_words = []
for tweet in obama_tweets:
	o = Tweet_Holder(tweet)
	obama_num_neg_words.append(o.negative())
	obama_num_pos_words.append(o.positive())
	obama_num_rac_words.append(o.racist())

romney_num_rac_words = []
romney_num_pos_words = []
romney_num_neg_words = []
for tweet in romney_tweets:
	r = Tweet_Holder(tweet)
	romney_num_rac_words.append(r.racist())
	romney_num_neg_words.append(r.negative())
	romney_num_pos_words.append(r.positive())


obama_total_pos = sum(obama_num_pos_words)
obama_total_neg = sum(obama_num_neg_words)
obama_total_rac = sum(obama_num_rac_words)
romney_total_pos = sum(romney_num_pos_words)
romney_total_neg = sum(romney_num_neg_words)
romney_total_rac = sum(romney_num_rac_words)


obama_neg_words = []
for tweet in obama_tweets:
	o = Tweet_Holder(tweet)
	for word in o.get_negative_words():
		obama_neg_words.append(word)


#----------------------------------------------------

class Analysis():
	def __init__ (self, tweets_instances):
		self.tweets_instances = tweets_instances
	
	def top_negative_words(self):
	 	d = {} 	
	 	for y in self.tweets_instances:
	 		for x in y.get_negative_words():
	 			if x not in d:
	 				d[x] = 1
	 			else:
	 				d[x] = d[x] +1
	 	top_3_negative = sorted(d.items(), None, lambda x: x[1], True)
	 	return top_3_negative[:3]
	 
	def top_positive_words(self):
		d2 = {}
		for y in self.tweets_instances:
			for x in y.get_positive_words():
				if x not in d2:
					d2[x] = 1
				else:
					d2[x] = d2[x] +1
		top_3_positive = sorted(d2.items(), None, lambda x: x[1], True)
		return top_3_positive[:3]
	
	def top_racist_words(self):
		d3 ={}
		for y in tweets_instances:
			for x in y.get_racist_words():
				if x not in d3:
					d3[x] = 1
				else:
					d3[x] = d3[x] +1
		top_3_racist = sorted(d3.items(), None, lambda x: x[1], True)
		return top_3_racist[:3]

sample_tweet2 = "Obama is a horrible horrible human being who is 2-faced and a cancerous callous terrible terrible terrible person"
sample2 = Tweet_Holder(sample_tweet2)
sample_list.append(sample2)
analysis = Analysis(sample_list)
test.testEqual(len(analysis.top_negative_words()), 3)
test.testType(analysis.top_positive_words(), 'list')

obama_analysis = Analysis(obama_tweet_holders)
romney_analysis = Analysis(romney_tweet_holders)

O1 = obama_analysis.top_negative_words()
O2 = obama_analysis.top_positive_words()
R1 = romney_analysis.top_negative_words()
R2 = romney_analysis.top_positive_words()


#-------------------------------------------------------

print "--------------------------------------------------------------"

print "This project compares tweets in which Obama was mentioned and tweets in which Romney was mentioned and collects data on these tweets."
print "Specifically, this project examines these tweets in terms of positive, negative, and racist words."
print "In tweets mentioning Obama, there were " + str(obama_total_pos) + " total positive words, " + str(obama_total_neg) + " total negative words, and " + str(obama_total_rac) + " total racist words."
print "In tweets mentioning Romney, there were " + str(romney_total_pos) + " total positive words, " + str(romney_total_neg) + " total negative words, and " + str(romney_total_rac) + " total racist words."

if romney_total_neg > romney_total_pos:
	print "Tweets mentioning Romney had more negative words than positive words, and the top 3 negative words were " + str(R1[0][0]) + ", " + str(R1[1][0]) + ", and " + str(R1[2][0]) + "."
else:
	print "Tweets mentioning Romney had more positive words than negative words, and the top 3 positive words were " + str(R2[0][0]) + ", " + str(R2[1][0]) + ", and " + str(R2[2][0]) + "."

if obama_total_neg > obama_total_pos:
	print "Tweets mentioning Obama had more negative words than positive words, and the top 3 negative words were " + str(O1[0][0]) + ", " + str(O1[1][0]) + ", and " + str(O1[2][0]) + "."
else:
	print "Tweets mentioning Obama had more positive words than negative words, and the top 3 positive words were " + str(O2[0][0]) + ", " + str(O2[1][0]) + ", and " + str(O2[2][0]) + "."

if obama_total_pos > romney_total_pos:
	print "Overall, Obama was mentioned in tweets more positively than Romney."
else:
	print "Overall, Romney was mentioned in tweets more positively than Obama."

print "--------------------------------------------------------------"



