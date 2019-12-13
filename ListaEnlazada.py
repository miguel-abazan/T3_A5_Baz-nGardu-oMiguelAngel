from  Nodo import Nodo

class ListaEnlazada:

    def __init__(self):
        self.nodoInicio = None
        self.nodoFin = None

    def agregarInicio(self, dato):
        nn = Nodo(dato)
        if (self.vacia() == True):
            self.nodoInicio = self.nodoFin = nn
        else:
            nn.enlace = self.nodoInicio
            self.nodoInicio = nn

    def vacia(self):
        if self.nodoInicio == None:
            return True


    def mostrarPromedio(self, lista):
        promedio = 0
        contador = 0
        nodoActual = lista.nodoInicio

        while nodoActual != None:
            promedio = promedio + nodoActual.dato
            nodoActual = nodoActual.enlace
            contador = contador + 1
        promedio = promedio / contador
        cadena = ""
        if promedio < 10:
            cadena = "Congelacion"
        elif promedio <= 20:
            cadena = "Frio"
        elif promedio < 30:
            cadena = "Normal"
        else:
            cadena = "Alta"

        return str(str(promedio) +" " + cadena)

l = ListaEnlazada()
l.agregarInicio(1)