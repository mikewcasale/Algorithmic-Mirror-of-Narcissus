import os
import pandas as pd
import xlrd

def createDirs():
	# Directory 
	directories = ["./codedata","./codedata/StudyTitle","./codedata/PressReleaseTitle"]
	for directory in directories:
		try:
			# Create the directory 
			# 'codedata' in 
			# '/home / User / Documents' 
			os.mkdir(directory) 
		except: pass
		
createDirs()

#dictionary to store xls dataframe
dic = {
	'GroundTruth':[],
	'Assertion':[],
	'LieCategory':[]
}
filect=0
directories = ['./data/JournalPROpenData-master/excelfiles']
for directory in directories:
	for filename in os.listdir(directory):
		filect+=1
		fname='assertion_'+str(filect)+'.txt'
		workbook = xlrd.open_workbook(directory+'/'+filename)
		worksheet = workbook.sheet_by_name('Sheet1')
		PressReleaseTitle = worksheet.cell(0, 1).value
		StudyTitle = worksheet.cell(1, 1).value
		LieCategory = 'Exaggeration'
		file = open("./codedata/StudyTitle/"+fname, "w") 
		file.write(StudyTitle) 
		file.close() 
		file = open("./codedata/PressReleaseTitle/"+fname, "w") 
		file.write(PressReleaseTitle) 
		file.close() 
		dic['GroundTruth'].append(StudyTitle)
		dic['Assertion'].append(PressReleaseTitle)
		dic['LieCategory'].append('Exaggeration')
		print('PressReleaseTitle',PressReleaseTitle)
		print('StudyTitle',StudyTitle)
df = pd.DataFrame(dic,columns=['GroundTruth','Assertion','LieCategory'])
df.to_csv('train_exaggeration.csv',index=False)








