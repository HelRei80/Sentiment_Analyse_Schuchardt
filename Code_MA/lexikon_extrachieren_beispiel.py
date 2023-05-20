# angewendet auf das SentiWS, bei Wörterbüchern in einem anderen Format sind Anpassungen notwendig
zahlen =[]
woerter=[]

# die Datei wird eingelesen, das Lexikon wird in eine Liste umgewandelt, über sie wird iteriert und die Zahlen werden vom Rest getrennt
with open(r"pfad\dateiname.txt", encoding='utf-8') as fh:
    sentiment_dict_pos = fh.readlines()
    lexikon=' '.join(sentiment_dict_pos)
    lexikon_liste=lexikon.split()
    for element in lexikon_liste:
        if element.startswith('0') or element.startswith('-0'):
            zahlen.append(element)
        else:
            woerter.append(element)

# da der Besitrich als Trennzeichen dient, werden alle einzelnen Teile durch Beistriche getrennt und in zwei Listen geteilt - eine ohne Pipezeichen und eine mit
nur_woerter=','.join(woerter)
nur_woerter_liste=nur_woerter.split(',')
mit_strich =[]
ohne_strich=[]
for element in nur_woerter_liste:
    if '|' in element:
        mit_strich.append(element)
    else:
        ohne_strich.append(element)
   
# die Liste ohne Pipezeichen wird in einer Datei gespeichert, die Liste mit Pipezeichen muss weiter bearbeitet werden
with open(r"pfad\dateiname_pos.txt", 'w', encoding='utf-8') as fh_out:
    for wort in ohne_strich:    
         fh_out.write("%s\n" % wort)
mit_strich_string='|'.join(mit_strich)
mit_strich_liste=mit_strich_string.split('|')

# die Liste mit Pipezeichen wird in zwei geteilt - eine mit Wortarten und eine mit Wörtern
wortart =[]
wort_liste=[]
for element in mit_strich_liste:
    if element == 'NN' or element=='VVINF' or element=='ADJX':
        wortart.append(element)
    else:
        wort_liste.append(element)
      
# die Liste mit Wörtern wird der schon existierenden Datei angefügt
with open(r"pfad\dateiname_pos.txt", 'a', encoding='utf-8') as fh_out:
    for wort in wort_liste:    
         fh_out.write("%s\n" % wort)



