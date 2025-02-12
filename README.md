# SSS_Phrase_Encryption
Please read this document carefully to understand its purpose.

A single main script to perform Shamir Secret Sharing algorithm on seed phrases based by default on the BIP-39 mnemonic words generator.

The Shamir Secret Sharing Algorithm is known for being a good and reliable way of protecting secret codes. It works by first defining a polynomial function of degree N-1 where N is the user-defined number of shares that will be needed to reconstruct the original secret. It then generates large numbers using this polynomial function in pairs as (x, f(x)) each pair is a "Share" and the user can generate as many as they like. Gathering any N of them no matter the order will allow the person to recover the original sharded secret. Think of it as Voldemort splitting his soul in Horocruxes and if and only if you gather N of them you can reconstruct the secret. 

The script is written as a single file to show transparency in the code as it purely executes the mathematical functions to perform the SSS algorithm and some extras to make it a little bit user friendly by accepting user inputs from the terminal.

# How this script works (briefly explained):
You might be wondering how can you turn a 24-word phrase into a number to encrypt, because yes, SSS algo encrypts numbers. The idea is simple, when you enter the words one by one the script turns them into indexes of the word list, that way a word, no matter how large it is it will always be represented by a number between 1 and 2048. Then all this numbers are concatenated into a giant integer number that is later one used as the encryption secret. Reason why this program also accounts for the option to simply convert your words into this indexes [1-2048] which you can later feed into the option to encrypt number to shares using SSS. Meaning you can take your seedphrase in the order you want and in the pieces you want and convert them one by one with the script into indexes, and then manually enter the concatenated number into the SSS algorithm. Do as you please. 

The script will ask you to firstly indicate how many shares in TOTAL you want to produce, this is the TOTAL number of shares. It then will ask you for the number of needed shares to reconstruct your secret, no need to indicate that the latter should be smaller than the former. 

Saved the received shares IN PAIRS, as if you need to reconstruct your secret you will be asked to input each share as the pair (x and f(x)), note that even if you make the smalles mistake and instead of a 1 you wrote 7 in the least significant digit of the share the recovered seed phrase will be NO CLOSE to the initial one so be careful when saving the shares.

# Advices and further information

I strongly recommend you simply download or copy paste both files to your local PC, the "english.txt" and the "main.py" and execute them on your PC offline to further enhance your security. I of course take no responsibility for having your seed phrase stolen to a virus in your PC listening to yout inputs in the keyboard despite you followed my advice to execute it offline.

I also strongly recommend you first play with the script with random words from the list as if they were a seed phrase and see how the encryption and then recovering works.

This script does not require internet to work, only python and the python package "sympy" which you can easily install by doing: "pip install sympy" this package is used only for two methods mod_inverse and nextprime. These two methods are used to generate primer numbers used in the encryption algorithm and to calculate the mod inverse operator used also in the algorithm. 

Then you would simply need to run a classic "python main.py" and see the magic work. If you for some reason did not use the BIP-39 mnemonic as the generator for your seed phrase (most of popular BTC wallets do, like Trezor, Metamask on the other hand uses the BIP-44 which you can solve by downloading the file yourself and naming it english.txt and then running the program as explained. It is well suited to handle 12-word seed phrases and 24-word seed-phrases.
