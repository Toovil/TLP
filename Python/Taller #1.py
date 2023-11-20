"""1. Deberá crear una función de orden superior que devuelva todos los números primos desde el 2
hasta un numero que se entregue como parámetro, esta función deberá utilizar filter dentro de su implementación."""


def es_primo(num1):
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True

<<<<<<< HEAD
    print(list(filter(lambda elemento: elemento % elemento + 1, list(lista_nums))))
    

primer_punto(50)
=======
def encontrar_primos(max1):
    return list(filter(es_primo, range(2, max1 + 1)))
>>>>>>> 2ff952675b42c76729b3f5521bf94af8e66db8e6

print(encontrar_primos(50))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""2. Deberá realizar una función que encuentre los números primos hasta un numero dado
 (básicamente repetir el ejercicio anterior), pero usando el generador Yield en su implementación."""

def es_primo2(num2):
    for i in range(2, num2):
        if num2 % i == 0:
            return False
    return True

def encontrar_primos2(max2):
    for num2 in range(2, max2 + 1):
        if es_primo(num2):
            yield num2

print(list(encontrar_primos2(50)))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""3.Programar Fibonacci Simple y Fibonacci Recursivo Cola comparando los tiempos de ejecución y analizar la ganancia en tiempo."""

import time

def fibonacci_simple(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def fibonacci_recursivo(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fibonacci_recursivo(n - 1, b, a + b)


n = 800  

inicio_simple = time.time()
resultado_simple = fibonacci_simple(n)
fin_simple = time.time()
tiempo_simple = fin_simple - inicio_simple

inicio_recursivo_cola = time.time()
resultado_recursivo_cola = fibonacci_recursivo(n)
fin_recursivo_cola = time.time()
tiempo_recursivo_cola = fin_recursivo_cola - inicio_recursivo_cola

print(f"Fibonacci Simple({n}): {resultado_simple}")
print(f"Tiempo de ejecución (Fibonacci Simple): {tiempo_simple} segundos\n")

print(f"Fibonacci Recursivo Cola({n}): {resultado_recursivo_cola}")
print(f"Tiempo de ejecución (Fibonacci Recursivo Cola): {tiempo_recursivo_cola} segundos")

