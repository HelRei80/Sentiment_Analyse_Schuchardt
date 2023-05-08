# angewendet auf das SentiWS, bei Wörterbüchern in einem anderen Format sind Anpassungen notwendig
zahlen =[]
woerter=[]


with open(r"pfad\dateiname.txt", encoding='utf-8') as fh:
    sentiment_dict_pos = fh.readlines()
    lexikon=' '.join(sentiment_dict_pos)
    lexikon_liste=lexikon.split()
    for element in lexikon_liste:
        if element.startswith('0') or element.startswith('-0'):
            zahlen.append(element)
        else:
            woerter.append(element)
nur_woerter=','.join(woerter)
nur_woerter_liste=nur_woerter.split(',')
mit_strich =[]
ohne_strich=[]
for element in nur_woerter_liste:
    if '|' in element:
        mit_strich.append(element)
    else:
        ohne_strich.append(element)
with open(r"pfad\dateiname_pos.txt", 'w', encoding='utf-8') as fh_out:
    for wort in ohne_strich:    
         fh_out.write("%s\n" % wort)
mit_strich_string='|'.join(mit_strich)
mit_strich_liste=mit_strich_string.split('|')
wortart =[]
wort_liste=[]
for element in mit_strich_liste:
    if element == 'NN' or element=='VVINF' or element=='ADJX':
        wortart.append(element)
    else:
        wort_liste.append(element)
with open(r"pfad\dateiname_pos.txt", 'a', encoding='utf-8') as fh_out:
    for wort in wort_liste:    
         fh_out.write("%s\n" % wort)



