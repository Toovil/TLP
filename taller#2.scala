object Main extends App{
  def separarAutomoviles(placas: List[String]): List[String] = {
    val patronAutomovil = """^[A-Z]{3}\s\d{3}$""".r
    placas.filter(patronAutomovil.matches)
  }

  def separarVehiculosCarga(placas: List[String]): List[String] = {
    val patronVehiculoCarga = """^\d{3}\s[A-Z]$""".r
    placas.filter(patronVehiculoCarga.matches)
  }

  def separarMotos(placas: List[String]): List[String] = {
    val patronMoto = """^[A-Z]{4,5}\d{3}$""".r
    placas.filter(patronMoto.matches)
  }

  val listaPlacas = List("XNF 400", "JFKE231", "324 E", "FJF 434")

  val automoviles = separarAutomoviles(listaPlacas)
  println(automoviles)

  val vehiculosCarga = separarVehiculosCarga(listaPlacas)
  println(vehiculosCarga)

  val motos = separarMotos(listaPlacas)
  println(motos)
  
}
