from PIL import Image
import math

#Definitions
iHeigth = 300
iWidth = 150
iGridWidth = 6.0 #items
i = 0 #counts the current note index

#Open fingering images
si0 = Image.open("Notes/si0.jpg")
do = Image.open("Notes/do.jpg")
re = Image.open("Notes/re.jpg")
mi = Image.open("Notes/mi.jpg")
fa = Image.open("Notes/fa.jpg")
sol = Image.open("Notes/sol.jpg")
la = Image.open("Notes/la.jpg")
si = Image.open("Notes/si.jpg")
do2 = Image.open("Notes/do2.jpg")

#Create dictionaries
dec = {'b0':si0, 'c':do, 'd':re, 'e':mi, 'f':fa, 'g':sol, 'a':la, 'b':si, 'c2':do2}

#Open & Read original file
f = open('Example/Carolina.txt', 'r')
fname = f.name.split('.')
fname = fname[0]
notes = f.read().split()

#Generate output file
iOutHeigth = int(math.ceil(len(notes) / iGridWidth)) * iHeigth
iOutWidth = int(150 * iGridWidth)
out = Image.new("RGB",(iOutWidth ,iOutHeigth))

#Go over the notes list and paste the corresponding images 
#inside the corresponding place of the output file
for note in notes:
	iPosX = int(i % iGridWidth) * iWidth
	iPosY = int(i // iGridWidth) * iHeigth
	i+=1
	out.paste(dec[note],(iPosX,iPosY))

out.save(fname+".jpg","JPEG")