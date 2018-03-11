from csv import reader

with open('positive_tweets_final.csv', 'w') as out, open('positive_tweets.csv', 'r') as csvfile:    
	for row in reader(csvfile):
		print>>out, row[6]
