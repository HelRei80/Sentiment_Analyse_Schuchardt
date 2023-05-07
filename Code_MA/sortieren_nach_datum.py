# den Ordner "nach1918" schon vorher machen, auf derselben Ebene wie die Dateien

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
        daten = group.getElementsByTagName('origDate')
        for datum in daten:
            datum = datum.getAttribute('when')
            if datum > "1918-12-31":
                shutil.move(pfad + datei, "nach1918")
            else:
                break
