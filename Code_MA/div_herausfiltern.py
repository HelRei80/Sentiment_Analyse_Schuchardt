import os
import bs4         
import lxml        
from bs4 import BeautifulSoup as bs

pfad = r"pfad\zu\Dateien\\"
os.chdir(pfad)

for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 

        with open (f, encoding = "utf-8") as fh:
            content = fh.read ()
            content= ''.join(content)
            bs_content = bs(content, 'lxml')
           
            for div in bs_content.find_all('div'): 
                with open (datei, "w", encoding = "utf-8") as fh_out: 
                    # macht eine neue Datei (der Name ändert sich nicht) und speichert nur das div-Element hinein
                    fh_out.write(str(div))