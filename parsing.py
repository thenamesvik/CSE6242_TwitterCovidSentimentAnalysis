import pandas as pd
import tweepy


def fetch_tweets(ids, api):
    # When I looped through all the 3400 ids, the API is giving an error.
    # Therefore, I tried to process the ids by batch or chunks.

    total_count = len(ids)
    chunks = (total_count - 1) // 50 + 1

    # We'll process only 50 entries because the statuses_lookup() method gives the statuses of IDs, up to 100 only..

    tw_statuses = api.statuses_lookup(ids, tweet_mode="extended")
    data = pd.DataFrame()
    for status in tw_statuses:
        tweet_elem = {"tweet_id": status.id,
                      "tweet": status.full_text,
                      "date": status.created_at}
        data = data.append(tweet_elem, ignore_index=True)
    data.to_csv("scraped_tweets.csv", mode="a")

    return data


def extract_tweets(consumer_key, consumer_secret, access_token, access_token_secret):

    tweet_url = pd.read_csv("tweet_ids.txt", index_col=None, header=None, names=["tweet_urls"])
    # Extract the tweet id
    af = lambda x: x["tweet_urls"].split("/")[-1]
    # store tweet id in another column
    tweet_url['tweet_id'] = tweet_url.apply(af, axis=1)
    ids = tweet_url['tweet_id'].tolist()
    return ids


def main():
    consumer_key = 'RrRUvq8ymjbusOQ4RFUNoPW7s'
    consumer_secret = 'W4pQUzhHTD0m5i5sNH8oxdNsbKoz7shspwVRx9t7DffWhRqKIv'
    access_token = '1238274915431743489-rA3yM0ui9yTmxUGJiWlpU60e56Utk7'
    access_token_secret = 'cQoCXkn6tbEdntZlt1vIcHdZIVqDvTIhSPHWiwkBbxtQ4'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    ids = extract_tweets(consumer_key, consumer_secret, access_token, access_token_secret)
    final_df = fetch_tweets(ids, api)
    print(final_df)


if __name__ == "__main__":
    main()
