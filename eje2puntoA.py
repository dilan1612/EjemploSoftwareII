class AFDParDeAs:
    def __init__(self):
        self.estado_actual = 'q0'  

    def transicion(self, simbolo):
        print(f"Transición desde {self.estado_actual} con símbolo {simbolo}")
        if self.estado_actual == 'q0':
            if simbolo == 'a':
                self.estado_actual = 'q1'
        elif self.estado_actual == 'q1':
            if simbolo == 'a':
                self.estado_actual = 'q0'
     
        print(f"Ahora en {self.estado_actual}")

    def aceptar(self, cadena):
        
        self.estado_actual = 'q0'
        for simbolo in cadena:
            self.transicion(simbolo)
      
        return self.estado_actual == 'q0'


afd = AFDParDeAs()
cadena = 'abba'  
resultado = afd.aceptar(cadena)
print(f"La cadena {cadena} {'es aceptada' if resultado else 'no es aceptada'} por el autómata")
