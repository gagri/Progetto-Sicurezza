# -*- coding: utf-8 -*-
import csv
import sys
import os
import os.path
import subprocess

##Comando per fare il grep nei file java:
##  find -name '*.java' -exec grep --color=always -in "ClassLoader" {} 2>/dev/null +


#definisco un oggetto che mi rappresenta la data applicazione
class applicazione:
	#definisco le variabili che mi interessano
	identificativo=""
	caricamentoDinamico1=0
	caricamentoDinamico2=0
	
	#definisco un metodo che mi costruisce una stringa pronta per essere stampata su un csv
	def csvPrint(self):
        	string=[]
		string.append(self.identificativo)
		string.append(self.caricamentoDinamico1)
		string.append(self.caricamentoDinamico2)
		return string

#variabili di supporto
Caricamento1 = False
Caricamento2 = False

#definizione delle varie parti della stringa del comando
parteIniziale='find -name "*.java" -exec grep -in '
parteFinale=' {} 2>/dev/null +'
stringhe=[]
stringhe.append('"dalvik.system.DexClassLoader"')
stringhe.append('"dalvik.system.PathClassLoader"')
stringhe.append('"dalvik.system.InMemoryDexClassLoader"')
stringhe.append('"dalvik.system.BaseDexClassLoader"')
stringhe.append('"dalvik.system.DelegateLastClassLoader"')
stringhe.append('"java.net.URLClassLoader"')
stringhe.append('"java.lang.reflect"')

#definizione del metodo di verifica sulla singola applicazione
def verificaIndicatori():
	CaricamentoDinamico = False
	for i in stringhe:
		comando = parteIniziale+i+parteFinale
		proc = subprocess.Popen([comando],shell=True, stdout=subprocess.PIPE,)
		stdout_value=proc.communicate()[0]
		if stdout_value:
			CaricamentoDinamico= True
	return CaricamentoDinamico

#creo un nuovo oggetto che mi rappresentera' la singola applicazione
app=applicazione()

#serve un modo per recuperare un identificativo dell'applicazione
#app.identificativo=""


#mi sposto nella cartella contenente la prima applicazione 

#verifico la presenza del caricamento dinamico nella prima app
app.CaricamentoDinamico1 = verificaIndicatori()


#mi sposto nella cartella contenente la prima applicazione 

#verifico la presenza del caricamento dimanico nella seconda app
app.CaricamentoDinamico2 = verificaIndicatori()


##stampa del cvs

#cerco di creare un file csv da aprire piu' volte e su cui effettuare piu' stampe

writepath = './data.csv'

#verifico l'esistenza del file
if(os.path.exists(writepath)):
	#se esiste lo apro in modalita' append e aggiungo i dati nuovi
	Resident_data = open(writepath,'a')
	csvwriter = csv.writer(Resident_data)
else:
	# altrimenti lo creo 
	Resident_data = open(writepath, 'w+')
	csvwriter = csv.writer(Resident_data)
	#creo la testa del file e la aggiungo
	file_head=[]	
	file_head.append("Applicazione")
	file_head.append("CaricamentoDinamico")
	csvwriter.writerow(file_head)

#aggiungo il valore appena ottenuto al file
csvwriter.writerow(app.csvPrint())

#chiudo i file utilizzati
Resident_data.close()

