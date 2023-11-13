object Main{
    
    def main(args: Array[String]): Unit ={
        
        //Primer Ejercicio
    
        /*Utilizando la funcion map cree a partir de una lista de caracteres otra lista que 
        convierta cada uno de los caracteres en una lista que contenga su version en mayuscula 
        y en minuscula.
        Ejemplo:
        Input: List('a','B','c')
        Output: List(List(A, a), List(B, b), List(C, c))*/
        
        def convertirMayusculaMinuscula(caracter: Char): List[Char] = {
            List(caracter.toUpper, caracter.toLower)
        }

        def convertirListaCaracteres(lista: List[Char]): List[List[Char]] = {
            lista.map(convertirMayusculaMinuscula)
        }
        
        val listaCaracteres = List('a', 'b', 'c')
        val resultado1 = convertirListaCaracteres(listaCaracteres)
        println(resultado1)
    
    
    
        //Segundo Ejercicio
        
        /*  Utilizando la funcion filter se debera eliminar de una lista que contiene nombres 
            Aquellos que tengan menos de 6 letras o inicien por cualquier letra que sea distinta 
            a la A 
            Ejemplo:
            Input: List("Andres David","Camilo","Juan")
            Output: List(Andres David)*/
    
        var lista2 = List("Andres David","Camilo","Juan")
        println(lista2.filter((i:String) => i.startsWith("A") || List(i).length > 6 ))
        
        
    
        //Tercer Ejercicio
        
        /*Dado una lista que contiene caracteres utilizando foreach 
        se debera imprimir true si es que el caracter corresponde a una vocal.
        Ejemplo: 
        Input: List("a","b","e","f")
        output: "a"
              "e" */
              
        var lista3 = List("a","b","e","f")
        
        lista3.foreach((i:String) => {
            if (i == "a" || i == "e" || i == "i" || i == "o" || i == "u"){
                println(i)
            } 
        })
    
    
        //Cuarto Ejercicio
        
        /*A partir de una lista que contiene números enteros, se deberá realizar el
        siguiente procedimiento utilizando recursividad, 
        si el elemento es impar debera multiplicarse por 2, 
        en caso contrario se dejara el numero tal cual, posteriormente se debera 
        reorganizar la lista de manera descendente sin tener repeticiones.
        
        Ejemplo:
        input: List(1,2,3,4,5,6,7)
        Output: List(14,10,6,4,2) */
        def procesarLista(lista: List[Int]): List[Int] = {
            lista match {
                case Nil => Nil 
                case head :: tail => {
                val nuevoElemento = if (head % 2 != 0) head * 2 else head
                nuevoElemento :: procesarLista(tail)
                }
            }
        }

        def reorganizarDescendente(lista: List[Int]): List[Int] = {
            lista match {
            case Nil => Nil 
            case _ => {
                val maximo = lista.max 
                val listaSinRepetir = lista.filter(_ != maximo) 
                maximo :: reorganizarDescendente(listaSinRepetir) 
            }
        }     
        }

        def procesarYReorganizar(lista: List[Int]): List[Int] = {
            val listaProcesada = procesarLista(lista)
            val listaReorganizada = reorganizarDescendente(listaProcesada)
            listaReorganizada
        }
        
        val lista = List(1, 2, 3, 4, 5, 6, 7)
        val resultado = procesarYReorganizar(lista)
        println(resultado)

    }
    
}
