# die notwendigen Ordner schon vorher machen, auf derselben Ebene wie die Dateien
# es werden die notwendigen Pakete importiert:
import xml.dom.minidom
import os
import shutil

#der Pfad zu den Dateien wird festgelegt
pfad = r"pfad\zu\dateien\\" 
os.chdir(pfad)

#es wird über die Dateien iteriert und nach dem Element <div> gesucht: 
for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 
        domtree = xml.dom.minidom.parse(f)
        group = domtree.documentElement
        sprachen = group.getElementsByTagName('div')
# es wird über alle <div>-Elemente iteriert und das Attribut @xml:lang geprüft; 
# wenn es den Wert 'de' hat, wird die Datei in den Ordner "de" verschoben, wenn es den Wert 'fr' hat, wird die Datei in den Ordner "fr" verschoben usw.

        for sprache in sprachen:
            if sprache.getAttribute("xml:lang") == "de":
                shutil.move(pfad + datei, "de")          
            elif sprache.getAttribute("xml:lang") == "fr":
                shutil.move(pfad + datei, "fr")
            elif sprache.getAttribute("xml:lang") == "it":
                shutil.move(pfad + datei, "it")
            elif sprache.getAttribute("xml:lang") == "es":
                shutil.move(pfad + datei, "es")
 # die Dateien, die keine der Bedingungen erfüllen, werden in den Ordner 'rest' verschoben:
            else:
                shutil.move(pfad + datei, "rest")

