import random
import os

def makeMe(desiredName):
    dirName = os.path.dirname(desiredName)
    if not os.path.exists(dirName):
        os.makedirs(dirName)

def makeSomeNoise(filePath):
    fileTypeBlock = ['.txt','.mp3','.mp4','.sh']
    #We need to make some fake .txt's, .mp3, .mp4. We will throw in jpg noises in the second iteration of this test
    path = filePath + '/' + makeRanString(4)+fileTypeBlock[random.randint(0,3)]
    makeMe(path)
    f = open(path, "w")
    f.write('')
    f.close()
    os.system("chown DrG:DrG " + path)


os.system("useradd DrG --create-home --password \"$(openssl passwd -1 password)\" --shell /bin/bash --user-group")
os.system("chown DrG:DrG /home/DrG/")

makeMe("/home/DrG/Desktop/")
makeMe("/home/DrG/Desktop/DrGFamilyVacation")
makeMe("/home/DrG/Documents")
makeMe("/home/DrG/Downloads")
makeMe("/home/DrG/Music")
makeMe("/home/DrG/Pictures")
makeMe("/home/DrG/Videos")


def giveRanLetter():
    letterArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return random.choice(letterArray)

def makeRanString(len):
    count = 0
    name = ''
    while (count < len):
        name += giveRanLetter()
        count+=1
    return name

passwordBlock = [makeRanString(4),makeRanString(4),makeRanString(4)]
passwordBlock.sort()
MadePassword = passwordBlock[0]+passwordBlock[1]+passwordBlock[2]

os.system("useradd DrGVictory --create-home --password \"$(openssl passwd -1 "+MadePassword+")\" --shell /bin/bash --user-group")


#The password will be a combination of 3 file names, each file name with be a 4 length string. Making the final password 12 len. In order the photos will be 1_RANDOM 2_RANDOM 3_RANDOM.jpg's
#They will be placed together in SOME location. Now the end result will demand they are placed into the family vacation in the desktop.

whatArea = random.randint(1,6)

#Desktop is one, documents is two and so forth
def makeZone(ZoneName,areaNumber):
    howMuchNoise = random.randint(0,20)
    counter = 0
    while counter <= howMuchNoise:
        makeSomeNoise('/home/DrG/'+ZoneName)
        counter+=1
    if whatArea == areaNumber:
        makeMe("/home/DrG/"+ZoneName+"/"+  passwordBlock[0]+'.jpg')
        g = open("/home/DrG/"+ZoneName+"/"+  passwordBlock[0]+'.jpg',"w+")
        g.write("1")
        g.close()
        os.system("chown DrG:DrG /home/DrG/"+ZoneName+"/"+  passwordBlock[0]+'.jpg')

        makeMe("/home/DrG/"+ZoneName+"/" + passwordBlock[1]+'.jpg')
        g = open("/home/DrG/" + ZoneName + "/" + passwordBlock[1] + '.jpg',"w+")
        g.write("2")
        g.close()
        os.system("chown DrG:DrG /home/DrG/" + ZoneName + "/" + passwordBlock[1] + '.jpg')
        makeMe("/home/DrG/"+ZoneName+"/" + passwordBlock[2]+'.jpg')
        g = open("/home/DrG/" + ZoneName + "/" + passwordBlock[2] + '.jpg',"w+")
        g.write("3")
        g.close()
        os.system("chown DrG:DrG /home/DrG/" + ZoneName + "/" + passwordBlock[2] + '.jpg')








makeZone("Desktop",1)
makeZone("Documents",2)
makeZone("Downloads",3)
makeZone("Music",4)
makeZone("Pictures",5)
makeZone("Videos",6)



#Now we have to put the 'checker' app in the inhere, along with the readme


makeMe("/home/DrG/Desktop/DrGFamilyVacation/README.txt")
opener = "Dr G has lost his family vacation photos somehwere on this machine, and wants them returned to this file! Run the Python script called 'checker' when done to get your password. \n"
generalOpener = open("/home/DrG/Desktop/DrGFamilyVacation/README.txt","w+")
generalOpener.write(opener)
generalOpener.close()
os.system("echo \"cd /home/DrG/Desktop/DrGFamilyVacation/\" >> /home/DrG/.bashrc")
os.system("echo \"cat README.txt\" >> /home/DrG/Desktop/DrGFamilyVacation/.bashrc")


makeMe("/home/DrG/Desktop/DrGFamilyVacation/checker.py")
g = open("/home/DrG/Desktop/DrGFamilyVacation/checker.py","w+")
g.write("from os import walk\n\nf = []\nfor (dirpath, dirnames, filenames) in walk(\'/home/DrG/Desktop/DrGFamilyVacation\'):\n   f.extend(filenames)\n   break\ng = []\nfor x in f:\n   if \'.jpg\' in x:\n      g.append(x)\n\n\npassword = \"\"\nfor part in g:\n   password += part.strip('.jpg')\nprint(password)")
g.close()

os.system("chmod 7777 /home/DrG/Desktop/")
os.system("chmod 7777 /home/DrG/Desktop/DrGFamilyVacation/")
os.system("chmod 7777 /home/DrG/Documents/")
os.system("chmod 7777 /home/DrG/Downloads/")
os.system("chmod 7777 /home/DrG/Music/")
os.system("chmod 7777 /home/DrG/Pictures/")
os.system("chmod 7777 /home/DrG/Videos/")




print("The password to DrG is password")
#First run through lets just propogate each one with a bunch of items. Later iterations are gonna have subfiles on subfiles, and then the third level will have the pictures we seek in different locations from eachother. Lastly we will move on from having just .jpg's we search for

