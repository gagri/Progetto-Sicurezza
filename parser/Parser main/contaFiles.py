import os
import sys

#dir= "/Users/grima/Desktop/Materiale2"


def cercaRisorse(percorso_res):		
	dir=percorso_res
	c=[]
	
	for root, dirs,files in os.walk(dir, topdown=False):
		n=os.path.basename(root)
		for name in files:
			c.append(os.path.join(n,name))
	return c


def differenzaRisorse(percorso_res1 , percorso_res2):
	res1=cercaRisorse(percorso_res1)
	res2=cercaRisorse(percorso_res2)
	lista=list(set(res1)-set(res2))
	return lista
