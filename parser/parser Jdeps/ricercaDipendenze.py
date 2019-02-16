import os
import sys
import subprocess

#ricerca le dipendenze e ritorna un array di stringhe con i risultati. I file creati durante il processo di analisi vengono salvati nella directory "analisiDip"

def ricercaDipendenze(jar1 , jar2):
	#array finale contenente i risultati della diff
	array_diff=[]
	#comandi per jdesp. Creano due file dot e li inserisco nella nuova cartella "analisiDip"
	comando1= "jdeps -verbose:class -dotoutput analisiDip " + jar1
	comando2= "jdeps -verbose:class -dotoutput analisiDip " + jar2
	os.system(comando1)
	os.system(comando2)
	#mi sposto nella directory "analisiDip"
	os.chdir(os.path.join(os.path.abspath(os.path.curdir),u'analisiDip'))
	#queste 4 stringhe servono per lanciare i comandi che ordinano i nodi (creando appositi file con est. .nodes) e fanno la diff 
	dotFile1=jar1 + ".dot"
	dotFile2=jar2 + ".dot"
	nodesFile1=dotFile1 + ".nodes"
	nodesFile2=dotFile2 + ".nodes"
	#costruisco i comandi
	comandoN1= "dot -Tplain " + dotFile1 + " | sed -ne 's/^node \([^ ]\+\).*$/\\1/p' | sort > " + nodesFile1
	comandoN2="dot -Tplain " + dotFile2 + " | sed -ne 's/^node \([^ ]\+\).*$/\\1/p' | sort > " + nodesFile2
	#lancio i comandi
	os.system(comandoN1)
	os.system(comandoN2)
	#comando per la diff
	comandoDiff= "diff " + nodesFile1 + " " + nodesFile2
	#questa parte serve per inserire il risultato nel comando nell array che poi viene ritornato
	handle = os.popen(comandoDiff)
   	line = " "
   	while line:
        	line = handle.read()
		array_diff.append(line)
    	handle.close()
	return array_diff


#PARTE DI TEST DELLA FUNZIONE

#Si considera la directory corrente.Va modificato in modo tale da scorrere tutte le cartelle del dataset
dir="."

#jdeps funziona sui jar o sulle directory. In questa lista memorizzo i jar contenuti nella directory
array_jar=[]
#array per i file ottenuti
i=0;
for root,dirs, files in os.walk(dir,topdown=False):
	for name in files:
		#per tutti i jar devo lanciare il comando jdeps
		if name.endswith("jar"):
			array_jar.append(name)
#dovrebbero essercene solo due in questo livello che sono quelli che interessano
app1=array_jar[0]
app2=array_jar[1]

for name in ricercaDipendenze(app1,app2):
	print name




