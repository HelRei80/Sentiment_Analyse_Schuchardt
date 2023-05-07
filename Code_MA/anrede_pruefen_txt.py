import os
from bs4 import BeautifulSoup as bs

pfad = r"pfad\zu\datei"
os.chdir(pfad)

for datei in os.listdir(pfad):
    
    f = os.path.join(pfad, datei) 
    name, endung = datei.split('.')
    if os.path.isfile(f): 
        with open (f, encoding = "utf-8") as fh: 
            content = fh.read ()
            content= ''.join(content)
            bs_content = bs(content, 'lxml')
            brief = bs_content.text
            for div in bs_content.find_all('opener'): 
                if 'Freund' in div.text:
                    with open (f'{name}.txt', "w", encoding = "utf-8") as fh_out: 
                        fh_out.write(brief)