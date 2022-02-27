# tweepy - video reference: https://www.youtube.com/watch?v=dvAurfBB6Jk
# tweepy - documentation: https://docs.tweepy.org/en/stable/authentication.html#
import tweepy
import argparse
import config


def main():
    # Change to OAuth Bearer token (App Only)
    consumer_key = config.API_KEY
    consumer_secret = config.API_KEY_SECRET
    access_token = config.ACCESS_TOKEN
    access_token_secret = config.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user = api.get_user()

    return print(user.screen_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="reads through content and tweets one sentence at a time")
    parser.add_argument('-d', '--data-file', dest='data_file',
                        metavar='', help='content that will be parsed and tweeted')
    args = parser.parse_args()
    data_file = args.data_file
    main()
