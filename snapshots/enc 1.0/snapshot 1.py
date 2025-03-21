import random

#Orignal Keys

ent=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
ent1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
ent2=["1","2","3","4","5","6","7","8","9","0"];
ent3=["!","@","#","$","%","^","&","*","(",")"," "];

'''
entkey=["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"];
entkey1=["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"];
entkey2=["$","!","@","*","(","%","&",")","^"," "];
entkey3=["#","0","9","6","7","8","4","1","3","5","2"];'''

#Random Character Mapping
def mapping(ent,ent1,ent2,ent3):
    
    entkey=[]
    entkey1=[]
    entkey2=[]
    entkey3=[]

    temp=[]
    for i in range(0,len(ent)):
        temp.append(ent[i]);
    for i in range(0,len(ent1)):
        temp.append(ent1[i]);
    for i in range(0,len(ent2)):
        temp.append(ent2[i]);
    for i in range(0,len(ent3)):
        temp.append(ent3[i]);

    for i in range(0,len(ent)):
        t=random.choice(temp)
        entkey.append(t)
        temp.remove(t)
    for i in range(0,len(ent1)):
        t=random.choice(temp)
        entkey1.append(t)
        temp.remove(t)
    for i in range(0,len(ent2)):
        t=random.choice(temp)
        entkey2.append(t)
        temp.remove(t)
    for i in range(0,len(ent3)):
        t=random.choice(temp)
        entkey3.append(t)
        temp.remove(t)
    temp=[];
    return entkey,entkey1,entkey2,entkey3

'''print(entkey)
print(entkey1)
print(entkey2)
print(entkey3)'''



#Encryption Code
def encrypttion(a,c):
    for i in range(0,len(a)):
        for j in range(len(ent)):
            if a[i] == ent[j]:
                c[i] = entkey[j];
                break

        for j in range(0,len(ent1)):
            if a[i] == ent1[j]:
                c[i] = entkey1[j];
                break
            
        for j in range(0,len(ent2)):
            if a[i] == ent2[j]:
                c[i] = entkey2[j];
                break
            
        for j in range(0,len(ent3)):
            if a[i] == ent3[j]:
                c[i] = entkey3[j];
                break
    #print(a);
    return c




#Decryption Code
def decryption(enc,c):
    a=enc
    for i in range(0,len(a)):
    
        for j in range(0,len(entkey)):
            if a[i] == entkey[j]:
                c[i] = ent[j];
                break
            
        for j in range(0,len(entkey1)):
            if a[i] == entkey1[j]:
                c[i] = ent1[j];
                break

        for j in range(0,len(entkey2)):
            if a[i] == entkey2[j]:
                c[i] = ent2[j];
                break

        for j in range(0,len(entkey3)):
            if a[i] == entkey3[j]:
                c[i] = ent3[j];
                break
    
    return c;




    
#User Input
e=int(input('Press (1) to encrypt string or Press (2) to encrypt file : '))
target=open(r'C:\Users\pc\Desktop\passwords.txt','r+')
    
def value(e,target):
    if e==1:
        
        #b="9406817179@As"
        b=input("Enter data : ")
    elif e==2:
        b=target.read()
    a=[];
    c=[];
    #b=["b","a","e","c","d"];
    for i in range(0,len(b)):
        a.append(b[i]);
    for i in range(0,len(b)):
        c.append(b[i]);
    return a,c;





#Calling User Input
chk,val=value(e,target);







def inputing():
    temp=int(input("Press ('1') for encryption OR Press ('0') for decryption : "))
    seeds=0;
    if temp==0:
        seeds=int(input("Enter the Key : "));
    return temp,seeds;

#calling inputting
d,seeds=inputing();


#seed function
def seeding(d,chk,seeds):
    h=id(chk)
    if d==1:
        random.seed(h);
        print("Your Encryption Key is ",h)
    elif d==0:
        random.seed(seeds);

seeding(d,chk,seeds);
    

# Calling Character Mapping into 4 different list
entkey,entkey1,entkey2,entkey3=mapping(ent,ent1,ent2,ent3);


#Process
def processes(d):
    if d==1:
        enc=encrypttion(chk,val);
        return enc
    elif d==0:
        dec=decryption(chk,val);
        return dec

output=processes(d)
target.write('');
target.close();
target=open(r'C:\Users\pc\Desktop\passwords.txt','r+');
#Display
def display(o,e,target):
    
    for i in range(0,len(o)):
        print(o[i],end="");

    if e==2:
        for i in range(0,len(o)):
            target.write(o[i])
        target.close()

display(output,e,target);
exi=input();




