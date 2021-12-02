import requests
from bs4 import BeautifulSoup
import re
import csv
import bleach
import lxml.html.clean as clean

fileName = "links.txt"
fileObj = open(fileName, "r") #opens the file in read mode
words = fileObj.read().splitlines() #puts the file into an array
fileObj.close()
# print(words)

myheaders = ['Content']
lines_word_list = [[]]

x1 = 0
for word_list in words:
    if x1 < 20:
        URL = word_list
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        # results = soup.find(id="section_1611241893681_301")
        content_elements = soup.find_all("div", class_="learnworlds-section-content")
        content_elements_str = str(content_elements)
        content_elements_str = content_elements_str.replace(">,", ">")
        content_elements_str = content_elements_str.replace('"', "'")
        content_elements_str = content_elements_str.replace("&amp;", "")
        content_elements_str = content_elements_str.replace(";", "")
        content_elements_str = content_elements_str.replace(",", "{COMMA}")
        content_elements_str = content_elements_str.strip()
        content_elements_str = content_elements_str.replace('\n', ' ').replace('\r', '')
        print(content_elements_str)

        # code = '<tr id="ctl00_Content_AdManagementPreview_DetailView_divNova" class="Extended" style="display: none;">'
        safe_attrs = clean.defs.safe_attrs
        # cleaner = clean.Cleaner(safe_attrs_only=True, safe_attrs=frozenset(['src', 'embed', 'iframe']))
        cleaner = clean.Cleaner(safe_attrs_only=False)
        cleansed_content_elements_str = cleaner.clean_html(content_elements_str)
        cleansed_content_elements_str = cleansed_content_elements_str.replace('"', "'")
        cleansed_content_elements_str = cleansed_content_elements_str.replace("&amp;", "")
        cleansed_content_elements_str = cleansed_content_elements_str.replace(";", "")
        cleansed_content_elements_str = cleansed_content_elements_str.strip()

        lines_word_list[0].append(cleansed_content_elements_str)
        lines_word_list.append([])
        lines_word_list[1].append(URL)
        # print(cleansed_content_elements_str)
        # print(URL)

        # print(content_elements_str)
        # print('\n')
        x1=x1+1



x2 = 0;
for lines in lines_word_list:
    print(x2)
    x2=x2+1

print(lines_word_list)

with open("tester.txt", 'w', encoding="utf-8") as f:
    for line in lines_word_list:
        line_str = str(line)
        line_str = line_str.replace(">,", ">")
        line_str = line_str.replace('"', "'")
        line_str = line_str.strip()
        line_str = line_str.replace('\n', ' ').replace('\r', '')
        f.write(line_str)
        f.write('\n')
        f.write('\n')

import pandas as pd

df = pd.DataFrame({'post_content':lines_word_list[0], 'post_url':lines_word_list[1]})
df.to_csv('content_scraped.csv', index=False)
