import os
import bs4         
import lxml        
from bs4 import BeautifulSoup as bs

pfad = r"pfad\zu\Dateien\\"
os.chdir(pfad)

i=1
for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 

        with open (f, encoding = "utf-8") as fh:
            content = fh.read ()
            content= ''.join(content)
            bs_content = bs(content, 'lxml')
           
            for name in bs_content.find_all(attrs={'type': 'received'}):
                korresp = name.text
                korresp1 = korresp.strip()
                korresp2 = korresp1.split()
                with open (f'{korresp2[-1]}_{i}.xml', "w", encoding = "utf-8") as fh_out: 
                    #der neue Name besteht aus dem Namen des Rezipienten und einer Nummer
                    fh_out.write(str(bs_content))
                    i+=1