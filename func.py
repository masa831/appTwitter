
import tweepy
from pprint import pprint
import schedule
from time import sleep
import random
import PersonalInfoTwitter

# 割り当て
BEARER_TOKEN        = PersonalInfoTwitter.BEARER_TOKEN
API_KEY             = PersonalInfoTwitter.API_KEY
API_SECRET          = PersonalInfoTwitter.API_SECRET
ACCESS_TOKEN        = PersonalInfoTwitter.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = PersonalInfoTwitter.ACCESS_TOKEN_SECRET

# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )
    return client

# tweet用関数
def CreateTweet(message):
    tweet = ClientInfo().create_tweet(text=message)
    return tweet

# delete関数
def DeleteTweet(tweet_id):
    delete_tweet = ClientInfo().delete_tweet(id=tweet_id)
    return delete_tweet

# HPのURL取得関数
def getURL():
    # 初期化
    url = ""
    randam_number = 99

    # URLを格納した辞書を定義
    dic_url = {
        1:"https://wkwkdkdk-blog.com/",
        2:"https://wkwkdkdk-blog.com/camp-diary/camp1/",
        3:"https://wkwkdkdk-blog.com/camp-diary/camp2/",
        4:"https://wkwkdkdk-blog.com/camp-diary/camp3/",
        5:"https://wkwkdkdk-blog.com/camp-diary/camp2_2/",
        6:"https://wkwkdkdk-blog.com/camp-diary/camp1_2/",
        7:"https://wkwkdkdk-blog.com/camp-diary/camp2_1/",
        8:"https://wkwkdkdk-blog.com/it-page/it_1/",
        9:"https://wkwkdkdk-blog.com/it-page/it_2/",
        }

    # 引数が辞書のlengthより大きい場合
    if randam_number > len(dic_url):
        randam_number = random.randint(1,len(dic_url))
    else:
        randam_number = 1

    # 引数に応じてURLを取得
    url = dic_url[randam_number] + "\n"
    return url

