# appTwitter

Twitter 自動投稿プログラム

指定したTwitterアカウントでプログラム内で指定した内容で自動投稿をする。

自動投稿内容は当時記載していたブログ記事

※現在はサーバー維持費の関係でブログは封鎖中。

## 必要認証情報

Twitterアカウントのログインに必要な認証情報として、以下のファイルが必要。

### PersonalInfoTwitter.py

アクセストークンを含む認証情報。ファイルの内部情報は以下のイメージ

BEARER_TOKEN        = "xx"  
API_KEY             = "xxx"  
API_SECRET          = "xxxx"  
CLIENT_ID           = "xx"  
CLIENT_SECRET       = "xx"  
ACCESS_TOKEN        = "xx"  
ACCESS_TOKEN_SECRET = "xx"  

### APIKey.txt

取得したAPIKeyのテキストファイル

## 実行イメージ

ローカル環境にpythonファイルを実行するためのbatファイルを用意し、そのbatファイルを実行することで処理を開始する。
※実際のbatファイルはローカル環境のパスが記載されているので、gitには上げない。

```bat
echo off
rem このファイルの配置フォルダをカレントにする
pushd %0\..
rem 画面をクリア
cls
rem pythonスクリプトを実行 ファイルの場所を指定する
python C:xxxx\appTwitter\mainTwitter.py
rem 30秒間待機
timeout /t 30
```

## 参考URL

python&twitter:<https://di-acc2.com/system/rpa/9748/>

twitterAPI:<https://di-acc2.com/system/rpa/9688/>
