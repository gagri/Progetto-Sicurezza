import os
import parserManifest
import VerificaCaricamentoDinamico

import sys

#path della directory contenete tutte le app
#dir= "/Users/grima/Desktop/Materiale2"
dir=sys.argv[1]

#dir = "D:\Apk_Dec1-1199"


secondo = False # serve per vedere se ho preso il secondo file in modo da poter fare la differenza


for item in os.listdir(dir): #cicla per ogni elemento di quella cartella, senza vedere le eventuali sotto cartelle
    itemfullpath = os.path.join(dir, item) #ottengo percorso completo
    print(itemfullpath)
    percorsifilejar = []
    percorsidirectory = []
    for i in os.listdir(itemfullpath): #scorro la sottocartella
        ifullpath = os.path.join(itemfullpath, i)
        #print(ifullpath)

        '''
        if i.endswith(".jar"): #salvo il percorso dei file jar che trovo in una lista, i primi due (dovrebbero sempre essere solo due) li passo come parametro per il confronto delle dipendenze
            print("da implementare")
        '''

        #salvo il percorso delle sottodirectory che trovo in una lista, le prime due ( dovrebbero sempre essere solo due) le passo come parametri per la verifica del caricamento dinamico
        if os.path.isdir(os.path.join(itemfullpath, i)):
            #print("cartella")
            percorsidirectory.append(ifullpath)


    print
    print 'prime due cartelle ottenute:'
    print percorsidirectory[0]
    print percorsidirectory[1]
    print

    coppiaManifest = parserManifest.coppiaManifest(os.path.join(percorsidirectory[0], "AndroidManifest.xml"),
                                                   os.path.join(percorsidirectory[1], "AndroidManifest.xml"))
    print 'differenza permessi:'
    differenzaPermessi = coppiaManifest.differenzaPermessi()
    print differenzaPermessi
    print
    print "differenza activity:"
    differenzaActivity = coppiaManifest.differenzaActivity()
    print differenzaActivity
    print

    vcd = VerificaCaricamentoDinamico.CaricamentoDinamico(percorsidirectory[0], percorsidirectory[1])
    print 'risultato VerificaCaricamentoDinamico:'
    for a in vcd:
        print(a)
    print
    print
    print








'''
#Esplora tutte le directory a partire dal path specificato (walk)
for root, dirs, files in os.walk(dir, topdown=False):


 
    # cerca tutti i file e stampa nel caso trova i file chiamatai AndroidManifest.xml
    for f in files:
        if f.endswith("AndroidManifest.xml"):
            path = os.path.join(root, f) #ottengo il path completo del file trovato
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

