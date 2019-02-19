import os
import sys
import subprocess

#ORA RICERCA DIPENDENZE RICEVE COME PARAMETRO IL PATH
			
def ricercaDipendenze(path1 , path2):
	array_diff=[]
	directory=os.path.dirname(path1)
	directory2=os.path.join(directory, "analisiDip")
	directory = directory.replace(' ','\ ')
	basename=os.path.basename(path1)
	basename2=os.path.basename(path2)
	#print basename
	#print basename2
	comando1= "jdeps -verbose:class -dotoutput " + directory + "/analisiDip " + path1.replace(' ','\ ')
	comando2= "jdeps -verbose:class -dotoutput " + directory + "/analisiDip " + path2.replace(' ','\ ')
	os.system(comando1)
	os.system(comando2)
	#directory per analisi dip
	dotFile1=directory2 + "/" + basename + ".dot"
	dotFile2=directory2 + "/"+ basename2 + ".dot"
	#print dotFile1	
	nodesFile1=dotFile1 + ".nodes"
	nodesFile2=dotFile2 + ".nodes"	
	#print dotFile1
	#print nodesFile1
	comandoN1= "dot -Tplain " + dotFile1.replace(' ','\ ') + " | sed -ne 's/^node \([^ ]\+\).*$/\\1/p' | sort > " + nodesFile1.replace(' ','\ ')
	comandoN2="dot -Tplain " + dotFile2.replace(' ','\ ') + " | sed -ne 's/^node \([^ ]\+\).*$/\\1/p' | sort > " + nodesFile2.replace(' ','\ ')
	os.system(comandoN1)
	os.system(comandoN2)
	#comando per la diff
	comandoDiff= "diff " + nodesFile1.replace(' ','\ ') + " " + nodesFile2.replace(' ','\ ')
	#print comandoDiff
	#questa parte serve per inserire il risultato nel comando nell array che poi viene ritornato
	'''
	handle = os.popen(comandoDiff)
   	line = " "
   	while line:
        	line = handle.read()
		#print line
		array_diff.append(line)
    	handle.close()
	'''
	proc = subprocess.Popen([comandoDiff],shell=True,stdout=subprocess.PIPE,)
	stdout_value=proc.communicate()[0]
	if stdout_value:
		array_diff.append(stdout_value)
		array_diff=array_diff[0].splitlines()
	return array_diff




# ESEMPIO PER VEDERE SE FUNZIONA. LA DIRECTORY CORRENTE E PROVA, OSSIA QUELLA CONTENENTE AD ESEMPIO 173,174,175 E 176. 
'''
dir="prova"
for item in os.listdir(dir):
   if not item.endswith(".py"):
	#print os.listdir(dir)
	itemfullpath=os.path.join(dir,item)
	#print(itemfullpath)
	array_jar=[]

	for i in os.listdir(itemfullpath):
		#print(os.path.join(itemfullpath,i))
		
		if os.path.isfile(os.path.join(itemfullpath,i)):
			
			path=os.path.join(itemfullpath,i)
			
		
			
			if path.endswith(".jar"):
				array_jar.append(path)
				#ricercaDipendenze()
				#print path
	#for name in array_jar:
	#	print name
	#	print len(array_jar)
	print array_jar[0]
	print array_jar[1]

	for name in ricercaDipendenze(array_jar[0] , array_jar[1]):
		print name
'''
			

