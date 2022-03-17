# tweepy - guide (for authentication): https://realpython.com/twitter-bot-python-tweepy/
# tweepy - full documentation: https://docs.tweepy.org/en/stable/getting_started.html
# tweepy - API reference: https://docs.tweepy.org/en/stable/api.html#api-reference
import tweepy
import argparse
import config

# Passes twitter authentication   
def auth() -> API:
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Reads content with keyword selection and sends as tweet
def main(content: str, keyword: str) -> None:
    api = auth()
    with open(content, mode='r', newline='') as c:
        for line in c:
            if keyword in line:
                api.update_status(line)

# Used for command line arguments when running script
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="reads through content and tweets one sentence at a time")
    parser.add_argument('-c', '--content', dest='content',
                        metavar='', help='content that will be parsed and tweeted', required=True)
    parser.add_argument('-k', '--keyword', dest='keyword',
                        metavar='', help='keyword to find in content file', required=True)

    args = parser.parse_args()
    content = args.content
    keyword = args.keyword

    main(content, keyword)
