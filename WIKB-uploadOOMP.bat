@echo off
set WIKBdirectory=C:\GH\oomlout-WIKB\


echo on

REM     UPLOADING Index Files

	REM PictureIndex
python %WIKBdirectory%WIKBmain.py -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\pictureIndex-wiki.html -wb projects/oomp/part/pictureIndex

	REM FamilyIndex
python %WIKBdirectory%WIKBmain.py -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\familyIndex-wiki.html -wb projects/oomp/part/familyIndex 

	REM AllParts
python %WIKBdirectory%WIKBmain.py -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\allParts-wiki.html -wb projects/oomp/part/allParts




REM     Uploading all part pages
REM python %WIKBdirectory%WIKBmain.py -rm A -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\ -wb projects/oomp/part/ -fa '-wiki.html'


