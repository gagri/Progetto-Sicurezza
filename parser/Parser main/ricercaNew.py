import os
import sys
import subprocess
import time
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

	#start_time = time.time()
	#print "prima di comando jdeps"



	comando1= "jdeps -verbose:class -dotoutput " + directory + "/analisiDip " + path1.replace(' ','\ ')
	comando2= "jdeps -verbose:class -dotoutput " + directory + "/analisiDip " + path2.replace(' ','\ ')
	os.system(comando1)
	os.system(comando2)
	#directory per analisi dip

	#print "dopo comando jdeps", " tempo: ", time.time() - start_time, " secondi"


	dotFile1=directory2 + "/" + basename + ".dot"
	dotFile2=directory2 + "/"+ basename2 + ".dot"
	#print dotFile1	
	nodesFile1=dotFile1 + ".nodes"
	nodesFile2=dotFile2 + ".nodes"	
	#print dotFile1
	#print nodesFile1

	#start_time = time.time()
	#print "prima comando dot"


	#print dotFile1
	#print nodesFile1
	surrogaDot(dotFile1, nodesFile1)
	surrogaDot(dotFile2, nodesFile2)

	#comandoN1= "dot -Tplain " + dotFile1.replace(' ','\ ') + " | sed -ne 's/^node \([^ ]\+\).*$/\\1/p' | sort > " + nodesFile1.replace(' ','\ ')
	#comandoN2="dot -Tplain " + dotFile2.replace(' ','\ ') + " | sed -ne 's/^node \([^ ]\+\).*$/\\1/p' | sort > " + nodesFile2.replace(' ','\ ')
	#os.system(comandoN1)
	#os.system(comandoN2)

	#print "dopo comando dot", " tempo: ", time.time() - start_time, " secondi"
	#start_time = time.time()

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

	#print "fine programma", " tempo: ", time.time() - start_time, " secondi"




	#restituisce quello il file .dot.nodes ma senza fare dot
def surrogaDot(fileInput, fileOutput):
	#print 'start'
	comando = "grep -F '>' "+fileInput.replace(' ','\ ')+" | sed 's/->/\\n/g' | sed 's/ //g' | sed 's/[(][^)]*[)]/()/g' | sed 's/()\";//' | sed 's/;//' | sort | uniq > "+fileOutput.replace(' ','\ ')
	#print comando
	os.system(comando)
