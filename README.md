# CSE6242_TwitterCovidSentimentAnalysis
The process of generating the csv is broken out in two steps:
1) Generate Tweet ID text files
2) Create CSV using the Tweet IDs and the Tweepy package

<b>Generate the Text file:</b>
Create a project and a virtual environment (if desired)
Install tweepy and snscrape packages into the working environment (use pip-install)

Step 2: Open your terminal and copy the following commands. Include changes that you want.
For txt file:

snscrape twitter-search "coronavirus since:2020-01-01 until:2020-10-30 near:'san-francisco' within:10km lang:en min_faves:5000 min_retweets:2500" > scraped_tweets_SF.txt

Once the txt file is generated, run the parsing.py file with the correct .txt file. It will create the sample csv for you
