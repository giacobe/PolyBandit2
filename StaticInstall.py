import hashlib
import base64
import os
import random
import gzip
import sys


def heroNameGen():
    heroNames = ["Dr Giacobe", "The Nittany Lion", "President Barron"]
    return random.choice(heroNames)


def goalNameGen():
    goalNames = ["Canvas account", "Lionpath account","Outlook account"]
    return random.choice(goalNames)


def giveRanLetter():
    letterArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                   "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return random.choice(letterArray)


def makeRanString(len):
    count = 0
    name = ''
    while (count < len):
        name += giveRanLetter()
        count += 1
    return name


def makePassword(len,username,levelname):
    encodeSeed = username + levelname
    hashed = hashlib.md5(encodeSeed.encode('utf-8'))
    based = base64.b64encode(hashed.digest())
    passwordToFind = str(based)
    passwordToReturn = passwordToFind[2:len+2]

    return passwordToReturn

def makeFakePassword(len):
    return makePassword(len,makeRanString(13),makeRanString(7))

def makeMe(desiredName):
    dirName = os.path.dirname(desiredName)
    if not os.path.exists(dirName):
        os.makedirs(dirName)

def makeOpener(levelName,stringToWrite):
    opener = stringToWrite
    makeMe("/home/" + levelName + "/README.txt")
    f = open("/home/" + levelName + "/README.txt", "w")
    starBar = ''
    i = 0
    while(i < len(stringToWrite)):
        starBar+='*'
        i = i + 1

    f.write(starBar+'\n')
    f.write(opener)
    f.write(starBar+'\n')
    f.write("Once you find the password, log into the next level with the password.\nExample: You've completed level1 now SSH into level2\n")
    f.write(starBar+'\n')
    f.close()
    makeMe("/home/" + levelName + "/.bashrc")
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")



def level0(paswardone,levelName):
    makeOpener(levelName, heroNameGen() + "'s password for their " + goalNameGen() + " is in inhere.txt\n")
    makeMe("/home/"+levelName+"/inhere.txt")
    g = open("/home/"+levelName+"/inhere.txt", "w")
    g.write(paswardone)
    g.close()
    os.system('chown '+levelName+':'+levelName+' /home/'+levelName+'/inhere.txt;')


def level1(passwardTwo,levelName):
    makeOpener(levelName,heroNameGen() + "'s password for their " + goalNameGen() + " account is in inhere.txt but something is off, the file is hidden!\nYou will have to search for hidden files to get it.\n")
    makeMe("/home/"+levelName+"/.inhere.txt")
    g = open("/home/"+levelName+"/.inhere.txt", "w")
    g.write(passwardTwo)
    g.close()
    os.system('chown '+levelName+':'+levelName+' /home/'+levelName+"/.inhere.txt;")


def level2(passwardThree,levelName):
    makeOpener(levelName,heroNameGen() + "'s password for their " + goalNameGen() + " is in the file that is only 9 bytes long.\n")

    password_spot = random.randint(1, 9)
    count = 0
    while (count < 10):
        ran_fileName = makeRanString(8)
        makeMe("/home/"+levelName+"/" + ran_fileName)
        if count == password_spot:
            f = open("/home/"+levelName+"/" + ran_fileName, "w")
            f.write(passwardThree)
            f.close()
            os.system("chown "+levelName+":"+levelName+" \"/home/"+levelName+"/\"" + ran_fileName)
            count += 1
        else:
            string_len = random.randint(1, 50) + 25
            count2 = 0
            file_string = ""
            while count2 < string_len:
                file_string += giveRanLetter()
                count2 += 1

            makeMe("/home/"+levelName+"/" + ran_fileName)
            f = open("/home/"+levelName+"/" + ran_fileName, "w")
            f.write(file_string)
            f.close()
            os.system("chown "+levelName+":"+levelName+" \"/home/"+levelName+"/\"" + ran_fileName)
            count += 1


def level3(passwardFour,levelName):
    password_spot = random.randint(1, 256)
    count = 0
    hint = makeRanString(8)
    while (count < 256):
        if count == password_spot:
            rand_pass = hint + "      " + passwardFour
            makeMe("/home/"+levelName+"/inhere.txt")
            f = open("/home/"+levelName+"/inhere.txt", "a")
            f.write(rand_pass)
            f.close()
            count += 1
        else:
            rand_pass = makeRanString(8) + "      " + makeFakePassword(8) + "\n"
            makeMe("/home/"+levelName+"/inhere.txt")
            f = open("/home/"+levelName+"/inhere.txt", "a")
            f.write(rand_pass)
            count += 1
    makeOpener(levelName,"The password you seek is next to the line.... " + hint + "\n")
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt;")


def level4(passwardFour,levelName):
    makeOpener(levelName,heroNameGen() + "'s password for their " + goalNameGen() + " is next to the word you would find last when sorted alphabetically.\n")

    makeMe("/home/"+levelName+"/inhere.txt")
    f = open("/home/"+levelName+"/inhere.txt", "w")
    f.write("")
    f.close()
    wordsSet = (
        " inside, jazz , moth , lamp , light , glass , mattress , pillow , television , whale , spoon , overt , grab , pull , delicate , obstruct , tendency , sore , cloth , redundant , staking , meek , implant , homely , plan , screw , motivate , stereo , typed , protective , lacking , verify , camp , wire , umbrella , eager , weight , competition , shed , irate , seat , scab , square , undo , bat , like , pot , land , watch , patch , ripe , eyes , rabid , brother , nondescript , use , retire , heal , infect , assert , calculating , versed , teeny , father , ashamed , occupy , boundless , reaction , mom , forbidden , dangle , concerned , fantastic , efficient , convict , sentence , glamorous , creator , cow , taking , glib , cruel , tedious , gain , say , wide-eyed , stranger , elbow , wax , beam , burly , order , behold , baseball , library , pollute , sassy , bread , war , slip , silent , fat , soft , unable , ducks , mellow , sophisticated , gag , shock , wealth , summer , stir , tire , replace , bring , vie , refuse , print , sit , nail , snack , sneeze , assorted , cracker , converge , psychedelic , co-operate , disturb , pray , hope , substance , nonchalant , capture , signal , fretful , consult , ubiquitous , output , thirsty , crayon , many , healthy , quit , expand , rail , wrench , under , stand , hold , late , pump , admit , vein , football , flowery , valuable , outrageous , fang , grind , secretary , rhetorical , love , observant , enlighten , lock , extend , reset , stitch , run , tremble , anxious , tourist , expensive , consort , stone , special , magic , justify , redo , exclaim , boiling , beggar , weapon , translate , dogs , fragile , cook , impossible , selection , insidious , cattle , envy , bright , teeth , scarf , polish , rich , clean , indulge , glow , nation , sponge , aloof , plod , tree , locket , match , tidy , stingy , rid , little , smelly , male , salute , cause , yawn , scan , question , hinder , pushy , hit , idolize , deserted , gun , husky , vacuous , tank , unequaled , sacrifice , remarkable , call , participate , talk , wrist , observe , zonked , weave , slink , cakes , tart , stick , recollect , crush , number , material , detach , hall , ultra , spoil , aboard , bray , curtain , lie , mold , enchanting , structure")
    words = wordsSet.split(",")
    random.shuffle(words)
    count = 0
    while (count < len(words)):

        if words[count] == " zonked ":
            ans = passwardFour
            f = open("/home/" + levelName + "/inhere.txt", "a")
            f.write(words[count] + "      " + ans)
            f.close()

        else:
            ans = makeFakePassword(8)
            f = open("/home/"+levelName+"/inhere.txt", "a")
            f.write(words[count] + "      " + ans + '\n')
            f.close()

        count += 1
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt;")


def level5(passwardSix,levelName):
    makeOpener(levelName,heroNameGen() + "'s password for their " + goalNameGen() + " is inside the file named inhere.txt\n")


    password_spot1 = random.randint(1, 10)
    password_spot2 = random.randint(1, 10)
    password_spot3 = random.randint(1, 10)
    count = 0
    while (count < 10):
        rand_dir1 = makeRanString(8)
        makeMe("/home/"+levelName+"/" + rand_dir1)
        count2 = 0
        while (count2 < 10):
            rand_dir2 = makeRanString(8)
            makeMe("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2)
            count3 = 0
            while (count3 < 10):
                if count == password_spot1 and count2 == password_spot2 and count3 == password_spot3:
                    makeMe("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/inhere.txt')
                    g = open("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/inhere.txt', "w")
                    g.write(passwardSix)
                    g.close()
                    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + "/inhere.txt;")
                else:
                    rand_file = makeRanString(8)

                    makeMe("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/' + rand_file)

                    g = open("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/' + rand_file, "w")
                    g.write(makeFakePassword(8))
                    g.close()
                    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/' + rand_file + ';')
                count3 += 1
            count2 += 1
        count += 1


def level6(passwardSeven,levelName):
    makeOpener(levelName,heroNameGen() + "'s password for their " + goalNameGen() + " is in the inhere.txt file, how ever they seem to have accidentally gzipped it. Can you help them?\n")


    makeMe("/home/"+levelName+"/inhere.txt")
    g = gzip.open("/home/"+levelName+"/inhere.txt.gz", "wb")
    g.write(passwardSeven.encode())
    g.close()
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt.gz;")


def level7(passwardEight,levelName):
    makeOpener(levelName,heroNameGen() + "'s password for their " + goalNameGen() + " is in the inhere.txt file, how ever they seem to have lost permission to read it\n")


    makeMe("/home/"+levelName+"/inhere.txt")
    g = open("/home/"+levelName+"/inhere.txt", "w")
    g.write(passwardEight)
    g.close()
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt;")
    os.system("chmod 333 /home/"+levelName+"/inhere.txt;")


def level8(passwordNine,levelName):
    passwordCount = random.randint(1, 255)
    makeOpener(levelName,
            heroNameGen() + "'s password for their " + goalNameGen() + " is in an unknown file. But they do believe the file had " + str(
        passwordCount) + " words. \n the password should be the last word in the file.\n")


    passwordSpot = random.randint(1, 10)
    i = 0
    while i <= 10:
        filName = makeRanString(8) + ".txt"
        makeMe("/home/"+levelName+"/" + filName)
        if i == passwordSpot:
            # now to generate the words-1
            x = 0
            toPut = ""
            while x < passwordCount - 1:
                toPut += makeRanString(8) + '\n'
                x += 1
            toPut += passwordNine
            f = open("/home/"+levelName+"/" + filName, "+w")
            f.write(toPut)
            f.close

        else:
            # now to generate the words-1
            x = 0
            toPut = ""
            numTOBe = random.randint(1, 255)
            if numTOBe == passwordCount:
                numTOBe += 1
            while x < numTOBe:
                toPut += makeRanString(8) + '\n'
                x += 1
            f = open("/home/"+levelName+"/" + filName, "+w")
            f.write(toPut)
            f.close
        i += 1


def level9(passwardTen,levelName):
    opener = (
            heroNameGen() + "'s password for their " + goalNameGen() + " account is in inhere.txt But there are some issues. The file's been hidden and they wrote the name with a space\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()

    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")
    g = open("/home/"+levelName+"/.in here.txt", "w+")
    g.write(passwardTen)
    g.close()


def level10(passwordEleven,levelName):
    makeOpener(levelName,heroNameGen() + "'s password for their " + goalNameGen() + " is the only different word\n")


    makeMe("/home/"+levelName+"/inhere1.txt")
    f = open("/home/"+levelName+"/inhere1.txt", "w")
    f.write('')
    f.close()
    makeMe("/home/"+levelName+"/inhere2.txt")
    f = open("/home/"+levelName+"/inhere2.txt", "w")
    f.write('')
    f.close()

    password_spot = random.randint(0, 256)
    count = 0
    while (count < 256):
        rand_pass = makeFakePassword(8)
        f = open("/home/"+levelName+"/inhere1.txt", "a")
        if count == password_spot:
            f.write(passwordEleven)
        else:
            f.write(rand_pass)
        f.close()
        f = open("/home/" +levelName+ "/inhere2.txt", "a")
        f.write(rand_pass)
        f.close()
        count += 1
    os.system("chown " +levelName+ ":" +levelName+ " /home/" +levelName+"/inhere1.txt;")
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere2.txt;")


def level11(password,levelName):
    makeOpener(levelName, heroNameGen() + " accidentally encoded their " + goalNameGen() + " password in base 64! They cant read whatever is in inhere.txt but maybe you can?\n")


    makeMe("/home/"+levelName+"/inhere.txt")
    g = open("/home/"+levelName+"/inhere.txt", "w+")
    g.write(str(base64.b64encode(password.encode("utf-8")), "utf-8") + '\n')
    g.close()



def makeLevelHome(levelPassword,levelName):
    os.system(
        "useradd "+ levelName +" --create-home --password \"$(openssl passwd -1 " + levelPassword + ")\" --shell /bin/bash --user-group")

def genRanLevel(nextLevelPassword,levelName):
    bigRan = random.randint(1,11)
    if bigRan == 1:
        level1(nextLevelPassword,levelName)
    if bigRan == 2:
        level2(nextLevelPassword,levelName)
    if bigRan == 3:
        level3(nextLevelPassword,levelName)
    if bigRan == 4:
        level4(nextLevelPassword,levelName)
    if bigRan == 5:
        level5(nextLevelPassword, levelName)
    if bigRan == 6:
        level6(nextLevelPassword, levelName)
    if bigRan == 7:
        level7(nextLevelPassword, levelName)
    if bigRan ==8:
        level8(nextLevelPassword,levelName)
    if bigRan ==9:
        level9(nextLevelPassword,levelName)
    if bigRan == 10:
        level10(nextLevelPassword,levelName)
    if bigRan == 11:
        level11(nextLevelPassword,levelName)


print("Welcome to PolyBandit initial setup! Please follow the instructions as they come on screen.\n")
username = input("Please enter your Penn State email address. Example: acb1234@psu.edu\n")
print("Thank you! Setting up your levels now! Please hold...")
sys.stdout.write("[")
sys.stdout.flush()
passwordToBe = makePassword(8,username,'level1')+'\n'
makeLevelHome("level0","level0")
level0(passwordToBe,"level0")
makeLevelHome(passwordToBe,"level1")
sys.stdout.write("*")
sys.stdout.flush()

passwordToBe = makePassword(8,username,'level2')+'\n'
level1(passwordToBe,"level1")
makeLevelHome(passwordToBe,"level2")
sys.stdout.write("*")
sys.stdout.flush()


passwordToBe = makePassword(8,username,'level3')+'\n'
level2(passwordToBe,"level2")
makeLevelHome(passwordToBe,"level3")
sys.stdout.write("*")
sys.stdout.flush()



passwordToBe = makePassword(8,username,'level4')+'\n'
level3(passwordToBe,"level3")
makeLevelHome(passwordToBe,"level4")
sys.stdout.write("*")
sys.stdout.flush()


passwordToBe = makePassword(8,username,'level5')+'\n'
level4(passwordToBe,"level4")
makeLevelHome(passwordToBe,"level5")
sys.stdout.write("*")
sys.stdout.flush()



passwordToBe = makePassword(8,username,'level6')+'\n'
level5(passwordToBe,"level5")
makeLevelHome(passwordToBe,"level6")
sys.stdout.write("*")
sys.stdout.flush()



passwordToBe = makePassword(8,username,'level7')+'\n'
level6(passwordToBe,"level6")
makeLevelHome(passwordToBe,"level7")
sys.stdout.write("*")
sys.stdout.flush()


passwordToBe = makePassword(8,username,'level8')+'\n'
level7(passwordToBe,"level7")
makeLevelHome(passwordToBe,"level8")
sys.stdout.write("*")
sys.stdout.flush()



passwordToBe = makePassword(8,username,'level9')+'\n'
level8(passwordToBe,"level8")
makeLevelHome(passwordToBe,"level9")
sys.stdout.write("*")
sys.stdout.flush()



passwordToBe = makePassword(8,username,'level10')+'\n'
level9(passwordToBe,"level9")
makeLevelHome(passwordToBe,"level10")
sys.stdout.write("*")
sys.stdout.flush()



passwordToBe = makePassword(8,username,'level11')+'\n'
level10(passwordToBe,"level10")
makeLevelHome(passwordToBe,"level11")
sys.stdout.write("*")
sys.stdout.flush()



passwordToBe = makePassword(8,username,'level12')+'\n'
level11(passwordToBe,"level11")
makeLevelHome(passwordToBe,"level12")
sys.stdout.write("*")
sys.stdout.flush()






levelCount = 12
while levelCount <= 100:
    passwordToBe = passwordToBe = makePassword(8,username,'level'+str(levelCount))+'\n'
    genRanLevel(passwordToBe,"level"+str(levelCount))
    levelCount += 1
    makeLevelHome(passwordToBe,"level"+str(levelCount))
    sys.stdout.write("*")
    sys.stdout.flush()

sys.stdout.write("]")
sys.stdout.flush()
print("\n")
print("ALL done!\n")


print("The password to level 0 localhost is “level0” Please log into level 0 by using the ssh command\n")
print("hint: ssh level0@localhost is the command you will need to use")












