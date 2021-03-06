import pywikibot, os, time



def WIKBuploadPage(uploadName, uploadFile):
	page = pywikibot.Page(site, uploadName)
	oompFileName = uploadFile
	print "FileName:  " + oompFileName
	print "Uploading To:  " + uploadName
	try:
		oompFile = open(oompFileName)
		oompFileContents = oompFile.read()
		page.text = oompFileContents
		page.save('Updating File - ' + time.strftime("%d/%m/%Y %H:%M:%S"))  # Saves the page
		print "Page Saved."
	except:
		"File Not Found: " + oompFileName

def WIKBuploadAll(baseDirectory, webBase, fileAddition):

	print "Uploading All OOMP Files:"

	for x in os.walk(baseDirectory):
		idString = str(x[0].replace(baseDirectory, ""))
		print "     Uploading ---> " + idString
		if idString <> "" :
			WIKBuploadPage(webBase + idString, baseDirectory + idString + "/" + idString + fileAddition)

def WIKBuploadAllFromFile(baseDirectory, webBase, fileAddition):

	print "Uploading All " + fileAddition + " Files: " + baseDirectory

	for (dirpath, dirnames, filenames) in os.walk(baseDirectory):
		for x in filenames:
			idString = x.replace(fileAddition, "")
			additionTest = x.replace(idString, "")
			print "IDSTRING DEBUG " +  idString + "    " + additionTest + "  " + fileAddition
			print "     Uploading ---> " + idString
			if fileAddition == additionTest:
				WIKBuploadPage(webBase + idString, baseDirectory + "/" + idString + fileAddition)


import argparse

parser = argparse.ArgumentParser(description='OOMLOUT-WIKB -- Bot for uploading WikiPages')
parser.add_argument('-rm','--runMode', help='Sets the runmode for special circumstances (A -- Upload All Directory, B - upload all with same end of file name.)', required=False)
parser.add_argument('-si','--wsite', help='Name of the site you are uploading to', required=True)
parser.add_argument('-ln','--language', help="Language to be uploaing in (default 'en')", required=False)
parser.add_argument('-bd','--baseDirectory', help="Basedirectory to work in", required=False)
parser.add_argument('-wb','--webBase', help="webbase to add the item to (this plus ID)", required=False)
parser.add_argument('-fa','--fileAddition', help="What to add to the id to get the filename", required=False)


args = vars(parser.parse_args())

#loading variables from comman line
runMode = ""
if args['runMode'] <> None:
	runMode = args['runMode']

wsite = ""
if args['wsite'] <> None:
	wsite = args['wsite']

language="en"
if args['language'] <> None:
	language = args['language']

webBase=""
if args['webBase'] <> None:
	webBase = args['webBase']

baseDirectory=""
if args['baseDirectory'] <> None:
	baseDirectory = args['baseDirectory']

fileAddition=""
if args['fileAddition'] <> None:
	fileAddition = args['fileAddition']
	fileAddition = fileAddition.replace("'",'')

site = pywikibot.Site(language, wsite)  # The site we want to run our bot on

print "fileAddition:" + fileAddition

if runMode == "A":
	bds = baseDirectory.split(",")
	for baseDirectory in bds:
		WIKBuploadAll(baseDirectory, webBase, fileAddition)
elif runMode == "B":
	WIKBuploadAllFromFile(baseDirectory, webBase, fileAddition)
else:
	bds = baseDirectory.split(",")
	wbs = webBase.split(",")
	count = 0
	for baseDirectory in bds:
		WIKBuploadPage(wbs[count],baseDirectory)
		count = count + 1