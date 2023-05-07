# den Ordner HS vorher machen, auf derselben Ebene mit den Dateien

import xml.dom.minidom
import os
import shutil

pfad = r"pfad\zu\dateien\\"
os.chdir(pfad)

for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 
        domtree= xml.dom.minidom.parse(f)
        group= domtree.documentElement
        autoren = group.getElementsByTagName('correspAction')
        
        for autor in autoren:
            name = autor.getElementsByTagName('surname')[0].childNodes[0].nodeValue
            if autor.getAttribute('type') == 'sent' and name == 'Schuchardt':
                shutil.move(pfad + datei, "HS")
            else:
                break    
