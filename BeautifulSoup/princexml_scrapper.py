import requests
from bs4 import BeautifulSoup

url = 'https://www.princexml.com/samples/'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = [ a['href'] for a in soup.find_all('a',href=True) if a['href'].endswith('.pdf') ]
    print(f"PDF Links extracted from the URL: {pdf_links}")
    titles = [ title.text.strip() for title in soup.find_all('h2') ]
    print(f"Extracted Sub-Headings from the webpage: {titles}")
    headings = [ heading.text.strip() for heading in soup.find_all('h1',class_="subpages-heading2") ]
    print(f"Tile of the page: {headings}")
    meta_name_descriptions = [ meta['content'] for meta in soup.find_all('meta', attrs={'name':'description'}) ] 
    print(f"Extracted from meta: {meta_name_descriptions}")
 
else:
    print(f"Connection error: {response.status_code}")

