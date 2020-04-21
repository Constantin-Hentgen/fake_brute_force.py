import time
import os

print("Welcome in the brute force software")
print("Do you want to know how much time i need to crack your password ?  ")
game = input("Enter 'yes' or 'no' : ")

while game == "yes":
    password = input("Enter a password : ")
    start_time = time.time()
    alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ€(ù)²Ë !\"#$%&'-,¨./:;<½Òú∟øô>=?@\\[¤]^_`}{|+-/›ß~^ˆ*‰‹‘‘“•–—˜¡¢£¥§©¬®°µ¶¿ÀÁÂÃÆÇÈÉÊÌÍÎÏÑàáâãäåæçèéêëñÄÅ"
    hack = ""
    k=0
    i=0
    while hack != password:
        if password[k] != alpha[i]:
            i += 1
        else: 
            hack = hack + alpha[i]
            i = 0
            k += 1
            print(hack)
    print(time.time() - start_time, "seconds")
    game = input("Do you want to test an other password? ")

os.system('Pause')
