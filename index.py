#  Renam Mp3 files with title and artist 
#  Author : Hamza Hassan
#  Date : 13 - 05-2020
#  Put all mp3 files inside "mp3files" path 
#  and run index.py 
#  All renamed files will be in "mp3files/renamed/" path




import os


arr = os.listdir('mp3files')


from eyed3 import id3
import shutil
for l in arr:
	 
	if ( l[-1:] == '3'): #check if file is mp3files
		tag = id3.Tag()
		tag.parse('mp3files/'+l)
		title = str(tag.title)
		if(str(title) != "None"): #if file title is empty escape it's name
			if os.path.exists('mp3files/renamed/'+str(tag.title)+"-"+str(tag.artist)+'.mp3') == False:
				os.rename('mp3files/'+l, 'mp3files/renamed/'+str(tag.title)+"-"+str(tag.artist)+'.mp3')
				
			else:
				shutil.move('mp3files/'+l, 'mp3files/renamed/'+l)

