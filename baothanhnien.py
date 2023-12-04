import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import os

url = "https://thanhnien.vn/moi-truong.html"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titles = soup.find_all("h3", class_="box-title-text")

data = []

def get_all_paragraphs(url):
    print("Crawling data ...")
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    paragraphs = soup.find_all('p')

    paragraph_texts = [p.get_text(strip=True) for p in paragraphs]
    

    return paragraph_texts

num = 1
for title in titles:
    os.system('cls')
    print("Saving data ..." ,num, "post")
    title_text = title.a.text.strip()
    href = url + "/" + title.a[ "href"]
    paragraphs = get_all_paragraphs(href)
    data.append([title_text, href, paragraphs])
    num = num + 1

    
df = pd.DataFrame(data)
df.to_csv("data2.csv", index=False, encoding="utf-16")
print("Saved data to data2.csv, press any key.....")
input()