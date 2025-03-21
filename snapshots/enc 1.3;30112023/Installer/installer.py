import os

target=open("dicdata.bin","r")
dicdata=target.read()
target.close()

target=open("entdata.bin","r")
entdata=target.read()
target.close()


path=r"C:\Users\pc\Desktop\Encryption Software"
isexist = os.path.exists(path)

if not isexist:
    os.makedirs(path)



target=open(r'C:\Users\pc\Desktop\Encryption Software\directory.py','w')
target.write(dicdata)
target.close()

target=open(r'C:\Users\pc\Desktop\Encryption Software\Encryption.py','w')
target.write(entdata)
target.close()


