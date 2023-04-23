import xml.dom.minidom
import os
import shutil

pfad = r"pfad\zu\dateien\\" 
os.chdir(pfad)

for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 
        domtree = xml.dom.minidom.parse(f)
        group = domtree.documentElement
        sprachen = group.getElementsByTagName('div')
        for sprache in sprachen:
            if sprache.getAttribute("xml:lang") == "de":
                shutil.move(pfad + datei, "de")          
            elif sprache.getAttribute("xml:lang") == "fr":
                shutil.move(pfad + datei, "fr")
            elif sprache.getAttribute("xml:lang") == "it":
                shutil.move(pfad + datei, "it")
            elif sprache.getAttribute("xml:lang") == "es":
                shutil.move(pfad + datei, "es")
            else:
                shutil.move(pfad + datei, "rest")

