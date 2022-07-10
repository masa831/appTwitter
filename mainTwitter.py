import tweepy
from pprint import pprint
import schedule
from time import sleep
import PersonalInfoTwitter
from func import tweetTask

try:
    # 処理開始メッセージ
    print('Twitter自動投稿処理を開始します')
    # tweet実施
    tweetTask()
    
    # schedule.every().days.at("21:52").do(tweetTask)
    # while True:
    #     schedule.run_pending()
    #     sleep(1)
    
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

# 定期実行メモ
# #01 定期実行する関数を準備
# def task():
#     print("タスク実行中")
    
# #02 スケジュール登録
# schedule.every().days.at("7:00").do(task)

# #03 イベント実行
# while True:
#     schedule.run_pending()
#     sleep(1)
