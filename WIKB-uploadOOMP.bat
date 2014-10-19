@echo off
set WIKBdirectory=C:\GH\oomlout-WIKB\


echo on

REM     UPLOADING Index Files
python %WIKBdirectory%WIKBmain.py -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\familyIndex-wiki.html -wb projects/oomp/part/ 



REM     Uploading all part pages
python %WIKBdirectory%WIKBmain.py -rm A -si oomlout -bd C:\KB\oomp-scripts\oomp-gen\parts\ -wb projects/oomp/part/ -fa '-wiki.html'


