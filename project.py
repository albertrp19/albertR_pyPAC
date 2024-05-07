import os
from funcions import *
opcio = 0
diccionari = {}
print(menu)
while opcio != 6:
    os.system('cls')
    menu()
    opcio = int(input("Introdueix una opcio valida: "))
    while opcio > 6 or opcio < 1:
        print("Ha introduit un opcio no valida")
        menu()
        opcio = int(input("Introdueix una opcio valida: "))
    if opcio == 1:
        os.system('cls')
        menu1()
        paraula = input("Introdueix la paraula: ")
        if paraula in diccionari:
            print("La paraula ja esta dins del diccionari")
        else:
            titold = input("Introdueix el titol de l'accepció: ")
            valor = input("Introdueix la accepció: ")
            entrada = {titold:valor}
            diccionari.update({paraula:entrada})
        continuar()
    if opcio == 2:
        os.system('cls')
        menu2()
        mostrar(diccionari)
        paraula = input("Introdueix la paraula a la que vols agregar una accepcio: ")
        if paraula in diccionari:
            titold = input("Introdueix el titol de la nova accepció: ")
            valor = input("Introdueix la accepció: ")
            entrada = {titold:valor}
            aux = diccionari[paraula]
            aux.update(entrada)
            diccionari.update({paraula:aux})
        else:
            print("La paraula no esta dins del diccionari")
        continuar()
    if opcio == 3:
        os.system('cls')
        menu3()
        mostrar(diccionari)
        continuar()
    if opcio == 4:
        os.system('cls')
        menu4()
        print(diccionari)
        paraula = input("Introdueix la paraula que vols modificar: ")
        if paraula in diccionari:
            definicio = diccionari.pop(paraula)
            nParaula = input("Introdueix la nova paraula: ")
            diccionari.update({nParaula:definicio})
            print("La paraula s'ha modificat correctament")
        else:
            print("La paraula no esta dins del diccionari")
        continuar()
    if opcio == 5:
        os.system('cls')
        menu5()
        print(diccionari)
        paraula = input("Introdueix la paraula que vols eliminiar: ")
        if paraula in diccionari:
            diccionari.pop(paraula)
            print("La paraula s'ha eliminat correctament")
        else:
            print("La paraula no esta dins del diccionari")
        continuar()
    if opcio == 6:
        os.system('cls')
        menu6()