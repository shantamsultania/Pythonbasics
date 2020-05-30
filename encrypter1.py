from pycipher import Vigenere

encipher = Vigenere('PASS').encipher("Shantam")
print("the enciphered text is ",encipher)
decipher = Vigenere("PASS").decipher(encipher)
print("the deciphered text is ",decipher)
