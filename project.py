import os
from funcions import *
opcio = 0

while opcio != 4:
    menu()
    opcio = int(input("Introdueix una opcio valida: "))
    while opcio > 4 or opcio < 1:
        os.system('cls')
        print("Ha introduit un opcio no valida")
        menu()
        opcio = int(input("Introdueix una opcio valida: "))
    if opcio == 1:
        os.system('cls')
        menu1()
    if opcio == 2:
        os.system('cls')
        menu2()
    if opcio == 3:
        os.system('cls')
        menu3()
    if opcio == 4:
        os.system('cls')
        menu4()