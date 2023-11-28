import pandas as pd
import unittest
from itertools import product as p

# //// Punto #1
print("#" * 25, "Punto #1")

digitos = ['9', '8', '7', '6', '5']
letras = ['P', 'Q', 'R', 'W', 'X', 'Y', 'Z']
especiales = ['_', '#', '&', '%']


def generar_codigos():

    codigos = []

    # permutaciones por grupo
    digitos_perm = p(digitos, repeat=3)
    letras_perm = p(letras, repeat=3)
    especiales_perm = p(especiales, repeat=1)

    # cada "item" de los tres abajo, representa una tupla
    # de los "k" seleccionados en las permutaciones
    for digito3, letra3, especial1 in p(digitos_perm, letras_perm,
                                        especiales_perm):
        codigos.append("COD-" + "".join(digito3 + letra3 + especial1))

    return codigos


lista_codigos = generar_codigos()

#Descomente esta linea si quiere que su terminal se llene de TODAS las combinaciones de códigos
# for c in lista_codigos: print(c)

print(
    "Descomente la linea 36 si quiere que su terminal se llene de TODAS las combinaciones de códigos."
)
print(f"La cantidad de códigos posibles es de: {len(lista_codigos)}")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# //// Punto #2
print("\n" + "#" * 25, "Punto #2")


class Personaje:

    def __init__(self):
        self.vida = 100
        self.monedas = 0
        self.diamantes = 0

    def verificar_vida_bonus(self) -> None:
        bonus_vida = self.monedas // 10
        self.vida += bonus_vida

    def agregar_monedas(self, cantidad) -> None:
        self.monedas += cantidad
        self.verificar_vida_bonus()

    def reducir_vida(self, cantidad) -> None:
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def alcanzar_diamante(self) -> bool:
        c = self.monedas >= 200 and self.monedas % 200 == 0
        if c:
            self.diamantes = self.monedas % 200

        return c

    def estado(self) -> dict:
        return {
            "vida": self.vida,
            "monedas": self.monedas,
            "diamantes": self.diamantes
        }


class TestPersonaje(unittest.TestCase):

    def setUp(self):
        self.p = Personaje()

    def test_creacion_personaje(self):
        self.assertEqual(self.p.vida, 100)
        self.assertEqual(self.p.monedas, 0)

    def test_agregar_monedas(self):
        self.p.agregar_monedas(20)
        self.assertEqual(self.p.monedas, 20)
        self.assertEqual(self.p.vida,
                         102)  # 20 monedas/10 = 2 de bonus de vida

    def test_perder_vida(self):
        self.p.reducir_vida(30)
        self.assertEqual(self.p.vida, 70)

    def test_alcanzar_diamante(self):
        self.assertFalse(self.p.alcanzar_diamante())
        self.p.agregar_monedas(200)
        self.assertTrue(self.p.alcanzar_diamante())

    def test_esta_vivo(self):
        self.assertTrue(self.p.esta_vivo())
        self.p.reducir_vida(100)
        self.assertFalse(self.p.esta_vivo())

    def test_estado(self):
        estado = self.p.estado()
        self.assertEqual(estado['vida'], 100)
        self.assertEqual(estado['monedas'], 0)
        self.assertEqual(estado['diamantes'], 0)




#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# //// Punto #3
print("\n" + "#" * 25, "Punto #3")

# asegurese de tener el archivo en 'properties.csv' en este directorio
data_ = pd.read_csv(r"C:\Users\Juan Tobon\Desktop\TLP\Python\Taller #3\properties.csv")

# ///////////////// (1)
print("1)\n")

data_['Price'] = data_['Price'] // 83
print(f"{data_}\n\n")

# ///////////////// (2)
print("\n\n2)\n")

#Encuentre los apartamentos que se encuentran disponibles (Ready to move o Immediately),posteriormente indique la media de precios de estos.

print(data_[data_['Possession Status'] == "Ready to Move"])

print(
    f"La media de precios de los aptos disponibles es: {round(data_[data_['Possession Status'] == 'Ready to Move']['Price'].mean())}"
)

# ///////////////// (3)
print("\n\n3)\n")

#Encuentre el número que inmuebles que se encuentran en el primer piso.

counter_first = 0
for i in data_['Floor No'].dropna():
    if i == "1":
        counter_first += 1

print(f"La cantidad de inmuebles en el primer piso es: {counter_first}")

# ///////////////// (4)
print("\n\n4)\n")

#Encuentre cual es el Developer que más edificios ha realizado.

print(data_['Developer'].value_counts().head(1))

# ///////////////// (5)
print("\n\n5)\n")

#Encuentre la cantidad de casas que se encuentran disponibles en general (Units Available).

counter_casas = 0

for i in data_["Units Available"].dropna():
    counter_casas += int(i)

print(
    f"La cantidad de casas que se encuentran disponibles en general es: {counter_casas}"
)

# ///////////////// (6)
print("\n\n6)\n")

#Muestre en un dataframe todos los locales comerciales.

print(data_[data_['Commercial'] == "Y"])

# ///////////////// (7)
print("\n\n7)\n")

#Indique cual es el inmueble más costoso y el más barato (Price).

print(f"El inmueble más costoso es: {data_['Price'].max()}")

print(f"El inmueble más barato es: {data_['Price'].min()}")

# ///////////////// (8)
print("\n\n8)\n")

#Encuentre los inmuebles que se encuentren siendo construidos por kalpataru Ltd.

print(data_[data_['Developer'] == "Kalpataru Ltd."])

unittest.main()