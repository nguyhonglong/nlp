import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL của trang web cần lấy dữ liệu
url = "https://baotainguyenmoitruong.vn/moi-truong"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titles = soup.find_all("h3", class_="b-grid__title")

data = []

def get_all_paragraphs(url):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    paragraphs = soup.find_all('p')

    paragraph_texts = [p.get_text(strip=True) for p in paragraphs]

    author = soup.find('span', class_='sc-longform-header-author block-sc-author').get_text(strip=True)
    publish_time = soup.find('span', class_='sc-longform-header-author block-sc-author').get_text(strip=True)
    publish_time = soup.find('span', class_='sc-longform-header-date block-sc-publish-time').get_text(strip=True)

    return paragraph_texts, author, publish_time


for title in titles:
    title_text = title.a.text.strip()
    href = title.a["href"]
    paragraphs, author, publish_time = get_all_paragraphs(href)
    
    # Thêm tiêu đề, đường dẫn và nội dung vào danh sách data
    data.append([title_text, href, author, publish_time, paragraphs])
    
df = pd.DataFrame(data, columns=["Tiêu đề", "Đường dẫn", "Tác giả", "Ngày đăng", "Nội dung"])
df.to_excel("data.xlsx", index=False)
