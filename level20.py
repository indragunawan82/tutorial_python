
#cara install BeautifulSoup
#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup

html = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.h1.text)
