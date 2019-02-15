from pymongo import MongoClient

#farlo a funzione che accetta i vari parametri in ingresso da salvare su mongo. Fare altre due insert di prova che stampa a video e uno reale che salva sul db.
#aggiungere una funzione per effettuare la connessione.

# creating connectioons for communicating with Mongo DB per ora previsto il db in locale
client = MongoClient('localhost:27017')
db = client.App

def main():

    while(1):
	# chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 3 to read, 4 to delete\n')
    
        if selection == '1':
	    insert()
    	#elif selection == '2':
	#   update()
    	elif selection == '3':
	    read()
    	elif selection == '4':
	    print 'delete'
	    delete()
    	else:
	    print '\n INVALID SELECTION \n'


# Function to insert data into mongo db
def insert():
    try:
	appId = int(input('Inserire l app id :'))
	appName = raw_input('Inserire il nome dell app :')
	numeroPermessi = int(input('Inserire il numero di permessi :'))
	listaPermessi=[]
	for i in range(0,numeroPermessi):
		temp=raw_input('Aggingere il permesso:')
		listaPermessi.append(temp)
	numeroFile = int(input('Inserire il numero di file :'))
	listaFile=[]
	for i in range(0,numeroFile):
		temp=raw_input('Aggingere il file:')
		listaFile.append(temp)
	numeroActivity =int(input('Inserire il numero di activity :'))
	listaActivity=[]
	for i in range(0,numeroActivity):
		temp=raw_input('Aggingere l activity:')
		listaActivity.append(temp)
	numeroRecord = int(input('Inserire il numero di record :'))
	listaRecord=[]
	for i in range(0,numeroRecord):
		temp=raw_input('Aggingere il record:')
		listaRecord.append(temp)

	db.App.insert_one(
	    {
		"id": appId,
	        "nome":appName,
		"#Permessi":numeroPermessi,
		"Lista permessi": listaPermessi,
		"#File":numeroFile,
		"Lista file": listaFile,
		"#Activity":numeroActivity,
		"Lista Activity": listaActivity,
		"#Record Caricamento dinamico":numeroRecord,
		"Lista Record Caricamento dinamico": listaRecord
	    })
        print '\nInserted data successfully\n'
	
    except Exception, e:
        print str(e)

'''	
# Function to update record to mongo db
def update():
    try:
	criteria = raw_input('\nEnter id to update\n')
	name = raw_input('\nEnter name to update\n')
	age = raw_input('\nEnter age to update\n')
	country = raw_input('\nEnter country to update\n')

	db.Employees.update_one(
	    {"id": criteria},
	    {
		"$set": {
		    "name":name,
		    "age":age,
		    "country":country
		}
	    }
	)
	print "\nRecords updated successfully\n"	
	
    except Exception, e:
	print str(e)
'''

# function to read records from mongo db
def read():
    try:
	empCol = db.App.find()
	print '\n All data from App Database \n'
	for emp in empCol:
	    print emp

    except Exception, e:
	print str(e)

# Function to delete record from mongo db
def delete():
    try:
	criteria = int(input('\nInserire l id dell app da eliminare\n'))
        db.App.delete_many({"id":criteria})
	print '\nDeletion successful\n'	
    except Exception, e:
	print str(e)

main()
