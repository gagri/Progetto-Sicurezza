import os
import sys

#dir= "/Users/grima/Desktop/Materiale2"
dir=sys.argv[1]


def cercaRisorse(percorso_res):		
	dir=percorso_res
	c=[]
	
	for root, dirs,files in os.walk(dir, topdown=False):
		n=os.path.basename(root)
		for name in files:
			c.append(os.path.join(n,name))
	#print c			 
	return c


def differenzaRisorse(percorso_res1 , percorso_res2):
	res1=cercaRisorse(percorso_res1)
	res2=cercaRisorse(percorso_res2)
	lista=list(set(res1)-set(res2))
	print len(set(res2))
	return lista
	

#Esplora tutte le directory a partire dal path specificato (walk)
'''
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
'''
d=differenzaRisorse("/home/gaia/Scaricati/ApkProva/1/000d753e7c/res" , "/home/gaia/Scaricati/ApkProva/1/fd537396e9/res")


print d
print len(d)



				

   

