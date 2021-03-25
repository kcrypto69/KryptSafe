'''
Project Name : CryptSafe
File Name : restore.py
Description: Given a password, hugeText.txt, cutsList.txt, and initialIgnore.txt,
generate the proper mnemonic phrase.
'''
from progress.bar import Bar
from art import *
import getpass

def main():
    print("---------------------------------------------")
    tprint("CryptSafe", font="small")
    print("Thank you for using CryptSafe!")
    print("You are now in the Restore application.\n")
    print("NOTICE: For your safety, please disconnect from the internet before running.\n")
    print("IMPORTANT: Ensure that all three recovery files (hugeText.txt, initialIgnore.txt,cutsList.txt) are in the directory that you are running this application on.\n")
    print("Thank you for your attention!\n")
    print("DISCLAIMER: I am not responsible for the any losses or damages incurred as a result of your usage of this application!")
    print("---------------------------------------------")
    password = getpass.getpass("Please type in your password and hit enter!\n")

    # Import hugeText.txt
    with open("hugeText.txt","r") as hugeTextFile:
        hugeText = hugeTextFile.read().split(" ")

    # Import cutsList.txt
    with open("cutsList.txt","r") as cutsListFile:
        cutsList = cutsListFile.read().split(" ")

    # Import initialIgnore.txt
    with open("initialIgnore.txt","r") as initialIgnoreFile:
        initialIgnore = initialIgnoreFile.read()

    # Reconstruct the mnemonic phrase with the three files and the password

    # Process the initialIgnore
    for x in range(0,int(initialIgnore)):
        hugeText.pop(0)

    solved = []
    # Process each cut
    for x in range(0,len(cutsList)):
        bar = Bar(' Processing Cut List ' + str(x + 1) + "/" + str(len(cutsList)), suffix='%(percent).1f%% - %(eta)ds', max = int(cutsList[x]))
        #Take ascii of password character
        ascii = ord(password[x]) - 32
        for y in range(0, ascii):
            hugeText.pop(0)
            bar.next()
        # Append first thing in hugeText to solved
        solved.append(hugeText[0])
        bar.next()
        # Delete till the cut
        for z in range(ascii-32,int(cutsList[x])):
            hugeText.pop(0)
            bar.next()
        bar.finish()
    print("---------------------------------------------")
    print("Your Mnemonic Phrase: " + str(solved))
    print("---------------------------------------------")
    print("Thank you for using CryptSafe! Goodbye!")
    print("---------------------------------------------")



if __name__ == "__main__":
   main()
