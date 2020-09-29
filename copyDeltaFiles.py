import io
file=io.open("list.txt", "r", encoding = "utf-16")
list = file.readlines()
print(list)
listUpdated=[]
for row in list:
	row = row.replace("/", "\\")
	listUpdated.append(str(row))
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
for row in listUpdated:
	row=row.rstrip()
	if("force-app" in row):
		index=row.rindex("\\")
		path=row[0:index]
		if os.path.isfile(row):
			os.system("mkdir "+ dir_path+"\\delta\\"+path)
		command="echo y | copy \""+dir_path+"\\"+row +"\" \""+ dir_path+"\\delta\\"+row+"\""
		os.system("echo y | copy \""+dir_path+"\\"+row +"-meta.xml\" \""+ dir_path+"\\delta\\"+row+"-meta.xml\"")
		print(command)
		result=os.popen(command).read()
		if("The system cannot find the file specified" in result):
			os.system("mkdir "+ dir_path+"\\deltaDestruction\\force-app\\main\\default\\manifest\\")
			os.system("copy "+dir_path+"\\package.xml "+ dir_path+"\\deltaDestruction\\force-app\\main\\default\\manifest\\")
			fileName=row[index+1:]
			if("meta.xml" not in fileName):
				os.system("mkdir "+ dir_path+"\\deltaDestruction\\"+path)
				os.system("echo file > " +dir_path+"\\deltaDestruction\\"+row)
			
