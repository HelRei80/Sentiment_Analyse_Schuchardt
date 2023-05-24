# Code fürs Extrachieren von NRC
# im ersten Schritt wurden  die unnötigen Spalten und die erste Zeile händisch entfernt

# das csv-Modul wird importiert:
import csv

# Funktion, die Listen in Dateien speichert:
def make_lex_file(lex_list, filename):
    with open(filename, 'w', encoding='utf-8') as fh_out:
        for wort in lex_list:    
            lex = fh_out.write("%s\n" % wort)
    return lex

# Funktion, die eine Liste in eine Menge umwandelt:
def make_set(liste):
    lex_set = sorted(set(liste))
    return lex_set

# Funktion, die eine Menge in eine Liste umwandelt:
def make_list(set):
    lex_list = list(set)
    return lex_list

# das Lexikon wird als Liste eingelesen:
with open(r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\NRC\NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations_mohammad.csv", newline='', encoding='utf-8') as f:
    liste = csv.reader(f, delimiter=';')

# Listen werden angelegt:    
    komplex_liste=[]
    liste_neg=[]
    liste_pos=[]

# über das Lexikon wird iteriert und Elemente werden den genannten Listen zugeordnet:
    for zeile in liste:
        if ' ' in zeile[0] or zeile[0]=='NO TRANSLATION':
            komplex_liste.append(zeile[0])
        elif zeile[1] == '0' and zeile[2]=='1': 
            liste_neg.append(zeile[0])
        elif zeile[1]=='1' and zeile[2]=='0':
            liste_pos.append(zeile[0])

# aus Listen werden Mengen gemacht, damit  doppelte Vorkommnisse vermieden werden, was wegen der Übersetzung möglich ist: 
lex_pos_set = make_set(liste_pos)
lex_neg_set = make_set(liste_neg)


# aus Mengen werden Listen gemacht: 
pos_liste = make_list(lex_pos_set)
neg_liste = make_list(lex_neg_set)

# die Listen werden in Dateien gespeichert:
lex_pos = make_lex_file(pos_liste, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\NRC\code_test\NRC_pos.txt")
lex_neg = make_lex_file(neg_liste, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\NRC\code_test\NRC_neg.txt")

