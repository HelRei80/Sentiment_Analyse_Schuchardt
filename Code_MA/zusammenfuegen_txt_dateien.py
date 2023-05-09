# es werden norwendige Pakete importiert:

import os

# der Pfad zu den Dateien wird definiert:
pfad = r"pfad\zu\dateien\\"
os.chdir(pfad)

# es wird über die Dateien iteriert, die Dateien werden  eingelesen und anschließend in einer anderen Datein angehängt:
for datei in os.listdir(pfad): 
    f = os.path.join(pfad, datei) 
    if os.path.isfile(f): 
        with open (f, encoding = "utf-8") as fh: 
            content = fh.read ()                  
            with open ('dateiname.txt', "a", encoding = "utf-8") as fh_out: 
                fh_out.write(content)
