import os
import sys
if os.name=="nt":
	import colorama
	colorama.init()
directory=os.path.dirname(os.path.abspath(__file__))
print("\u001b[31mRed Color means a lossy file gets converted\n\u001b[32mGreen Color means a Lossless file gets converted\u001b[0m")
for dirpath,dirnames,filenames in os.walk(os.path.abspath(directory)):
	dirpath+="/"
	for filename in filenames:
		filename = os.fsdecode(filename)
		if filename.lower().endswith(".wav") or filename.lower().endswith(".aiff") or filename.lower().endswith(".au") or filename.lower().endswith(".ape") or filename.lower().endswith(".wv") or filename.lower().endswith(".tta") or filename.lower().endswith(".aa3") or filename.lower().endswith(".oma") or filename.lower().endswith(".at3") or filename.lower().endswith(".at9") or filename.lower().endswith(".m4a") or filename.lower().endswith(".wma") or filename.lower().endswith(".shn") or filename.lower().endswith(".mpc") or filename.lower().endswith(".mp+") or filename.lower().endswith(".mpp") or filename.lower().endswith(".3gp") or filename.lower().endswith(".m4b") or filename.lower().endswith(".m4p") or filename.lower().endswith(".m4r") or filename.lower().endswith(".m4v") or filename.lower().endswith(".aac"):
			print(dirpath+"\u001b[32m"+str(filename)+"\u001b[0m")
			os.system("ffmpeg -y -loglevel panic -i \""+dirpath+filename+"\" \""+dirpath+filename+".flac\"")
			os.remove(dirpath+filename)
		elif filename.lower().endswith(".ogg") or filename.lower().endswith(".ogg.flac") or filename.lower().endswith(".mp3.flac"):
			print(dirpath+"\u001b[31m"+str(filename)+"\u001b[0m")
			os.system("ffmpeg -y -loglevel panic -i \""+dirpath+filename+"\" \""+dirpath+filename+".mp3\"")
			os.remove(dirpath+filename)
inpot=input('Finished!')