"""1. (1.0) Una empresa busca generar códigos únicos para sus productos
utilizando letras, dígitos y caracteres especiales dadas las siguientes
restricciones:
• Letras: P, Q, R, W, X , Y, Z
• Dígitos: 9, 8, 7, 6, 5
• Especiales: _, #, &, %
Los códigos generados constan de: palabra “COD-” seguido de 3 dígitos,
3 letras y 1 carácter especial
ej: COD-563ZXZ&. Encuentre todos los posibles códigos y retorna el tamaño de la 
lista.
"""

import random

def count_codes():
    list_letters = ["P", "Q", "R", "W", "X" , "Y", "Z"]
    list_digits = [9, 8, 7, 6, 5]
    list_specials = ["_", "#", "&", "%"]

    list_codes = []

    for letters in list_digits:
        for digits in list_letters:
            for specials in list_specials:
                list_codes.append("COD-" + str(random.sample(list_digits, 3)) + str(random.sample(list_letters, 3)) + str(random.choice(list_specials)))
    return " ".join(list_codes) + "\n\n" + str(len(list_codes)) # Da un tamaño de lista de 140, está mal.

#Machetazo:

""" Queremos formar combinaciones de codigos con 3 letras: 7 objetos (7**3), 3 digitos: 5 objetos (5**3) y un especial: 4 objetos (4**1).

    Si hacemos combinatoria, la lista tendría que tener (7**3) + (5**3) + (4**1) = 472 elementos
    """

    

print(count_codes())