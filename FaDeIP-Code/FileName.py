import os
import ScrollText
import glob
def getNewFileName(folderName, prefix, extention):
	path = os.getcwd()
	if(folderName == ""):
		newPath = path
	else:
		newPath = path + "\\" + folderName
	if not os.path.isdir(newPath):
		ScrollText.sc.appendStatusText("Creating Folder %s"%newPath)
                os.mkdir(newPath)
	
	os.chdir(newPath)
	try:
		newest = max(glob.iglob(prefix + '*' + extention), key=os.path.getctime)
		newest = newest.strip(prefix)
		newest = newest.strip(extention)
	except:
		newest = "0"
	fileName =  newPath + "\\" + prefix + str(int(newest) + 1) + extention
	os.chdir("..")
	return fileName
	