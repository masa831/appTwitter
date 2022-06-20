import tweepy
from pprint import pprint
import schedule
from time import sleep
import PersonalInfoTwitter
from func import ClientInfo,getURL

try:
    # メッセージを指定
    message_main = "Hello World!!\n今日のpickup記事はこちら!\n※これは定期tweetです\n"

    # URLをランダムで取得
    url = getURL()

    # メッセージタグを指定
    message_tag = "#blog #ブログ #ブログ初心者 #ブログ仲間 #ブログ仲間募集\n#python #自動化"

    # messageを結合
    message = message_main + url + message_tag

    # メッセージの長さを判定 全角180 半角280
    if len(message) >180:
        message = "Hello World!"

    # tweet実施
    tweet = ClientInfo().create_tweet(text=message)

except:
    print('エラーが発生しました')

else:
    print('処理は正常に終了しました')

# Tmp
# 関数実行・結果出力
# pprint(tweet)

# # ツイートIDを指定
# tweet_id = 'ツイートIDを入力'

# delete_tweet = ClientInfo().delete_tweet(id=tweet_id)

# pprint(delete_tweet)

