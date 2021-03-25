'''
Project Name : CryptSafe
File Name: generate.py
Description: Given a mnemonic phrase of a certain length, this program will
generate three items: a 2,000,000-word text file, initialIgnore.txt,
and cutsList.txt
'''
import random
from art import *
import getpass

def listToString(s):
    str1 = " "
    return (str1.join(s))

def main():
    print("---------------------------------------------")
    tprint("CryptSafe", font="small")
    print("Thank you for using CryptSafe!")
    print("You are now in the Generate application.\n")
    print("NOTICE: For your safety, please disconnect from the internet before running.\n")

    print("IMPORTANT: Please ensure that your wallet uses the BIP-39 word list for wallet creation.\n")

    print("WARNING: ALL THREE FILES (hugeText.txt, initialIgnore.txt,cutsList.txt) WILL GET OVERRIDEN AFTER RUNNING THIS APP!")
    print("IF YOU HAVE IMPORTANT INFORMATION, PLEASE CTRL-C NOW AND MOVE THEM OUT!\n")

    print("Thank you for your attention!\n")
    print("DISCLAIMER: I am not responsible for the any losses or damages incurred as a result of your usage of this application!")
    print("---------------------------------------------")

    mnemonic_list = input("Please type in your mnemonic phrase, with each word separated by a comma!\nFor example: cat,dog,mouse,rabbit,...\n").split(",")
    print(mnemonic_list)

    passwordMatch = False;

    while passwordMatch == False:
        password = getpass.getpass("Please type in a password and hit enter!\nThe length of your password must be at least the length of your mnemonic phrase!\n")
        password2 = getpass.getpass("Please confirm your password\n")
        if(password == password2):
            passwordMatch = True;
        else:
            print("Passwords do not match. Please try again!")
        
    # Assume that the user has inputted a valid mnemonic_list for now

    # Second, generate initialIgnore
    initialIgnore = random.randint(10000, 50000)

    # Third, generate cutsList
    cutsList = []
    strCutsList = []
    for x in range(0,len(mnemonic_list)):
        randomCut = random.randint(10000, 50000)
        cutsList.append(randomCut)
        strCutsList.append(str(randomCut))

    # Fourth, generate the huge text file (using initialIgnore and cutsList)
    hugeText = []
    with open("wordlist.txt","r") as bip39:
        data = bip39.read().split("\n")
        data.pop(-1)

    # Handle initialIgnore
    for x in range(0,initialIgnore):
        hugeText.append(random.choice(data))

    # Handle password with cuts
    for x in range(0,len(mnemonic_list)):
        # Get the ASCII of the corresponding character in the password
        ascii = ord(password[x]) - 32
        for y in range(0, ascii):
            hugeText.append(random.choice(data))
        hugeText.append(mnemonic_list[x])
        for z in range(ascii-31,cutsList[x]):
            hugeText.append(random.choice(data))

    # Export all the relevant files

    try:
        with open("hugeText.txt","w") as hugeTextFile:
            hugeTextFile.write(listToString(hugeText))

        with open("cutsList.txt","w") as cutsListFile:
            cutsListFile.write(listToString(strCutsList))

        with open("initialIgnore.txt","w") as initialIgnoreFile:
            initialIgnoreFile.write(str(initialIgnore))

        print("---------------------------------------------")
        print("NOTICE: All three files have been successfully generated.\n")
        print("IMPORTANT: Please test them using python restore.py to ensure that it works.\n")

        print("Afterwards, you can make as many copies of these files anywhere you like.")
        print("e.g.: Digitally: Google Drive, Microsoft OneDrive, iCloud, in your phone's notes,etc.")
        print("e.g.: Physically: in a safe, in a drawer, under your bed, etc.")
        print("---------------------------------------------")
    except Exception as e:
        print("NOTICE: Something went wrong somewhere with file creation. Sorry about that!")
        print("Please send me an issue on Github and attach the exception message below. Thank you!\n")
        print("https://www.github.com/kcrypt69/CryptSafe/issues\n")
        print(e)
        print("---------------------------------------------")



if __name__ == "__main__":
   main()
