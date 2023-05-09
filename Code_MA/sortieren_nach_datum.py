# Notwendige Pakete werden importiert:
import xml.dom.minidom
import os
import shutil

# der Pfad zu den Dateien wird definiert:
pfad = r"pfad\zu\dateien\\" 
os.chdir(pfad)

# es wird über die Dateien iteriert und sie werden geparst:
for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 
        domtree= xml.dom.minidom.parse(f)
        group= domtree.documentElement
 
# es wird nach dem Element <origDate> gesucht, in dem das Entstehungsdatum steht:
        daten = group.getElementsByTagName('origDate')
# es wird über alle <origDate>-Elemente iteriert:
        for datum in daten:
            datum = datum.getAttribute('when')
# es werden Bedingungen definiert: wenn das Datum nach dem 31.12.1918 kommt, wird die Datei in den Ordner 'nach1918' verschoben: 
            if datum > "1918-12-31":
                shutil.move(pfad + datei, "nach1918")
# wenn das Datum vor dem 31.12.1913 kommt, wird die Datei in den Ordner 'vor1914' verschoben: 
            elif datum < "1913-12-31":
                shutil.move(pfad + datei, "vor1914")
# die Dateien, die keine der Bedingungen erfüllen, bleiben, wo sie waren:
            else:
                break
