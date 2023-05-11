#main source for encryption of messages
def encrypt_K(keys):
     
     #it opens the regular message textfile and reads it
     og_F = open('regularM.txt', 'r')
     readog_F = og_F.read()

     #opens the decrypted textfile that the message will appear at
     #creates file if there is none
     en_F = open('decryptM.txt', 'w')

     #reads every letter, character, and symbol in the textfile
     for letters in readog_F:
          
          #find if the letter is visible in the key code and match the corresponding key
          #it writes the vaule in the decryption textfile
          if letters in keys:
               en_F.write(keys[letters])

           #If anything else, have it the same
          else:
               en_F.write(letters)

     #File will close 
     en_F.close()

#main source for decrypting messages
def decrypt_K(keys):
     
     #it opens the decrypted textfile and reads it
     en_F = open('decryptM.txt', 'r')
     rden_F = en_F.read()

     #loop every character in the decrypt textfile
     for letters in rden_F:
          
          #used to check and see if it is in the key code or not then it will print
          #then it will print ' ' or '.' if 
          if not letters in keys.values() or letters == '.' or letters == ' ':
              print(letters, end='')

          #gives the else command to print key that matches the letter
          else:
               for t, que in keys.items():
                    if letters == que:
                         print(t, end='')


             
     
#main source for the output code
def ende ():

    #the alphabet is assigned a different key code from encryption and decryption
    keys = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'~', 'c':'`', 'D':'!', 'd':'1', \
             'E':'2', 'e':'3', 'F':'$', 'f':'4', 'G':'5', 'g':'^', 'H':'6', 'h':'7', \
             'I':'&', 'i':'*','J':'8', 'j':'(', 'K':'9', 'k':')', 'L':'0', 'l':'-', \
             'M':'_', 'm':'=', 'N':'+', 'n':'|', 'O':'/', 'o':'?', 'P':'[', 'p':'}', \
             'Q':'{', 'q':']', 'R':',', 'r':'<', 'S':'.', 's':'>', 'T':'"', 't':':', \
             'U':'o', 'u':'K', 'V':'e', 'v':'s', 'W':'m', 'w':'Q', 'X':'D', 'x':'A', \
             'Y':'p', 'y':'X', 'Z':'F', 'z':'j'
}
    
    #use to encrypt the alphabet in the message
    encrypt_K(keys)
    
    
    #use to decrypt the alphabet in the message
    decrypt_K(keys)

    

    ende()



