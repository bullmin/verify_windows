import os
import subprocess as sp
from Crypto.Hash import SHA3_224
from Crypto.Hash import SHA3_256
from Crypto.Hash import SHA3_384
from Crypto.Hash import SHA3_512
from Crypto.Hash import MD5
from Crypto.Hash import SHA512
from Crypto.Hash import SHA1
from Crypto.Hash import SHA256

def verifer(hashresult):
    orHash = input("Input Hash Value for compare >>> ")
    if orHash == hashresult:
        print("Verify : Correct")
    else:
        print("Verify : Incorrect")

def getHash():
    g = True
    while g:
        infLo = input("Input File Location >>> ")
        fLo = os.path.abspath(infLo)
        fName = input("Input File Name >>> ")
        fAbsPath = fLo + "\\" + fName
        if os.path.isfile(fAbsPath) == True:
            break
        else:
            print("Can't Find FIle")

    go = True
    while go:
        print("\nHash Function\n"
              "\t1. MD5\n"
              "\t2. SHA-1\n"
              "\t3. SHA-256\n"
              "\t4. SHA-512\n"
              "\t5. SHA3-224\n"
              "\t6. SHA3-256\n"
              "\t7. SHA3-384\n"
              "\t8. SHA3-512\n"
              "\t0. Quit\n")
        awnser = input("Select Hash Function : ")
        if awnser == "1":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = MD5.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : MD5\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "2":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = SHA1.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : SHA1\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "3":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = SHA256.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : SHA-256\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "4":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = SHA512.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : SHA-512\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "5":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_224.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : SHA3-224\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "6":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_256.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : SHA3-256\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "7":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_384.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : SHA3-384\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "8":
            f = open(fAbsPath, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_512.new()
            hashResult.update(data)
            print("File Location : " + fAbsPath + "\n",
                  "Checksum Type : SHA3-512\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult.hexdigest())
            go = False
        elif awnser == "0" or awnser == "exit" or awnser == "quit":
            print("\n-> Bye!")
            go = False
        else:
            print("Please enter correct command.")


getHash()