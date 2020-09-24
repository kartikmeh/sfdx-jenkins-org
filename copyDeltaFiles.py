file=open("list.txt", "r")
list = file.readlines()
listUpdated=[]
listMkdir=[]
for row in list:
	row = row.replace("/", "\\")
	listUpdated.append(str(row))
	try:
		index=row.rindex("\\")
		row=row[0:index]
		listMkdir.append(row)
	except:
		print("substring not found")
print(listUpdated)
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
for row in listMkdir:
	if("force-app" in row):
		os.system("mkdir delta\\"+row)
for row in listUpdated:
	row=row.rstrip()
	if("force-app" in row):
		command="echo y | copy "+dir_path+"\\"+row +" "+ dir_path+"\\delta\\"+row
		os.system(command)