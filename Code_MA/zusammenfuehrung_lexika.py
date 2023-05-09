# Funktion, die Dateien einliest:

def read_lex (filename):
    with open(filename, encoding='utf-8') as fh:
        lex = fh.readlines()
        return lex
# Funktion, die eine Liste in eine Menge umwandelt:

def make_set(liste):
    lex_set = set(liste)
    return lex_set

# Funktion, die eine Menge in eine Liste umwandelt:

def make_list(set):
    lex_list = list(set)
    return lex_list

# Funktion, die eine Liste in einer TXT-Datei speichert:

def make_lex_file(lex_list, filename):
    with open(filename, 'w', encoding='utf-8') as fh_out:
        for wort in lex_list:    
            lex = fh_out.write(wort)
    return lex

# Einlesen der positiven und negativen Listen (Anzahl der Listen kann angepasst werden, hier kommen zwei positive und zwei negative Listen vor):
lex_pos_1 = read_lex(r"datei1.txt")
lex_neg_1 = read_lex (r"datei2.txt")
lex_pos_2 = read_lex(r"datei3.txt")
lex_neg_2 = read_lex(r"datei4.txt")


# Umwamdeln von Listen in Mengen: 
lex_pos_set_1 = make_set(lex_pos_1)
lex_neg_set_1 = make_set(lex_neg_1)
lex_pos_set_2 = make_set(lex_pos_2)
lex_neg_set_2 = make_set(lex_neg_2)

# Zusammenführen von Mengen:
set_pos_alle = lex_pos_set_1 | lex_pos_set_2
set_neg_alle = lex_neg_set_1 | lex_neg_set_2

# Kontrolle, ob es Wörter gibt, die auf beiden Listen zu finden sind:
set_doppelt = set_pos_alle.intersection(set_neg_alle)

# Entfernen von doppelt vorkommenden Wörtern: 
set_pos_alle_2 = set_pos_alle - set_doppelt
set_neg_alle_2 = set_neg_alle - set_doppelt

# Umwandeln von sortierten Mengen in Listen
list_pos_alle = make_list(sorted(set_pos_alle_2))
list_neg_alle = make_list(sorted(set_neg_alle_2))

# Speichern der Listen in die TXT-Dateien:
lex_pos = make_lex_file(list_pos_alle, "lex_pos.txt")
lex_neg = make_lex_file(list_neg_alle, "lex_neg.txt")

