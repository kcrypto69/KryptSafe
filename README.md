# KryptSafe

Welcome to the KryptSafe Repository, where you will find a better way to store your crypto wallet mnemonic phrase.

## Permanent Competition

As a personal vote of confidence in KryptSafe, I have exposed one of the generated files, hugeText.txt, in this repository. This is one in four items required to restore the mnemonic phrase, the other three being my password, initialIgnore.txt, and cutsList.txt.

If you can break into the wallet, you can have all the crypto in it:
https://bscscan.com/address/0xE2e12F7483D3E341d7229b1aB7589D09E10654e1

This competition will run perpetually.

## What is KryptSafe, how does it work (and why it's better)?

KryptSafe is similar to existing mnemonic storage solutions in that you still have to store files, either on paper or in a hard-drive. Also, KryptSafe is similar to wallets in that you MUST own your password.

However, with KryptSafe, you will get three files that serve as substitutes. You can choose to store these files, and your password as a raw text file, anywhere you want, whether online or offline. To restore your mnemonic phrase, you need all three files and your password. Individually, each file and your password has zero value.

If a would-be attacker cannot get hold of all four pieces of information, you are safe. The same cannot be said if they get hold of your raw mnemonic phrase.

### Preparation

1. Install the latest version of Python on your system. Please visit https://www.python.org for more information
2. Download or clone this repository on your local system and cd into it via your terminal.
3. Run this command: pip install -r requirements.txt

### Generating the encryption files

1. DISCONNECT your computer from the internet.
2. Run python generate.py and follow the instructions.
3. After that's done, you will now find some files in your current directory, namely initialIgnore.txt, cutsList.txt, and hugeText.txt.
4. IMPORTANT: CHECK IF EVERYTHING WENT WELL by running python restore.py and following the instructions.
5. Record your password and store it somewhere.
6. If all is well, reconnect your computer to the internet.
7. Choose how you want to store your three files and your password.
8. You're done!

### Obtaining your Mnemonic phrase

1. For added safety, DISCONNECT from the internet.
2. Please ensure that you have initialIgnore.txt, cutsList.txt, and hugeText.txt in your KryptSafe directory.
3. Run python restore.py and follow the instructions.
4. Wait while the program does its thing.
5. You're done!

## Pros of KryptSafe

- Four is the maximum number of hiding places you need:
  - One for initialIgnore.txt
  - One for cutsList.txt
  - One for hugeText.txt
  - One for your password
- The four items do not have to be in any order.
- To decrypt the mnemonic phrase, someone would need to know the location of all four.
- This is definitely safer than storing the raw mnemonic phrase in a safe.
- This is definitely more reliable than slicing your mnemonic phrase and storing it in different locations (you need to remember the order).

## Cons of KryptSafe

- Phishing: You use a frequently used password to mask your mnemonic and that password got phished. (You still have the three files to keep you safe.)
- Forgetting to go offline: If you keep initialIgnore.txt and cutsList.txt on your main system and go online, there's always the risk that someone can hack your system.
- Hacking: If you have a keylogger or some other malware on your system, I am sorry but KryptSafe will be unable to help you. Operate on a fresh, clean system if you need to.
- Unable to protect against fire and hardware failure: No matter where you store your files, there's always the chance that Murphy's Law kicks into overdrive.

## Disclaimer and Endnotes

Before using KryptSafe, please ensure that you understand what's going on.
If you have any questions, please ping me on the issues tab.

Please feel free to fork this repo and modify stuff. I'm interested to know what you come up with!

And whatever you do, please do not sell this program or any derivative program from this one. That's just bad taste.

DISCLAIMER: I am not responsible for anything that goes wrong with using any of the KryptSafe programs.
