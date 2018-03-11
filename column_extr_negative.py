from csv import reader

with open('negative_tweets_final.csv', 'w') as out, open('negative_tweets.csv', 'r') as csvfile:    
	for row in reader(csvfile):
		print>>out, row[6]
