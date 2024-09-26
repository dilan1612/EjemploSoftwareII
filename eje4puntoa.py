class AFDNoIICon00:
    def __init__(self):
        self.estado_actual = 'q0'

    def transicion(self, simbolo):
        print(f"Transición desde {self.estado_actual} con símbolo {simbolo}")
        if self.estado_actual == 'q0':
            if simbolo == '0':
                self.estado_actual = 'q1'
            elif simbolo == '1':
                self.estado_actual = 'q3'
        elif self.estado_actual == 'q1':
            if simbolo == '0':
                self.estado_actual = 'q2'
            elif simbolo == '1':
                self.estado_actual = 'q3'
        elif self.estado_actual == 'q2':
            
            self.estado_actual = 'q2'
        elif self.estado_actual == 'q3':
            if simbolo == '0':
                self.estado_actual = 'q1'
            elif simbolo == '1':
                self.estado_actual = 'q4'
        print(f"Ahora en {self.estado_actual}")

    def aceptar(self, cadena):
        self.estado_actual = 'q0'
        for simbolo in cadena:
            self.transicion(simbolo)
        return self.estado_actual == 'q2'


afd = AFDNoIICon00()
cadena = '0010'
resultado = afd.aceptar(cadena)
print(f"La cadena {cadena} {'es aceptada' if resultado else 'no es aceptada'} por el autómata")
