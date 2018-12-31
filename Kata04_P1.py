#read data from file
def readFileLines(datafile):
	#open file for reading
	with open(datafile,'r') as rf:
		#read each row as a line from text file
		rows=rf.readlines()
	print "\nrows in readFile",rows
	return rows

def extractTable(rowsList):
	Table=[]
	#split the content of line based on space
	for row in rowsList:
		rowncol=row.strip().replace('    ',' ').replace('   ',' ').replace('  ',' ').split(' ')
	#append each rowncol to Table to get table with rows and columns
		Table.append(rowncol)
	print "\nTable:: \n",Table
	return Table

def removestar(val):
	val=val.replace('*','')
	return val

#The funtion to validate each row and refine the values in each column
def validate(row):
	ncol=[]
	ncount=len(row)
	for i,col in enumerate(row):
		#if the row starting with numeric element then add them to table else leave them out
		print col
		if len(col)>0:
			if i == 0:
				if(col.isdigit()== False):
					print "col.isdigit"
					return [0,row]
				else:
					if '*' in col:
						col=removestar(col)
					#else:
					try:
						ncol.append(int(col))
					except:
						ncol.append(float(col))
			else:
				if '*' in col:
					col=removestar(col)
				#else:
				try:
					ncol.append(int(col))
				except:
					try:
						ncol.append(float(col))
					except:
						ncol.append(col)
		else:
			ncol.append(col)
	print ("\n ncol",ncol)
	if len(ncol)==ncount:
		return [1,ncol]


#Remove unnecessary rows and symbols that shouldn't be in table
def RefineTable(Table):
	RTable=[]
	validateval=None
	for row in Table:
		print("row",row)
		print "\n"
		if len(row)>1:
			validateval=validate(row)
			print ("validateval",validateval)
			if validateval[0] == 1:
				RTable.append(validateval[1])
	return RTable

def TempTable(Rtable):
	TableTemp=[]
	for row in Rtable:
		TableTemp.append([row[0],row[1],row[2]])
	print TableTemp
	return TableTemp

def findMinMonth(Table):
	minmonth=9999
	minmonth_idx=0
	for row in Table:
		print row[0],row[1],row[2],row[1]-row[2]
		if(minmonth > (row[1]-row[2])):
			minmonth_idx=row[0]
			minmonth=row[1]-row[2]
	return [Table[minmonth_idx][0],Table[minmonth_idx][1],Table[minmonth_idx][2]]

file="weather.dat"
rowline=readFileLines(file)
Table=extractTable(rowline)
Rtable=RefineTable(Table)
print Rtable					
TTable=TempTable(Rtable)
MinMonth=findMinMonth(TTable)
print "\n Month minimum spread:"+str(MinMonth[0])+" with spread "+str(MinMonth[1]-MinMonth[2])
