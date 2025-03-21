target=open(r'C:\Users\pc\Desktop\Python Projects\Encreption Project\Encryption.py','r')
entdat=target.read()
target.close()

target=open(r"C:\Users\pc\Desktop\Python Projects\Encreption Project\Installer\entdata.bin",'w')
target.write(entdat)
target.close()


target=open(r'C:\Users\pc\Desktop\Python Projects\Encreption Project\directory.py','r')
dicdata=target.read()
target.close()

target=open(r"C:\Users\pc\Desktop\Python Projects\Encreption Project\Installer\dicdata.bin",'w')
target.write(dicdata)
target.close()
