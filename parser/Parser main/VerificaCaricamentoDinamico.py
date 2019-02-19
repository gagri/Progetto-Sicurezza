# -*- coding: utf-8 -*-
import sys
import os
import os.path
import subprocess

##Comando per fare il grep nei file java:
##  find -name '*.java' -exec grep --color=always -in "ClassLoader" {} 2>/dev/null +

#definizione delle varie parti della stringa del comando
parteIniziale='find -name "*.java" -exec grep -in '
parteFinale=' {} 2>/dev/null +'
stringhe=[]
#definizione degli indicatori di caricamento dinamico
stringhe.append('"dalvik.system.DexClassLoader"')
stringhe.append('"dalvik.system.PathClassLoader"')
stringhe.append('"dalvik.system.InMemoryDexClassLoader"')
stringhe.append('"dalvik.system.BaseDexClassLoader"')
stringhe.append('"dalvik.system.DelegateLastClassLoader"')
stringhe.append('"java.net.URLClassLoader"')
stringhe.append('"java.lang.reflect"')

#definizione del metodo di verifica sulla singola applicazione
def verificaIndicatori(listaIndicatori):
	CaricamentoDinamico = False
	for i in stringhe:
		comando = parteIniziale+i+parteFinale
		proc = subprocess.Popen([comando],shell=True, stdout=subprocess.PIPE,)
		stdout_value=proc.communicate()[0]
		if stdout_value:
			CaricamentoDinamico= True
			listaIndicatori.append(stdout_value)
	if CaricamentoDinamico:
		listaIndicatori=listaIndicatori[0].splitlines()
	return CaricamentoDinamico


#la funzione prevede i due percorsi contenenti le due versioni delle app come input.
#la funzione restituisce la lista delle differenze tra i due caricamenti dinamici se ci sono. Altrimenti restituisce una lista vuota se entrambe le app presentano gli stessi identici indicatori di caricamento dinamico. Restituisce infine un oggetto None se non ci sono indicatori di caricamento dinamico in nessuna delle due app
def CaricamentoDinamico(percorso1,percorso2):
	#variabili di supporto
	#variabili che mi rappresentano gli indicatori di caricamento dinamico nelle due app
	Caricamento1 = False
	Caricamento2 = False
	#lista degli indicatori di caricamento dinamico delle due app
	listaIndicatori1=[]
	listaIndicatori2=[]
	#mi sposto nella cartella contenente la prima applicazione 
	os.chdir(percorso1)
	#verifico la presenza del caricamento dinamico nella prima app
	CaricamentoDinamico1 = verificaIndicatori(listaIndicatori1)
	#mi sposto nella cartella contenente la seconda applicazione 
	os.chdir(percorso2)
	#verifico la presenza del caricamento dimanico nella seconda app
	CaricamentoDinamico2 = verificaIndicatori(listaIndicatori2)
	#faccio la differenza tra i due set
	if(CaricamentoDinamico1 or CaricamentoDinamico2):
		#print("indicatori prima app:\n")		
		#print(listaIndicatori1)
		#print("indicatori seconda app:\n")		
		#print(listaIndicatori2)
		lista=list(set(listaIndicatori1) - set(listaIndicatori2))
		#lista=lista+list(set(listaIndicatori2) - set(listaIndicatori1))
		return lista
	else:
		return None

#linea utilizzata per verificare che il programma funzioni
#print(CaricamentoDinamico("/home/lucio/Scrivania/Progetto-Sicurezza/ApkProva/ApkProva/3/0046c61ae2","/home/lucio/Scrivania/Progetto-Sicurezza/ApkProva/ApkProva/3/b333c3b395"))
