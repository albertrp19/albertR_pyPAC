diccionari = {}

print(diccionari)

paraula = "xarxa"
entrada = {
  "PESCA" : "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal."}

diccionari.update({paraula:entrada})

print(diccionari)

auxiliar = diccionari[paraula]

print(auxiliar)

entrada = {
  "TÈXTIL" : "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà."}
  
auxiliar.update(entrada)

print(auxiliar)

diccionari.update({paraula:auxiliar})

print(diccionari)