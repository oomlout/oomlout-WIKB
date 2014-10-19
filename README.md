# oomlout-WIKB
A command line python tool used to upload generated files to our wiki

(requires pywikibot)

##  Command Line Parameters

* -rm -- runMode (A,ALL generate all)
* -si -- Name of the website you are uploading to (configured in pywikibot)
* -ln -- Language (default. en)
* -bd -- baseDirectory Directory to use as the base for uploads
* -wb -- webBase Base to be uploaded to
* -fa -- fileAddition Additional ending added to the file (ie. -wiki.html)

##  Usage

### Upload Single File
	
	* -si oomlout (name of profile setup in pywikibot)
	* -bd baseDirectory (name of file to upload)
	* -wb Location to upload to	
		
	python %WIKBdirectory%WIKBmain.py -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\familyIndex-wiki.html -wb projects/oomp/part/familyIndex

### Upload Directory of Files
	* -rm A (all)
	* -si oomlout (name of profile setup in pywikibot)
	* -fa -wiki.html (what to add to the end of a file)
	* -bd base Directory (this is where we pull everything in from, will look for basedirectory/ID/ID-wiki.html (will get all directory names then try and upload a file for each, using the directory name as the ID)
	
	python %WIKBdirectory%WIKBmain.py -rm A -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\ -wb projects/oomp/part/ -fa '-wiki.html'
