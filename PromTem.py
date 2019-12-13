class Temperatura:
    def __init__(self, temperatura, fecha):
        self.temperatura = temperatura
        self.fecha = fecha

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


    def mostrarPromedio(self, lista, fecha):
        promedio = 0
        contador = 0
        nodoActual = lista.nodoInicio

        while nodoActual != None:
            if nodoActual.dato.fecha == fecha:

                promedio = promedio + nodoActual.dato.temperatura
                contador = contador + 1
            nodoActual = nodoActual.enlace

        promedio = promedio / contador
        cadena = ""
        if promedio < 10:
            cadena = "Congelación"
        elif promedio <= 20:
            cadena = "Frio"
        elif promedio < 30:
            cadena = "Normal"
        else:
            cadena = "Alta"

        return str(str(promedio) +" " + cadena)

class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.enlace = None

    def getDato(self):
        return self.dato
    def setDato(self, dato):
        self.dato = dato
        pass
    def getEnlace(self):
        return self.enlace

    def setEnlace(self, enlace):
        self.enlace = enlace
        pass

    def __str__(self) -> str:
        return f"[ {self.dato} , {self.enlace}]"


t1 = Temperatura(25, "2001")
t2 = Temperatura(32, "2006")
t3 = Temperatura(-6, "2001")

l1 = ListaEnlazada()
l1.agregarInicio(t1)
l1.agregarInicio(t2)
l1.agregarInicio(t3)

print(l1.mostrarPromedio(l1,"2001"))