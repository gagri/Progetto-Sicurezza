import os
import parserManifest
import VerificaCaricamentoDinamico
import ricercaNew
import ComunicazioneDB
import contaFiles
import sys

#path della directory contenete tutte le app
#dir= "/Users/grima/Desktop/Materiale2"
#dir=sys.argv[1]

#dir = "D:\Apk_Dec1-1199"
import datetime
import time

#cartella gia' analizzata
#dir="/media/lucio/HDAure/Dataset_Visaggio_Progetto/ApkDec2400"
dir="/media/lucio/HDAure/Dataset_Visaggio_Progetto/ApkDec2400"

for item in os.listdir(dir): #cicla per ogni elemento di quella cartella, senza vedere le eventuali sotto cartelle
    itemfullpath = os.path.join(dir, item) #ottengo percorso completo
    #print(itemfullpath)
    percorsifilejar = []
    percorsidirectory = []
    for i in os.listdir(itemfullpath): #scorro la sottocartella
        ifullpath = os.path.join(itemfullpath, i)
        #print(ifullpath)

        if i.endswith(".jar"): #salvo il percorso dei file jar che trovo in una lista, i primi due (dovrebbero sempre essere solo due) li passo come parametro per il confronto delle dipendenze
            #print("file jar :" , ifullpath)
            percorsifilejar.append(ifullpath)

        #salvo il percorso delle sottodirectory che trovo in una lista. Bisogna non prendere in consierazione la cartella "analisiDip" che viene creata dall'analisi con jdeps quindi con la funzione "ricercaDipendenze"
        if os.path.isdir(os.path.join(itemfullpath, i)) and not i.endswith("analisiDip"):
            #print("cartella")
            percorsidirectory.append(ifullpath)

    #controllo se gli elementi sono presenti nella cartella o altrimenti l'analisi non e' possibile
    if len(percorsifilejar) >= 2 and len(percorsidirectory) >= 2 and not ComunicazioneDB.check(item):
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print 'prime due cartelle ottenute:'
        print percorsidirectory[0]
        print percorsidirectory[1]
        print
	print st
	print
        # esegue le operazioni sul manifest e stampa la differenza di permessi e activity
        coppiaManifest = parserManifest.coppiaManifest(os.path.join(percorsidirectory[0], "AndroidManifest.xml"),
                                                       os.path.join(percorsidirectory[1], "AndroidManifest.xml"))
        #print 'differenza permessi:'
        differenzaPermessi = coppiaManifest.differenzaPermessi()
        #print differenzaPermessi
        #print
        #print "differenza activity:"
        differenzaActivity = coppiaManifest.differenzaActivity()
        #print differenzaActivity
        #print
        #print "permessi duplicati:"
        permessiDuplicati = coppiaManifest.duplicatiPermessi()
        #print permessiDuplicati
        #print

        # operazioni sui file
        #print "differenza tra i file:"
        res1 = os.path.join(percorsidirectory[0], 'res')  # unisco il path del percorso a "res"
        res2 = os.path.join(percorsidirectory[1], 'res')
        differenzaFile = contaFiles.differenzaRisorse(res1, res2)
        #print differenzaFile
        #print

        # esegue la ricerca delle dipendenze e le stampa
        jdeps = ricercaNew.ricercaDipendenze(percorsifilejar[0], percorsifilejar[1])
	#jdeps=["prova"]
        #  print len(jdeps)
        # for a in jdeps:      print(a)
        #print

        # esegue e stampa il caricamento dinamico
        vcd = VerificaCaricamentoDinamico.CaricamentoDinamico(percorsidirectory[0], percorsidirectory[1])
        # print 'risultato VerificaCaricamentoDinamico:'
        # for a in vcd:
        #   print(a)
        #print
        #print
        #print
        ComunicazioneDB.insert(item,differenzaPermessi,permessiDuplicati,differenzaFile,differenzaActivity,vcd,jdeps)

    else:
        print ("elementi necessari per l'analisi non trovati")
        print

    

