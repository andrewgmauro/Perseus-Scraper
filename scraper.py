#For Parsing Perseus.com text files in bulk and identifying meter#


# 

#longv = ("?", "?", "?", "?", "?")
#longv = ()


#shortv = ("?", "?", "?", "?", "?")
#shortv = ()

from bs4 import BeautifulSoup
import requests

#Identifies target URL#
url = input('Enter a Perseus webpage:')

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml') #Stores URL HTML in a variable#

body = soup.find('div', class_ = 'text') #Isolates div class which contains the target body of text#

#words = body.find_all('a') #Stores all words in variable#

fulltext_list = []

for word in body.contents:
      if word.find('<a') != -1:
            fulltext_list.append(word.text)
      if word.find('<br>') != -1:
            fulltext_list.append('\r')
      else:
            fulltext_list.append(word)

fulltext = ''.join(fulltext_list)

n_file_name = soup.find('title').text #opens new file and defines name#

file_name = n_file_name.replace('\n', '')

#print(file_name)
file = open(file_name, mode = 'w', encoding = 'utf-8-sig')
file.write(fulltext)
file.close()