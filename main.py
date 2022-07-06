import os
import subprocess as sp


def getHash():
    infLo = input("Input File Location >>> ")
    fLo = os.path.abspath(infLo)
    fName = input("Input File Name >>> ")
    go = True
    while go:
        print("\nHash Function\n"
              "\t1. MD5\n"
              "\t2. SHA-256\n"
              "\t0. Quit\n")
        awnser = input("Select Hash Function : ")
        if awnser == "1":
            os.chdir(fLo)
            cmdResult = sp.getstatusoutput("certutil -hashfile " + fName + " MD5")
            hashResult = cmdResult[1].split("\n")[1]
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : MD5\n",
                  "Check Hash Value : " + hashResult)
        elif awnser == "2":
            os.chdir(fLo)
            cmdResult = sp.getstatusoutput("certutil -hashfile " + fName + " SHA256")
            hashResult = cmdResult[1].split("\n")[1]
            print("File Location : " + fLo + "\\" + fName + "\n",
                  "Checksum Type : MD5\n",
                  "Check Hash Value : " + hashResult)
        elif awnser == "0" or awnser == "exit" or awnser == "quit":
            print("-> Bye!")
            go = False
        else:
            print("Please enter correct command.")


getHash()