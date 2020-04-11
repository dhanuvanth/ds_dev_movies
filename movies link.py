from bs4 import BeautifulSoup
import requests
from time import sleep
import re

url = 'http://103.133.204.82/Data/Disk2/English%20Movie/'
name = list()
links = list()
years = list()
# output = open('movies_list.txt', 'a')  # a - append
# out_name = open('movies_name.txt', 'a')

webpage = requests.get(url)  # also use .text at last
# print(webpage.status_code) # response should be 200

# no need of .context if .text is add
soup = BeautifulSoup(webpage.content, 'lxml')
for item in soup.findAll('a')[1:]:
    currentLink = item['href']  # get all links
    year = item.text  # get text of links and add to list
    # output.write("\n" + item.text + "\n") # write it in a file

    webpage = requests.get(url + currentLink)
    # print(webpage.status_code)
    soup = BeautifulSoup(webpage.content, 'lxml')
    for item in soup.findAll('a')[1:]:
        currentLink = item['href']
        links.append(str(currentLink))  # get text of links and add to list
        name.append(item.text)  # get text of links and add to list
        print(item.text)
        # output.write(year + '-' + item.text + "-" + currentLink + "\n")
        # out_name.write(item.text + "\n")
# output.close()
# out_name.close()

# output = open('movies_list.txt', 'r+')  # read the file
# print(output.read())
# output.close()

# out_name = open('movies_name.txt', 'r+')  # read the file
# print(out_name.read())
# output.close()
