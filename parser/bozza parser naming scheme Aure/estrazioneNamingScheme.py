#import per visitare le sotto directory
import os
#import per leggere i valori da riga di comando
import sys
#modifica del path per windows
path = sys.argv[1].replace("\\","/")
#nome dell'apk analizzato per usarlo come nome del file di output
nome_apk = sys.argv[1].replace("\\","_")
#apertura file su cui scrivere i risultati
out_file = open(nome_apk+".txt","w+")
#Il metodo walk () genera i nomi dei file in un
#albero delle directory navigando l'albero dal basso verso 
#l'alto. L'indice serve solo a contare il numero delle classi .java presenti nella directory
index=0
for root, dirs, files in os.walk(path):
	#nel primo ciclo andiamo a cercare in tutti i file contenuti nella directory
	for file in files:
		#prendiamo tutti i file che terminano con .java
		if file.endswith(".java"):
			#ci prendiamo il percorso di tutti i file che terminano con .java
			fi=os.path.join(root, file)
			#aggiustiamo il path per windows
			fis = fi.replace("/","\\")
			#apriamo i vari file per cercare il naming scheme
			in_file = open(fis,"r")
			#leggiamo riga per riga
			for line in in_file:
				#se la linea inizia per package stampiamo il contenuto della linea
				if line.startswith("package"):
					#con line[8:] stampiamo i caratteri a partire dalla posizione 8 fino alla fine
					#la posizione parte da zero.
					#convertiamo index in stringa perché write vuole solo stringhe (SE POSSIBILE MIGLIORARE QUESTA COSA)
					out_file.write(str(index)+"."+fis+";"+line[8:])
					#riconvertiamo in intero per incrementare il valore (SE POSSIBILE MIGLIORARE QUESTA COSA)
					int(index)
				#le linee che non iniziano con package vengono skippate
					index=index+1
				else:
					pass
		#i file che non terminano con .java vengono skippati
		else:
			pass
out_file.close()