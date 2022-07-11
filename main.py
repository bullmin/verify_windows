import os
import subprocess as sp
from Crypto.Hash import SHA3_224
from Crypto.Hash import SHA3_256
from Crypto.Hash import SHA3_384
from Crypto.Hash import SHA3_512

def verifer(hashresult):
    orHash = input("Input Hash Value for compare >>> ")
    if orHash == hashresult:
        print("Verify : Correct")
    else:
        print("Verify : Incorrect")

def getHash():
    infLo = input("Input File Location >>> ")
    fLo = os.path.abspath(infLo)
    fName = input("Input File Name >>> ")
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
            os.chdir(fLo)
            cmdResult = sp.getstatusoutput("certutil -hashfile " + fName + " MD5")
            hashResult = cmdResult[1].split("\n")[1]
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : MD5\n",
                  "Check Hash Value : " + hashResult)
            verifer(hashResult)
            go = False
        elif awnser == "2":
            os.chdir(fLo)
            cmdResult = sp.getstatusoutput("certutil -hashfile " + fName + " SHA1")
            hashResult = cmdResult[1].split("\n")[1]
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : SHA-1\n",
                  "Check Hash Value : " + hashResult)
            verifer(hashResult)
            go = False
        elif awnser == "3":
            os.chdir(fLo)
            cmdResult = sp.getstatusoutput("certutil -hashfile " + fName + " SHA256")
            hashResult = cmdResult[1].split("\n")[1]
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : SHA-256\n",
                  "Check Hash Value : " + hashResult)
            verifer(hashResult)
            go = False
        elif awnser == "4":
            os.chdir(fLo)
            cmdResult = sp.getstatusoutput("certutil -hashfile " + fName + " SHA512")
            hashResult = cmdResult[1].split("\n")[1]
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : SHA-512\n",
                  "Check Hash Value : " + hashResult)
            verifer(hashResult)
            go = False
        elif awnser == "5":
            f = open(fLo +"\\" +fName, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_224.new()
            hashResult.update(data)
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : SHA3-224\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult)
            go = False
        elif awnser == "6":
            f = open(fLo +"\\" +fName, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_256.new()
            hashResult.update(data)
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : SHA3-256\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult)
            go = False
        elif awnser == "7":
            f = open(fLo +"\\" +fName, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_384.new()
            hashResult.update(data)
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : SHA3-384\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult)
            go = False
        elif awnser == "8":
            f = open(fLo +"\\" +fName, "rb")
            data = f.read()
            f.close()
            hashResult = SHA3_512.new()
            hashResult.update(data)
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : SHA3-512\n",
                  "Check Hash Value : " + hashResult.hexdigest())
            verifer(hashResult)
            go = False
        elif awnser == "0" or awnser == "exit" or awnser == "quit":
            print("\n-> Bye!")
            go = False
        else:
            print("Please enter correct command.")


getHash()