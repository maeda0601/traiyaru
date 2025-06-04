"""
トライやるウィーク用
012
郵便番号のAPI
"""

import requests

# 郵便番号（ハイフンなし）
zipcode = "6752364"  # 協和製作所

# APIのURL
url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# APIにリクエストを送信
response = requests.get(url)

# 結果をJSONで受け取る
data = response.json()

# 結果の表示
if data["results"]:
    result = data["results"][0]
    print(f"{result['address1']} {result['address2']} {result['address3']}")
else:
    print("該当する住所が見つかりませんでした。")
