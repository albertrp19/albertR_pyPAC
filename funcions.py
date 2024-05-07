def menu():
    """Aquesta funcio serveix per mostrar el menu principal"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  BENVINGUTS AL LLIBRE DE LES ACCEPCIONS DE L'ALBERT RODIGUEZ  ║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print("║                                                               ║")
    print("║  1).   Afegir paraula i accepció                              ║")
    print("║  2).   Afegir accepcio                                        ║")
    print("║  3).   Mostrar paraula i accepcions                           ║")
    print("║  4).   Modificar paraula                                      ║")
    print("║  5).   Eliminar paraula o accepció                            ║")
    print("║  6).   Sortir                                                 ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

def menu1():
    """Aquesta funcio serveix per mostrar la capçalera del menu per afegir paraules i accepcions"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                   Afegir paraula i accepció                   ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

def menu2():
    """Aquesta funcio serveix per mostrar la capçalera del menu per afegir accepcio"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                        Afegir accepció                        ║")
    print("╚═══════════════════════════════════════════════════════════════╝")


def menu3():
    """Aquesta funcio serveix per mostrar la capçalera del menu per mostrar paraules i accepcions"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                 Mostrar paraula i accepcions                  ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

def menu4():
    """Aquesta funcio serveix per mostrar la capçalera del menu modificar paraules o accepcions"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                       Modificar paraula                       ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
 
def menu5():
    """Aquesta funcio serveix per mostrar la capçalera del menu eliminar paraules i accepcions"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                  Eliminar paraula i accepció                  ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

def menu6():
    ""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                            Sortir                             ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("Adeu, que tinguis un bon dia")

def continuar():
    input("Pressiona qualsevol tecla per continuar...")

def mostrar(diccionari):
    diccionari_str = "\n".join(f"{k}: {v}\n" for k, v in diccionari.items())
    print(diccionari_str)