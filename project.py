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

opcio = 0

while opcio != 4:
    menu()
    opcio = int(input("Introdueix una opcio valida: "))
    while opcio > 4 or opcio < 1:
        os.system('cls')
        print("Ha introduit un opcio no valida")
        menu()
        opcio = int(input("Introdueix una opcio valida: "))