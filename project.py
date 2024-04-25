import os

def menu():
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  BENVINGUTS AL LLIBRE DE LES ACCEPCIONS DE L'ALBERT RODIGUEZ  ║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print("║                                                               ║")
    print("║  1).   Afegir paraula i accepció                              ║")
    print("║  2).   Mostrar paraula i accepcions                           ║")
    print("║  3).   Eliminar paraula i accepció                            ║")
    print("║  4).   Sortir                                                 ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

def menu1():
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                   Afegir paraula i accepció                   ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
        
def menu2():
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                 Mostrar paraula i accepcions                  ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    
def menu3():
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                  Eliminar paraula i accepció                  ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

def menu4():
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                            Sortir                             ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("Adeu, que tinguis un bon dia")
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