import os
import time
delCounter = 0
while (delCounter <= 101):
    os.system("userdel level" + str(delCounter) + " --force --remove &> /dev/null")
    #"userdel level“+delCounter+” --force --remove"
    delCounter+=1
    time.sleep(.2)

