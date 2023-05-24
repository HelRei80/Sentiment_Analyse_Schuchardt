# Code fürs Extrachieren von SentiMerge

# das Modul für reguläre Ausdrücke wird importiert:

import re

# Funktion, die Listen in Dateien speichert:
def make_lex_file(lex_list, filename):
    with open(filename, 'w', encoding='utf-8') as fh_out:
        for wort in lex_list:    
            lex = fh_out.write("%s\n" % wort)
    return lex

# das Lexikon wird als Liste eingelesen:
with open(r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\alt\SentiMerge_emerson.txt", encoding='utf-8') as fh_out:
    liste=fh_out.readlines()

# Listen werden angelegt:
    woerter_pos =[]
    woerter_neg=[]
    rest = []

# über das Lexikon wird iteriert und Elemente werden den genannten Listen zugeordnet:
    for element in liste:
        if '-0.' in element or '-1.' in element:
            woerter_neg.append(element)
        elif element =='lemma' or element == 'PoS' or element =='sentiment' or element =='weight':
            rest.append(element)
        else:
            woerter_pos.append(element)

# aus Listen werden Strings und umgekehrt gemacht:
    lexikon_neg=' '.join(woerter_neg)
    lexikon_liste_neg=lexikon_neg.split('\t')
    lexikon_neg2=' '.join(lexikon_liste_neg)
    lexikon_liste_neg2=lexikon_neg2.split()

    lexikon_pos=' '.join(woerter_pos)
    lexikon_liste_pos=lexikon_pos.split('\t')
    lexikon_pos2=' '.join(lexikon_liste_pos)
    lexikon_liste_pos2=lexikon_pos2.split()

# Listen werden angelegt:
    wortart_neg=[]
    zahl_neg=[]
    wort_neg=[]

    wortart_pos=[]
    zahl_pos=[]
    wort_pos=[]


# über die Listen wird iteriert und Elemente werden den genannten Listen zugeordnet:
    for el in lexikon_liste_neg2:
        if re.search('[A-Z]', el):
            wortart_neg.append(el)
        elif re.search('-?\d\.\d*', el):
            zahl_neg.append(el)
        else:
            wort_neg.append(el)
 
    for el in lexikon_liste_pos2:
        if re.search('[A-Z]', el):
            wortart_pos.append(el)
        elif re.search('-?\d\.\d*', el):
            zahl_pos.append(el)
        else:
            wort_pos.append(el)

# die Liste wird in einer Datei gespeichert:
lex_pos = make_lex_file(wort_neg, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\alt\code_test\merge_pos.txt")
lex_neg = make_lex_file(wort_pos, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\alt\code_test\merge_neg.txt")


