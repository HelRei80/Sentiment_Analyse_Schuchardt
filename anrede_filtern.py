import bs4         
import lxml        
from bs4 import BeautifulSoup as bs
import os

pfad = r"pfad\zu\dateien\\"
os.chdir(pfad)

for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 

        with open (f, encoding = "utf-8") as fh:
            content = fh.read ()
            content= ''.join(content)
            bs_content = bs(content, 'lxml')
            for div in bs_content.find_all('opener'):
                print(div.text)