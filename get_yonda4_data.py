import requests
import json
import datetime
import dateutil.parser

# ユーザー名
user_name = "niwacchi"

# 対象ユーザーの取得する総ページ数
page_count = 31

# 初期設定
start = 0
num = 20
url = "http://yonda4.com/api/user/{user_name}?format=json&start={start}&num={num}"
items = []

# リクエスト
for i in range(0, page_count):

    start = num * i

    r_url = url.format(user_name=user_name, start=start, num=num)
    #print(r_url)

    r = requests.get(r_url)
    data = json.loads(r.text)
    
    for item in data['value']['items']:
        items.append(item)

    # 最新ページのみ取得。全データ取得するときはコメントアウトする。
    break

# 出力
for item in items:
    str = "title={title},pubDate={pubDate},description={description}"
    print(str.format(title=item['title'], pubDate=dateutil.parser.parse(item['pubDate']), description=item['description']))
