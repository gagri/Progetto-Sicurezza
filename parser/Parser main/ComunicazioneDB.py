# -*- coding: utf-8 -*-
from pymongo import MongoClient

#non e' possibile includere la parte di connessione in una funzione perche' le variabili client e db devono essere globali ma la funzione insertStampa che non fa accessi al db funziona in ogni caso
client = MongoClient('localhost:27017')
db = client.App
cl = db.app

# Funzione che serve a verificare l'effettivo collegamento con il db e che consente l'inserimento dei dati da stdinput
# non sono previsti parametri in ingressi questi vengono inseriti tramite stdinput
def insertProva():
    try:
	appId = int(input('Inserire l app id :'))
	numeroPermessi = int(input('Inserire il numero di permessi :'))
	listaPermessi=[]
	for i in range(0,numeroPermessi):
		temp=raw_input('Aggingere un permesso:')
		listaPermessi.append(temp)
	numeroFile = int(input('Inserire il numero di file :'))
	listaFile=[]
	for i in range(0,numeroFile):
		temp=raw_input('Aggingere un file:')
		listaFile.append(temp)
	numeroActivity =int(input('Inserire il numero di activity :'))
	listaActivity=[]
	for i in range(0,numeroActivity):
		temp=raw_input('Aggingere una activity:')
		listaActivity.append(temp)
	numeroIndicatori = int(input('Inserire il numero di indicatori di caricamento dinamico :'))
	listaIndicatori=[]
	for i in range(0,numeroIndicatori):
		temp=raw_input('Aggingere un indicatore:')
		listaIndicatori.append(temp)
	numeroDipendenze = int(input('Inserire il numero di dipendenze aggiunte:'))
	listaDipendenze=[]
	for i in range(0,numeroDipendenze):
		temp=raw_input('Aggingere una dipendenza:')
		listaDipendenze.append(temp)

	cl.insert_one(
	    {
		"id": appId,
		"#Permessi":numeroPermessi,
		"Lista permessi": listaPermessi,
		"#File":numeroFile,
		"Lista file": listaFile,
		"#Activity":numeroActivity,
		"Lista Activity": listaActivity,
		"#Indicatori Caricamento dinamico":numeroIndicatori,
		"Lista Indicatori Caricamento dinamico": listaIndicatori,
		"#Dipendenze Aggiunte":numeroDipendenze,
		"Lista Dipendenze Aggiunte": listaDipendenze
	    })
        print '\nInserted data successfully\n'
	
    except Exception, e:
        print str(e)

# Funzione che serve a verificare che i dati vengano recuperati e stampati in maniera corretta sul db
# In input sono previsti: l'identificativo dell'applicazione, la lista dei permessi, la lista dei file, la lista delle activity, la lista degli indicatori di caricamento dinamico, la lista delle dipendenze
def insertStampa(appId,listaPermessi,listaFile,listaActivity,listaIndicatoriCaricamentoDinamico, listaDipendenze):
	string=[]
	string.append('"id":')
	string.append(appId)
	string.append('"#Permessi":')
	string.append(len(listaPermessi))
	string.append('"Lista permessi":')
	string.append(listaPermessi)
	string.append('"#File":')
	string.append(len(listaFile))
	string.append('"Lista file":')
	string.append(listaFile)
	string.append('"#Activity":')
	string.append(len(listaActivity))
	string.append('"Lista Activity":')
	string.append(listaActivity)
	string.append('"#Indicatori Caricamento dinamico":')
	string.append(len(listaIndicatoriCaricamentoDinamico))
	string.append('"Lista Record Caricamento dinamico":')
	string.append(listaIndicatoriCaricamentoDinamico)
	string.append('"#Dipendenze Aggiunte":')
	string.append(len(listaDipendenze))
	string.append('"Lista Dipendenze Aggiunte":')
	string.append(listaDipendenze)
        print string
	

# Funzione che serve a inserire i dati nel db
# In input sono previsti: l'identificativo dell'applicazione, la lista dei permessi,la lista dei permessi duplicati, la lista dei file, la lista delle activity, la lista degli indicatori di caricamento dinamico, la lista delle dipendenze
def insert(appId,listaPermessi,listaPermessiDuplicati,listaFile,listaActivity,listaIndicatoriCaricamentoDinamico, listaDipendenze):
	numeroClassiDipendenze=len(listaDipendenze)
	for string in listaDipendenze:
		if string.startswith('<') or string.startswith('>'):
			numeroClassiDipendenze=numeroClassiDipendenze-1
	try:
		cl.insert_one(
		    {
			"id": appId,
			"#Permessi":len(listaPermessi),
			"Lista Permessi": listaPermessi,
			"#Permessi Duplicati": len(listaPermessiDuplicati),
			"Lista Permessi Duplicati": listaPermessiDuplicati,
			"#File":len(listaFile),
			"Lista File": listaFile,
			"#Activity": len(listaActivity),
			"Lista Activity": listaActivity,
			"#Indicatori Caricamento dinamico": len(listaIndicatoriCaricamentoDinamico),
			"Lista Indicatori Caricamento dinamico": listaIndicatoriCaricamentoDinamico,
			"#Dipendenze Aggiunte":numeroClassiDipendenze,
			"Lista Dipendenze Aggiunte": listaDipendenze
		    })
	        print '\nInserted data successfully\n'
	except Exception, e:
        	print str(e)	


# funzione per verificare se una app e' gia' stata inserita all'interno del db
def check(Id):
    try:
	empCol = cl.find_one({'id':Id})
	if empCol:
		return True
	else:
		return False

    except Exception, e:
	print str(e)


#comandi utilizzati per testare il programma
#insertProva()
#lista = ['a','b','c']
#insertStampa(1,lista,lista,lista,lista,lista)
#insert(1,lista,lista,lista,lista,lista)
