# CSE6242_TwitterCovidSentimentAnalysis
The process of generating the final csv with imputed location is broken out in 3 steps:
1) Generate Tweet ID text files
2) Create CSV using the Tweet IDs and the Tweepy package
3) Use imputation techniques for the Tweets with missing location information
 
<b>1) Generate the Text file with Tweet IDs:</b>
Create a project and a virtual environment (if desired)
Install tweepy and snscrape packages into the working environment (use pip-install)

Step 2: Open your terminal and copy the following commands. Include changes that you want.
For txt file:

snscrape twitter-search "coronavirus since:2020-01-01 until:2020-10-30 near:'san-francisco' within:10km lang:en min_faves:5000 min_retweets:2500" > scraped_tweets_SF.txt
Additional filters can be found here: https://github.com/igorbrigadir/twitter-advanced-search<br>
<b>2 & 3: Creating the CSV</b>
Once the txt file is generated, run the parsing.py file with the correct .txt file. It will create the final csv for you. The functions used in each step are as follows:
Create CSV using Tweet IDs and Tweepy package: extract_tweets(), fetch_tweets()<br>
Use imputation techniques for the missing location tweets: impute_locations(), fill_blanks(), replace_location()
