import os
import sys
import random
import directory

#User Input (sorf=string or file)

sorf=int(input('Press (1) to encrypt string or Press (2) to encrypt file : '))


if sorf == 2:
    dire=directory.directory();


#target=open(r'C:\Users\pc\Desktop\Encreption Project\passwords.txt','r+')
target=open(dire,"r+")






def value(e,target):
    if e==1:
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
chk,val=value(sorf,target);


def inputing(chk):
    temp=int(input("Press ('1') for encryption OR Press ('0') for decryption : "))
    seeds=id(chk);
    if temp==0:
        seeds=int(input("Enter the Key : "));
    return temp,seeds;

#calling inputting (eord=encrypt or decrypt)
eord,seeds=inputing(chk);


#seed function
def seeding(d,seeds):
    if d==1:
        random.seed(seeds);
        print("Your Encryption Key is ",seeds)
    elif d==0:
        random.seed(seeds);

seeding(eord,seeds);
    











def character_map():
    temp=[];
    for i in range(32,127):
        temp.append(chr(i))
    return(temp);

ent=character_map();

random.seed(0);

def mapping(a):
    temp1=[];
    temp=[];
    for i in range(0,len(a)):
        temp1.append(a[i])
    for i in range(0,len(a)):
        t=random.choice(temp1);
        temp.append(t)
        temp1.remove(t)
    return(temp);

entkey=mapping(ent);







# Encryption Code
def encryption(a,c,ent,entkey):
    for i in range(0,len(a)):
        for j in range(0,len(ent)):
            if a[i] == ent[j]:
                c[i] = entkey[j];
    return(c)



# Decryption Code
def decryption(a,c,ent,entkey):
    for i in range(0,len(a)):
        for j in range(0,len(entkey)):
            if a[i] == entkey[j]:
                c[i] = ent[j];
    return(c)




#process
def process(d):
    if d == 1:
        temp = encryption(chk,val,ent,entkey);
    elif d == 0:
        temp = decryption(chk,val,ent,entkey);
    return temp;



output=process(eord);

target.write("");
target.close();


#target=open(r'C:\Users\pc\Desktop\Encreption Project\passwords.txt','r+');
target=open(dire,"r+")






# Display
def display(o,e,target):
    for i in range(0,len(o)):
        print(o[i],end="");

    if e==2:
        for i in range(0,len(o)):
            target.write(o[i])
        target.close()

display(output,sorf,target);
exi=input("\n\n\n\n\n\n\nPress Enter to Exit");
