# Code fürs Extrachieren von GermanPolarityClues
# der Vorgang muss für die negativen Wörter wiederholt werden

# das csv-Modul wird importiert:
import csv

# das Lexikon wird als Liste eingelesen:
with open(r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\GermanPolarityClues-2012(1)\GermanPolarityClues-2012\positiv.csv", newline='', encoding='utf-8') as f:
    clues_pos = csv.reader(f, delimiter=';')

# Liste wird angelegt:      
    liste_pos=[]

# über das Lexikon wird iteriert und Elemente werden der genannten Liste zugeordnet:
    for zeile in clues_pos:
        woerter_pos=zeile[0]
        liste_pos.append(woerter_pos)

# Listen werden angelegt:        
    liste_pos_leer=[]
    liste_pos_wort=[]

# über das Lexikon wird iteriert und Elemente werden der genannten Liste zugeordnet:
    for wort in liste_pos:
        if ' ' in wort:
            liste_pos_leer.append(wort)
        else:
            liste_pos_wort.append(wort)

# die Liste wird in einer Datei gespeichert:
with open(r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\GermanPolarityClues-2012(1)\GermanPolarityClues-2012\code_test\clues_pos.txt", 'w', encoding='utf-8') as fh_out:
    for wort in liste_pos_wort[1:]:    
        fh_out.write("%s\n" % wort)