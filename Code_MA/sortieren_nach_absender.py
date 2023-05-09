# den Ordner HS vorher machen, auf derselben Ebene mit den Dateien
# notwendige Bibliotheken werden importiert:
import xml.dom.minidom
import os
import shutil

# Pfad zu den Dateien:
pfad = r"pfad\zu\dateien\\"
os.chdir(pfad)

# es wird über alle Dateien iteriert, sie werden geparst und es wird nach dem Element <correspAction> gesucht, das in der VAriable Autoren gespeichert wird:
for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 
        domtree= xml.dom.minidom.parse(f)
        group= domtree.documentElement
        autoren = group.getElementsByTagName('correspAction')
        
# es wird über jedes einzelne Element in der VAriable autoren iteriert und nach dem Inhalt des Elements <surname> gesucht:         
        for autor in autoren:
            name = autor.getElementsByTagName('surname')[0].childNodes[0].nodeValue
            
# es werden zwei Bedingungen definiert: das Attribut @type soll den Wert 'sent' haben und im Element <surname> soll Schuchardt stehen:
            if autor.getAttribute('type') == 'sent' and name == 'Schuchardt':
        
# wenn die Bedingungen erfüllt sind, wird die Datei in den Ordner 'HS' verschoben; ansonsten passiert nichts:
                shutil.move(pfad + datei, "HS")
            else:
                break    
