import encodings

import requests
import lxml
from bs4 import BeautifulSoup



article_url_list = []
card_url_list = []

for i in range (1, 2):

    url = f"https://shinaufa.ru/tyres?page={i}"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    article_title = soup.find_all("div", class_="name")


    for article in article_title:

        article_url = article.find("a").get("href")
        article_url_list.append(article_url)


    with open('article_url_list.txt', "w", encoding='utf-8') as file:
        for line in article_url_list:
            file.write(f"https://shinaufa.ru{line}\n")


    with open('article_url_list.txt', "r") as file:

        lineses = [line.strip() for line in file.readlines()]

        for line in lineses:

            b = requests.get(url=line, headers=headers)
            soup_url = BeautifulSoup(b.text, 'lxml')
            card_url = soup_url.find_all("div", class_="info")


            for card in card_url:

                card_name = card.find("h1", class_="name").text
                card_price = card.find("span", class_="price").text.strip()
                rest_goods = card.find("ul", class_="availability").text.strip()
                print({card_name}, {card_price}, {rest_goods})
                # card_url_list.append({card_name} | {card_price}| {rest_goods})


                # with open('card_url_list.txt', "w", encoding='utf-8') as file:
                #     for line in card_url_list:
                #         file.write(line)