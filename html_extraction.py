from bs4 import BeautifulSoup
import requests

site = "https://www.bailii.org/ew/cases/EWCC/Fam/2014/B79.html"
hdr = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(site, headers=hdr)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
list(soup.children)
parameters = [type(item) for item in list(soup.children)]
# print(parameters)
html = list(soup.children)[1]
# print(list(html.children))
print(soup.find_all('p')[1].get_text())
pass