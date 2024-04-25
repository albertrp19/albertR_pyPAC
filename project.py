import os
from funcions import *
opcio = 0

while opcio != 5:
    os.system('cls')
    menu()
    opcio = int(input("Introdueix una opcio valida: "))
    while opcio > 5 or opcio < 1:
        print("Ha introduit un opcio no valida")
        menu()
        opcio = int(input("Introdueix una opcio valida: "))
    if opcio == 1:
        os.system('cls')
        menu1()
        continuar()
    if opcio == 2:
        os.system('cls')
        menu2()
        continuar()
    if opcio == 3:
        os.system('cls')
        menu3()
        continuar()
    if opcio == 4:
        os.system('cls')
        menu4()
        continuar()
    if opcio == 5:
        os.system('cls')
        menu5()