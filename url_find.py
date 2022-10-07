import re
import requests
url = input("Enter your website: ")
req = requests.get(url, 'html.parser')
s = req.text
# file = open("D:\\file.txt",'r')
# data = file.read()
ptt = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
list = re.findall(ptt,s)
# u = 'https://www.chevrolet.ca/en/performance/camaro'
u = 'https://www.craw.in/blog/'
for i in list:
    if u == i[0]:
        with open("E://linksFromUrl.txt",'a') as file:
            file.write(f'{i[0]}\n')
