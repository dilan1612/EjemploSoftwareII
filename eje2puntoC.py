class AFDImparAB:
    def __init__(self):
        self.estado_actual = 'q0' 

    def transicion(self, simbolo):
        print(f"Transición desde {self.estado_actual} con símbolo {simbolo}")
        if self.estado_actual == 'q0':
            if simbolo == 'a':
                self.estado_actual = 'q2'
        elif self.estado_actual == 'q1':
            if simbolo == 'a':
                self.estado_actual = 'q2'
        elif self.estado_actual == 'q2':
            if simbolo == 'b':
               
                self.estado_actual = 'q1' if self.estado_actual == 'q0' else 'q0'
            elif simbolo == 'a':
                
                self.estado_actual = 'q2'
        print(f"Ahora en {self.estado_actual}")

    def aceptar(self, cadena):
        
        self.estado_actual = 'q0'
        for simbolo in cadena:
            self.transicion(simbolo)
        
        return self.estado_actual == 'q1'


afd = AFDImparAB()
cadena = 'aababb'  
resultado = afd.aceptar(cadena)
print(f"La cadena {cadena} {'es aceptada' if resultado else 'no es aceptada'} por el autómata")
