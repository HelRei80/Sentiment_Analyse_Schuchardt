import os
import bs4         
import lxml        
from bs4 import BeautifulSoup as bs

pfad = r"pfad\zu\dateien\\"
os.chdir(pfad)

for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 

        with open (f, encoding = "utf-8") as fh:
            content = fh.read ()
            content= ''.join(content)
            div = bs(content, 'lxml')
            for fremd in div.find_all('foreign'):
                fremd.decompose()  
                with open (datei, "w", encoding = "utf-8") as fh_out: 
                    fh_out.write(str(div))