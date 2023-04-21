import bs4         
import lxml        
from bs4 import BeautifulSoup as bs
import os


pfad = r"pfad\zu\dateien\\" 
os.chdir(pfad)

gruesse=[]
gruss_counter = {}

for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 

        with open (f, encoding = "utf-8") as fh:
            content = fh.read ()
            content= ''.join(content)
            bs_content = bs(content, 'lxml')
            for anrede in bs_content.find_all('opener'):
                gruss_formel = anrede.text
                gruss_formel_ohne = gruss_formel.replace('!', '').replace(',', '').replace('.', '').replace(';', '').replace(':', '').replace('*)', '').replace('-', '').strip()
                for gruss in gruss_formel_ohne:
                    gruesse.append(gruss)
                    for gruss1 in gruesse:
                        gruss_counter[gruss1] = gruss_counter.get(gruss1, 0) + 1
                        s_gruss_counter = sorted(gruss_counter.items(), key=lambda name_counter: name_counter[1], reverse=True)
                        for key, value in s_gruss_counter:
                            print("{}: {}".format(value, key))