import pandas as pd
import tweepy
import config


def fetch_tweets(ids, api):
    # When I looped through all the 3400 ids, the API is giving an error.
    # Therefore, I tried to process the ids by batch or chunks.

    # We'll process only 50 entries because the statuses_lookup() method gives the statuses of IDs, up to 100 only..

    tw_statuses = api.statuses_lookup(ids, tweet_mode="extended")
    data = pd.DataFrame()
    for status in tw_statuses:
        # print(status)
        tweet_elem = {"tweet_id": status.id,
                      "tweet": status.full_text,
                      "date": status.created_at}
        data = data.append(tweet_elem, ignore_index=True)
    data.to_csv("scraped_tweets_SF.csv", mode="a")

    return data


def extract_tweets():

    tweet_url = pd.read_csv("scraped_tweets_SF.txt", index_col=None, header=None, names=["tweet_urls"])
    # Extract the tweet id
    af = lambda x: x["tweet_urls"].split("/")[-1]
    # store tweet id in another column
    tweet_url['tweet_id'] = tweet_url.apply(af, axis=1)
    ids = tweet_url['tweet_id'].tolist()
    return ids


def main():
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    ids = extract_tweets()
    total_count = len(ids)
    chunks = (total_count - 1) // 50 + 1
    for i in range(chunks):
        subset_ids = ids[i * 50:(i + 1) * 50]
        final_df = fetch_tweets(subset_ids, api)
        print(final_df.size)


if __name__ == "__main__":
    main()
