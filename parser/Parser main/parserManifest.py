# -*- coding: utf-8 -*-
#serie di funzioni che permettono di fare il parser di un file manifest


import xml.etree.cElementTree as ET


#classe in cui ci sarà il nome dell'elemento (che sia un'aacitivy, una service o un receiver)
# e tre array che conterranno tutte le ACTION,CATEGORY,DATA del nodo intentFilter
class ElementoManifest:

    def __init__(self): # se le dichiarazioni non vengono messe qua, phyton le considera come attributi di classi comuni a tutte le variabili di quella classe
        self.name = ""
        self.action = []
        self.category = []
        self.data = []

    def printElemento(self):
        print(self.name)
        print(self.action)
        print(self.category)
        print()

#funzione che dato un file xml restituisce il root
#il percorso va scritto  con una r prima (esempio r"c:\utenti") or con due backslash (""c:\\utenti") or con uno slash("c:/utenti")
def getRoot(percorso):
    tree = ET.parse(percorso)
    root = tree.getroot()
    return root;


#dato un root restituisce un array con tutti i permessi trovati
def getPermessi(root):
    permessi = [] #la lista con i permessi che verrà poi restituita
    # https://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
    # con elementtree si ha un problema col namespace, xmlns:android e va messo per esteso
    for member in root.findall('uses-permission'):
        attribute = member.attrib
        permessi.append(attribute["{http://schemas.android.com/apk/res/android}name"])
    return permessi

#dato un root restituisce una lista dei nomi delle activity ...... il che rende la funzione quasi uguale a "getPermessi" per ora
def getNomiActivity(root):
    activity = [] #la lista con gli activity che verrà poi restituita
    # https://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
    # con elementtree si ha un problema col namespace, xmlns:android e va messo per esteso

    applicatazione = root.find("application") # ottengo il figlio application dal manifest, dovrebbe essere solo uno, quindi non serve un for
    for member in applicatazione.findall("activity"): #dal figlio application prendo il figlio activity
        attribute = member.attrib
        activity.append(attribute["{http://schemas.android.com/apk/res/android}name"])
    return activity


#funzione che restituisce una lista di ElementoManifest contenente tutte le activity con i corrispettivi intent
def getActivity(root):
    elementi = [] # la lista di ElementoManifest che verrà restituita
    for applicazione in root.findall("application"): # le activity sono sotto la voce application; dovrebbe essercene solo una, ma nel dubbio metto un find all
        for member in applicazione.findall("activity"):
            em = ElementoManifest()
            attribute = member.attrib
            em.name = attribute["{http://schemas.android.com/apk/res/android}name"] #salvo il nome dell'activity
            for intent in member.findall("intent-filter"): #cerco se l'activity ha un figlio "intent", non sempre lo ha
                for action in intent.findall("action"): # cerco tutte le azioni dell'intent
                    em.action.append(action.attrib["{http://schemas.android.com/apk/res/android}name"])
                for category in intent.findall("category"): # cerco tutte le category dell'intent in modo da inserirle
                    em.category.append(category.attrib["{http://schemas.android.com/apk/res/android}name"])
            #print (em.name)
            elementi.append(em) #aggiungo il nuovo elemento creato alla lista
    return elementi


# restituisce il complemento dell'intersezione tra due liste (controllare complessità del codice)
def diffList(li1, li2):
    l = list(set(li1) - set(li2))
    l = l + list(set(li2) - set(li1))
    return (l)

#restituisce tutti i duplicati in una lista
def cercaDuplicati(lista):
    elementi = []
    duplicati = []
    for x in lista:
        if x not in elementi:
            elementi.append(x)
        else:
            duplicati.append(x)
    return(duplicati)


#dato un percorso e un nome file scrive la lista passata su quel file (in modalità w)
def scriviListaSuFile(file, lista):
    file = open(file, "w")
    for item in lista:
        file.write("%s\n" % item)
    file.close()



#classe che contiene due file xml ed esegue su richiesta le operazioni di cui si ha bisogno
class coppiaManifest():
    #nell'inizializzazione vanno passati due percorsi, che sarebbero i due file xml
    def __init__(self, percorso1, percorso2):
        self.root1 = getRoot(percorso1)
        self.root2 = getRoot(percorso2)

    #restituisce i permessi non in comune tra i due file xml
    def differenzaPermessi(self):
        permessi1 = getPermessi(self.root1)
        permessi2 = getPermessi(self.root2)
        return diffList(permessi1, permessi2)

    #restituisce le activity non in comute tra i due file xml
    def differenzaActivity(self):
        activity1 = getNomiActivity(self.root1)
        activity2 = getNomiActivity(self.root2)
        return diffList(activity1,activity2)
