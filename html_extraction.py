from bs4 import BeautifulSoup
import requests


def dataset_extraction(html_page):
    site_2 = html_page
    hdr_2 = {'User-Agent': 'Mozilla/5.0'}
    page_2 = requests.get(site_2, headers=hdr_2)
    soup_2 = BeautifulSoup(page_2.content, 'html.parser')
    print(soup_2.find_all('p')[1].get_text())


def year_webpage_extraction(year):
    site_1 = year
    hdr_1 = {'User-Agent': 'Mozilla/5.0'}
    page_1 = requests.get(site_1, headers=hdr_1)
    soup_1 = BeautifulSoup(page_1.content, 'html.parser')
    webpages_subdivisions_1 = []
    for element_1 in soup_1.find_all('a', href=True):
        site_dummy = site_1.replace("https://www.bailii.org", "")
        if element_1['href'].startswith(site_dummy):
            element_2 = element_1['href'].split('/')
            new_site = site_1 + element_2[-1]
            webpages_subdivisions_1.append(new_site)
        # print("Found the URL:", a['href'])
    webpages_subdivisions_1 = list(set(webpages_subdivisions_1))
    print(webpages_subdivisions_1)
    for element in webpages_subdivisions_1:
        dataset_extraction(element)


if __name__ == '__main__':
    site_0 = "https://www.bailii.org/ew/cases/EWCC/Fam/"
    hdr_0 = {'User-Agent': 'Mozilla/5.0'}
    page_0 = requests.get(site_0, headers=hdr_0)
    soup_0 = BeautifulSoup(page_0.content, 'html.parser')
    # print(soup.prettify())
    webpages_subdivisions_0 = []
    for element_1 in soup_0.find_all('a', href=True):
        site_dummy = site_0.replace("https://www.bailii.org", "")
        if element_1['href'].startswith(site_dummy) and element_1['href'].endswith('/'):
            element_2 = element_1['href'].split('/')
            new_site = site_0 + element_2[-2] + '/'
            webpages_subdivisions_0.append(new_site)
    print(webpages_subdivisions_0)
    for element in webpages_subdivisions_0:
        year_webpage_extraction(element)
