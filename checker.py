from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('/home/DrG/Desktop/DrGFamilyVacation'):
    f.extend(filenames)
    break

g = []
for x in f:
    if '.jpg' in x:
        g.append(x)


password = ""
for part in g:
    password += part.strip('.jpg')

print(password)
