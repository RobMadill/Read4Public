# tweepy - guide (for authentication): https://realpython.com/twitter-bot-python-tweepy/
# tweepy - full documentation: https://docs.tweepy.org/en/stable/getting_started.html
# tweepy - API reference: https://docs.tweepy.org/en/stable/api.html#api-reference
import tweepy
import argparse
import config

# Passes twitter authentication to tweepy


def auth() -> tweepy.API:
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Modifies content to make period delimiter


def content_modify(content: str) -> str:
    with open(content, mode='r') as c:
        text = c.read().replace('\n', ' ')
        sentence = text.split('.')
        sentence = [s.strip() for s in sentence]
        return sentence

# Creates list of keywords for case insensitive search


def case_ignore(keyword: str) -> list:
    return [keyword.lower(), keyword[0:1].upper()+keyword[1:]]

# Reads content with keyword selection and sends as tweet


def main(content: str, keyword: str) -> None:
    api = auth()
    text = content_modify(content)
    keyword_list = case_ignore(keyword)
    for line in range(len(text)):
        if any(keyword in text[line] for keyword in keyword_list):
            if len(text[line]) < 265:
                # write if statement to make tweet keyword if there is empty space
                api.update_status(text[line])
                # print(f"Line: {line} ", text[line])


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
