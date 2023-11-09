"""1. Deberá crear una función de orden superior que devuelva todos los números primos desde el 2
hasta un numero que se entregue como parámetro, esta función deberá utilizar filter dentro de su implementación."""


def primer_punto(num_final):
    
    lista_nums = range(2, num_final + 1)

    print(list(filter(lambda elemento: elemento in lista_nums, list(lista_nums))))
    

primer_punto(50)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""2. Deberá realizar una función que encuentre los números primos hasta un numero dado
 (básicamente repetir el ejercicio anterior), pero usando el generador Yield en su implementación.













///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

3.Programar Fibonacci Simple y Fibonacci Recursivo Cola comparando los tiempos de ejecución y analizar la ganancia en tiempo."""