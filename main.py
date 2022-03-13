# tweepy - guide: https://realpython.com/twitter-bot-python-tweepy/
# tweepy - documentation: https://docs.tweepy.org/en/stable/authentication.html#
import tweepy
import argparse
import config


def auth() -> object:
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


def main():
    api = auth()
    content = 'resources\The_Idiot_Part_One.txt'
    with open(content, mode='r', newline='') as c:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="reads through content and tweets one sentence at a time")
    parser.add_argument('-c', '--content', dest='content',
                        metavar='', help='content that will be parsed and tweeted')
    args = parser.parse_args()
    content = args.content
    main()
