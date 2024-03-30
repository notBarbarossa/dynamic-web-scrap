import requests
import csv

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "false",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.mymarket.ge",
    "referer": "https://www.mymarket.ge/",
    "sec-ch-ua": '"Brave";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

data = {
    "CatID": "69",
    "Limit": "28",
    "Page": "1",
    "SortID": "1",
}

response = requests.post(
    "https://api2.mymarket.ge/api/ka/products", headers=headers, data=data
).json()

asd = response["data"]["Prs"]

name_price_list = []

for i in asd:
    name = i["lang_data"]["title"]
    price = i["price"]
    final = f"{name} -- ₾{price}"
    name_price_list.append(final)
    

with open('phones.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([item.split(' -- ') for item in name_price_list])
