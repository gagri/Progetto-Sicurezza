import os
import fnmatch
import parserManifest

import sys
#A partire dal path specificato in dir, il programma stampa per ogni coppia
#di App il numero di file contenuti nella directory res di ognuna delle due applicazioni

#Passare la directory a riga di comando! secondo me è più conveniente scrivere il path iniziale direttamente nello script

#path della directory contenete tutte le app
#dir= "/Users/grima/Desktop/Materiale2"
#dir=sys.argv[1]

dir = "D:\Apk_Dec1-1199"


secondo = False # serve per vedere se ho preso il secondo file in modo da poter fare la differenza


for item in os.listdir(dir): #cicla per ogni elemento di quella cartella, senza vedere le eventuali sotto cartelle
    itemfullpath = os.path.join(dir, item) #ottengo percorso completo
    print(itemfullpath)
    for i in os.listdir(itemfullpath): #altra sottocartella
        ifullpath = os.path.join(itemfullpath, i)
        print(ifullpath)

        filejar= []
        if i.endswith(".jar"): #salvo il percorso dei file jar che trovo in un array, i primi due (dovrebbero sempre essere solo due) li passo come parametro per il confronto delle dipendenze
            print("fle jar")

        '''
        if os.path.isdir(os.path.join(itemfullpath, i)): #serve per controllare se l'elemento è una cartella
            print()
        '''





'''
#Esplora tutte le directory a partire dal path specificato (walk)
for root, dirs, files in os.walk(dir, topdown=False):


 
    # cerca tutti i file e stampa nel caso trova i file chiamatai AndroidManifest.xml
    for f in files:
        if f.endswith("AndroidManifest.xml"):
            path = os.path.join(root, f) #ottengo il path completo del file trovato
            # PATCH DA DISCUTERE, il problema è che esiste un file xml nella cartella original che però non è ben formattato e che quindi da errore
            if "original" not in path:
                if secondo == False:
                    path0 = path
                    secondo = True
                else:
                    print(path0)
                    print(path)

                    coppiaManifest = parserManifest.coppiaManifest(path0, path)
                    print("differenza permessi:")
                    differenzaPermessi = coppiaManifest.differenzaPermessi()
                    print(differenzaPermessi)
                    print("differenza activity:")
                    differenzaActivity = coppiaManifest.differenzaActivity()
                    print(differenzaActivity)

                    print()
                    secondo = False
               # print(*permessi,sep="\n")  # stampa tutta la lista senza parentesi e dividendo ogni oggetto della lista con il valore sep
    '''

