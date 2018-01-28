#For Parsing Perseus.com text files in bulk and identifying meter#


# 

#longv = ("ᾱ", "η", "ῑ", "ω", "ῡ")
#longv = ()


#shortv = ("α", "ε", "ι", "ο", "υ")
#shortv = ()

from bs4 import BeautifulSoup
from requests import get

url = 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0135%3Abook%3D1%3Acard%3D1'

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

greektext = html_soup.find_all('div', class_ = 'text_container greek')

word1 = greektext.find('a', class_ = 'text')
word1 = int(word1.text)

print(len(word1))

#for word in words:
 #   if "morph" in word:
      #  print(word.text)
