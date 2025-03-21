import os

target=open("dicdata.bin","r")
dicdata=target.read()
target.close()

target=open("entdata.bin","r")
entdata=target.read()
target.close()


path=r"C:\Users\pc\Desktop\Encryption Software"
pathdir=r"C:\Users\pc\AppData\Roaming\Encryption"
isexist = os.path.exists(path)
isexist = os.path.exists(pathdir)

if not isexist:
    os.makedirs(path)
if not isexist:
    os.makedirs(pathdir)



target=open(r'C:\Users\pc\AppData\Roaming\Encryption\directory.py','w')
target.write(dicdata)
target.close()

target=open(r'C:\Users\pc\Desktop\Encryption Software\Encryption.py','w')
target.write(entdata)
target.close()


