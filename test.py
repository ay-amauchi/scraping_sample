import bs4
import requests

res = requests.get("https://cookpad.com/")

# 全情報を取得済み→使える形に加工
soup = bs4.BeautifulSoup(res.text, "html.parser")

# <title>の情報を取得
# title_tag = soup.title
# print(title_tag.text)

# divタグをすべて取得
# div_tags = soup.find_all("div")
# div_tag_texts = [div_tag.text for div_tag in div_tags]  # 文字列をリストで取り出す(リスト内包表記)
# print(div_tag_texts)

# left_containerを検索
# tags = soup.find_all("div", class_="left_container")
# tag_text = [tag.text for tag in tags]
# print(tag_text)

# 関連サービスのURLを取得
div_tag = soup.find("div", class_="left_container")
a_tag = div_tag.find("a")
url = "https://cookpad.com" + a_tag.attrs["href"]
print(url)
