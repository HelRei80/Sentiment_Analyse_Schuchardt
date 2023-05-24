# Code fürs Extrachieren von BAWL_R
# im ersten Schritt wurden die unnötigen Spalten händisch entfernt

# das csv-Modul wird importiert
import csv

# Funktion, die Listen in Dateien speichert:
def make_lex_file(lex_list, filename):
    with open(filename, 'w', encoding='utf-8') as fh_out:
        for wort in lex_list:    
            lex = fh_out.write("%s\n" % wort)
    return lex

# das Lexikon wird als Liste eingelesen:
with open(r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\BAWL-R\BAWL-R.csv", newline='', encoding='utf-8') as f:
    liste = csv.reader(f, delimiter=';')

# Listen werden angelegt:
    liste_pos=[]
    liste_neg=[]
    liste_neu=[]

# über das Lexikon wird iteriert und Elemente werden den genannten Listen zugeordnet:
    for zeile in liste:
        if zeile[1].startswith('-'):
            liste_neg.append(zeile[0])
        elif zeile[1] == '0':
            liste_neu.append(zeile[0])
        else:
            liste_pos.append(zeile[0])

# die Listen werden in Dateien gespeichert:
lex_pos = make_lex_file(liste_pos, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\BAWL-R\code_test\BAWL_R_pos.txt")
lex_neg = make_lex_file(liste_neg, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\BAWL-R\code_test\BAWL_R_neg.txt")

