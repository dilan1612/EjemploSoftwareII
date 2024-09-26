class AFDLongitudParParA:
    def __init__(self):
        self.estado_actual = 'q0'

    def transicion(self, simbolo):
        print(f"Transición desde {self.estado_actual} con símbolo {simbolo}")
        if self.estado_actual == 'q0':
            if simbolo == 'a':
                self.estado_actual = 'q2'
            elif simbolo == 'b':
                self.estado_actual = 'q1'
        elif self.estado_actual == 'q1':
            if simbolo == 'a':
                self.estado_actual = 'q3'
            elif simbolo == 'b':
                self.estado_actual = 'q0'
        elif self.estado_actual == 'q2':
            if simbolo == 'a':
                self.estado_actual = 'q0'
            elif simbolo == 'b':
                self.estado_actual = 'q3'
        elif self.estado_actual == 'q3':
            if simbolo == 'a':
                self.estado_actual = 'q1'
            elif simbolo == 'b':
                self.estado_actual = 'q2'
        print(f"Ahora en {self.estado_actual}")

    def aceptar(self, cadena):
        self.estado_actual = 'q0'
        for simbolo in cadena:
            self.transicion(simbolo)
        return self.estado_actual == 'q0'


afd = AFDLongitudParParA()
cadena = 'abab'
resultado = afd.aceptar(cadena)
print(f"La cadena {cadena} {'es aceptada' if resultado else 'no es aceptada'} por el autómata")
