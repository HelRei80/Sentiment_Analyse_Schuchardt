# Code fürs Extrachieren von polArt


# Funktion, die einen String in eine Liste umwandelt:
def make_list(lex_string):
    lex_list = lex_string.split()
    return lex_list

# Funktion, die eine Liste in einen String umwandelt:
def make_string(lex_list):
    lex_string = ' '.join(lex_list)
    return lex_string

# Funktion, die Listen in Dateien speichert:
def make_lex_file(lex_list, filename):
    with open(filename, 'w', encoding='utf-8') as fh_out:
        for wort in lex_list:    
            lex = fh_out.write("%s\n" % wort)
    return lex

# das Lexikon wird als Liste eingelesen:
with open(r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\polart_lexicon\polartlexicon.txt", encoding='utf-8') as fh:
    sentiment_dict = fh.readlines()

# Listen werden angelegt:
polart_neg=[]
polart_pos=[]

# über das Lexikon wird iteriert und Elemente werden den genannten Listen zugeordnet:
for line in sentiment_dict:
    if 'NEG' in line:
        polart_neg.append(line)
    elif 'POS' in line: 
        polart_pos.append(line)

# aus Listen werden Strings gemacht: 
lexikon_neg=make_string(polart_neg)
lexikon_pos=make_string(polart_pos)

# aus Strings werden Listen gemacht
lexikon_liste_neg=make_list(lexikon_neg)
lexikon_liste_pos=make_list(lexikon_pos)

# Listen werden angelegt:
wort_neg =[]
wort_pos=[]
rest_neg=[]
rest_pos=[]

# über die Listen wird iteriert und Elemente werden den genannten Listen zugeordnet:
for el_neg in lexikon_liste_neg:
    if el_neg.startswith('NEG=') or el_neg=='adj' or el_neg=='nomen' or el_neg=='verben' :
        rest_neg.append(el_neg)
    else:
        wort_neg.append(el_neg)

for el_pos in lexikon_liste_pos:
    if el_pos.startswith('POS=') or el_pos=='adj' or el_pos=='nomen' or el_pos=='verben':
        rest_pos.append(el_pos)
    else:
        wort_pos.append(el_pos)

# die Listen werden in Dateien gespeichert:
lex_pos = make_lex_file(wort_neg, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\polart_lexicon\code_test\polart_neg.txt")
lex_neg = make_lex_file(wort_pos, r"C:\Users\helen\Meine Dokumente\Helena\Universität\Fächer\Masterarbeit\Lexikon\polart_lexicon\code_test\polart_pos.txt")
