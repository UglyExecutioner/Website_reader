#Python Script to readout websites
import re
import requests
import pyperclip
import os
from gtts import gTTS
from bs4 import BeautifulSoup
def cleanhtml(raw):
        cleanr = re.compile(r'<.*?>')
        cleantext = re.sub(cleanr,'',raw)
        return cleantext
url = pyperclip.paste()
file1 = open("C:/Users/Ugly_Executioner/Desktop/thefile.txt","w")
check = re.compile(r'https://')
mo = check.search(url)
print(check)
print(mo.group())
no = mo.group(0)
print(no)

if no == 'https://':
        print(" url copied")
else:
        print(" no url copied")
        
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
#print(soup.prettify())
#text = soup.find_all(text=True)
#print(text)
#print('After text')
dam = []
output = ''

para = soup.find_all('p')
print(len(para))
paragraphy = str(para)
#print(paragraphy)
for i in range(len(paragraphy)):
        chunk = cleanhtml(paragraphy)
output +=chunk
print(output)        
        
language = 'en'
myobj = gTTS(text=output, lang=language, slow=False)
myobj.save("C:/Users/Ugly_Executioner/Desktop/recording.wav")
os.system("start C:/Users/Ugly_Executioner/Desktop/recording.wav")
   
