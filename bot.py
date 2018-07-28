import tweepy
import time

REPLIED_TO = 'replied_to_log.txt'

with open('config.ini', 'r') as config:
    tokens = config.readlines()
    TW_CONSUMER_KEY = tokens[0].rstrip()
    TW_CONSUMER_SECRET = tokens[1].rstrip()
    TW_ACCESS_KEY = tokens[2].rstrip()
    TW_ACCESS_SECRET = tokens[3].rstrip()


def authenticate_twitter():
    print('Authenticating twitter...')
    auth = tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
    auth.set_access_token(TW_ACCESS_KEY, TW_ACCESS_SECRET)
    twitter = tweepy.API(auth)
    print('Twitter authenticated.\n')
    return twitter


def log_replied_to_tweets(tweet):
    with open(REPLIED_TO, 'a') as f:
        f.write(str(tweet.id) + '\n')


def check_log_if_replied_to(tweet):
    with open(REPLIED_TO, 'r') as f:
        if str(tweet.id) in f.read():
            return True
        else:
            return False


def tweet(twitter, text):
    twitter.update_status(text)


def main():
    twitter = authenticate_twitter()
    while True:
        tweet(twitter, 'test')
        time.sleep(1200)


if __name__ == '__main__':
    main()
