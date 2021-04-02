from cryptography.fernet import Fernet
import os

pathFile = 'C:\\Users\\Nelson Sanchez\\Documents\\attact'
    
def return_key():
    return open("key.key","rb").read()

def decrypt(items,key):
    i = Fernet(key)
    for x in items:
        with open(x,"rb") as file:
            file_data = file.read()
        data = i.decrypt(file_data)
        
        with open(x,"wb") as file:
            file.write(data)

if __name__ == "__main__":
    try:
        os.remove(pathFile+"\\"+"README.txt")
    except Exception as e:
        print("File does not exists")
    items = os.listdir(pathFile)
    items2 = [pathFile+"\\"+x for x in items]
    
key = return_key()
decrypt(items2,key)

