import requests
from bs4 import BeautifulSoup

URL = "https://www.elinsolheim.dk/blog"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

lines_txt = []

blogs_urls = soup.find_all("div", class_="js-render-wrapper")
for div in blogs_urls:
    links = div.findAll('a')
    for a in links:
        # print("https://www.elinsolheim.dk/blog" + a['href'])
        lines_txt.append("https://www.elinsolheim.dk/blog" + a['href'])

print(lines_txt)
with open("links.txt", 'w') as f:
    for line in lines_txt:
        f.write(line)
        f.write('\n')
