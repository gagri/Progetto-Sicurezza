import os
import sys
#A partire dal path specificato in dir, il programma stampa per ogni coppia
#di App il numero di file contenuti nella directory res di ognuna delle due applicazioni

#Passare la directory a riga di comando! secondo me è più conveniente scrivere il path iniziale direttamente nello script

#path della directory contenete tutte le app
#dir= "/Users/grima/Desktop/Materiale2"
dir=sys.argv[1]

#Esplora tutte le directory a partire dal path specificato (walk)
for root, dirs, files in os.walk(dir, topdown=False):
    #Per ogni directory contenuta in dir
    for name in dirs:
       #aggiunge al path di partenza in nome della directory in cui si trova
       dir2= os.path.join(root, name)
       #se la directory termina con res 
       if dir2.endswith("res"):
           #conta tutti i file anche quelli presenti nelle sottodirectory
           file_c = sum(len(files) for _, _, files in os.walk(dir2))
           #stampa la directory
           print(dir2)
           #stampa il numero di files
           print(file_c)

