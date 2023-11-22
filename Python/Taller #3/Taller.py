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

    for i in list_digits:
        for j in list_letters:
            for k in list_specials:
                list_codes.append("COD-" + str(random.sample(list_digits, 3)) + str(random.sample(list_letters, 3)) + str(random.choice(list_specials)))
    
    return list_codes

    

print(count_codes())