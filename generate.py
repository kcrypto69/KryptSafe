'''
Project Name : CryptSafe
File Name: generate.py
Description: Given a mnemonic phrase of a certain length, this program will
generate three items: a 2,000,000-word text file, initialIgnore.txt,
and cutsList.txt
'''
import random

def listToString(s):
    str1 = " "
    return (str1.join(s))

def main():
    print("---------------------------------------------")
    print("Thank you for using CryptSafe!")
    print("For your safety, please inspect the source code before running!")
    print("Please ensure that your wallet adheres to the BIP-39 word list for wallet creation!\n")
    print("ALL THREE FILES (hugeText.txt, initialIgnore.txt,cutsList.txt) WILL GET OVERRIDEN AFTER RUNNING THIS APP!")
    print("IF YOU HAVE IMPORTANT INFORMATION, PLEASE CTRL-C NOW AND MOVE THEM OUT!\n")
    print("Thank you for your attention!\n")
    print("DISCLAIMER: I am not responsible for the any losses or damages incurred as a result of your usage of this application!")
    print("---------------------------------------------")

    mnemonic_list = input("Please type in your mnemonic phrase, with each word separated by a comma!\nFor example: cat,dog,mouse,rabbit,...\n").split(",")
    print(mnemonic_list)

    password = input("Please type in a password!\nThe length of your password must be at least the length of your mnemonic phrase!\n")

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

    with open("hugeText.txt","w") as hugeTextFile:
        hugeTextFile.write(listToString(hugeText))

    with open("cutsList.txt","w") as cutsListFile:
        cutsListFile.write(listToString(strCutsList))

    with open("initialIgnore.txt","w") as initialIgnoreFile:
        initialIgnoreFile.write(str(initialIgnore))

if __name__ == "__main__":
   main()
