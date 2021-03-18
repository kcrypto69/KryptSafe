# CryptSafe

Welcome to the CryptSafe Repository, I am glad to see you here!

You want a better way to store your crypto wallet mnemonic phrase?
Well, here it is. I got your back!

## Existing solutions for storing mnemonic phrases (and why they aren't that good)
  - Writing the phrase it down and storing it in a safe at home (robbery, fire, toss out into the trash by accident)
  - Writing the phrase down and storing it in a bank safety deposit box (robbery (Money Heist style), fire, flood, hassle to retrieve, not necessarily insured by the bank)
  - Slicing and dicing the phrase and storing bits of it in different locations (forgetting the order, forgetting one of the locations, fire, robbery)
  - Laser-engraved the phrase into metal and storing it somewhere (expensive, oxidation, robbery, fire, toss out into the trash by accident)
  - Sharing the phrase among other people (not your keys not your crypto, possible misappropriation, plus a lot of the above mishaps)

## What is CryptSafe, how does it work (and why it's better)?

CryptSafe is similar to existing mnemonic storage solutions in that you still have to store files, either on paper or in a hard-drive. Also, CryptSafe is similar to wallets in that you MUST have your password on hand or else you're done for.

However, what you'll be storing isn't the raw mnemonic (which is really bad btw), but rather some files that serve as substitutes. You can also store your password on another piece of paper and hard-drive. Additionally, you'll be posting a huge list of words in a public repository on a fake Github account that camouflages your mnemonic. If a would-be attacker cannot get hold of every single piece of information, you are safe.

### Preparation
At this point, I am assuming that you have the latest version of Python installed. If not, please go do that!

Install "progress" package: pip install progress

### Generating the encryption files
1. Clone this repository on your local system and cd into it.
2. DISCONNECT your computer from the internet.
3. Run python generate.py and follow the instructions.
4. After that's done, you will now find some files in your current directory, namely initialIgnore.txt, cutsList.txt, and hugeText.txt.
5. IMPORTANT: CHECK IF EVERYTHING WENT WELL by running python restore.py and following the instructions.
6. Record your password and store it somewhere.
7. At this point, you MUST decide your desired level of security. Depending on this, you should transfer (NOT COPY) either/both initialIgnore.txt and cutsList.txt to another offline machine. Alternatively, you can write it down and subsequently delete the file(s) from the current directory. Please see the Complexity Example tab for more information.
8. If all is well, reconnect your computer to the internet.
9. Create a fake Github account and push everything in the currently directory. Make sure the new repo is public.
10. Record your fake Github's username and store it somewhere.
11. You're done!

### Obtaining your Mnemonic phrase
1. For added safety, DISCONNECT from the internet.
2. Please ensure that you have initialIgnore.txt, cutsList.txt, and hugeText.txt in your cryptsafe directory.
3. Run python restore.py and follow the instructions.
4. Wait while the program does its thing.
5. You're done!

## Complexity Example

Complexity goes as follows:

Initial Ignore: 40000
Cuts List : 40000 ^ [Mnemonic Phrase Length]
Password (assuming you're not using common dictionary word) : 94! / (94! - [Mnemonic Phrase Length]!)

For example, assuming mnemonic phrase length of 12:
1. Hide password (Please pick a solid password I beg you): 2.287 * 10^23 permutations
2. Hide password and initial ignore number: 9.150 * 10^27 permutations
3. Hide password, initial ignore number, and cuts list: 1.535 * 10^83 permutations

## Pros of CryptSafe
  - Four is the maximum number of hiding places you need:
    * One for initialIgnore.txt
    * One for cutsList.txt
    * One for your password
    * One for your fake Github username (hugeText.txt is in a public repo)
  - The four items do not have to be in any order.
  - To decrypt the mnemonic phrase, someone would need to know the location of all four.
  - This is definitely safer than storing the raw mnemonic phrase in a safe.
  - This is definitely more reliable than slicing your mnemonic phrase and storing it in different locations (you need to remember the order).

## Cons of CryptSafe
  - Phishing: You use a frequently used password to mask your mnemonic and that password got phished. (You still have barriers to keep you safe.)
  - Forgetting to go offline: If you keep initialIgnore.txt and cutsList.txt on your main system and go online, there's always the risk that someone can hack your system.
  - Hacking: If you have a keylogger or some other malware on your system, I am sorry but CryptSafe will be unable to help you. Operate on a fresh, clean system if you need to.
  - Unable to protect against fire and hardware failure: No matter where you store your files, there's always the chance that Murphy's Law kicks into overdrive.

## Disclaimer and Endnotes
Before using CryptSafe, please ensure that you understand what's going on.
If you have any questions, please ping me on the issues tab.

Please feel free to fork this repo and modify stuff. I'm interested to know what you come up with!

And whatever you do, please do not sell this program or any derivative program from this one. That's just bad taste.

DISCLAIMER: I am not responsible for anything that goes wrong with using my program.
