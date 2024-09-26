class AFDUnosConsecutivos:
    def __init__(self):
        self.estado_actual = 'q0' 

    def transicion(self, simbolo):
        print(f"Transición desde {self.estado_actual} con símbolo {simbolo}")
        if self.estado_actual == 'q0':
            if simbolo == '1':
                self.estado_actual = 'q1'
        elif self.estado_actual == 'q1':
            if simbolo == '1':
                self.estado_actual = 'q2'
            elif simbolo == '0':
                self.estado_actual = 'q0'
        elif self.estado_actual == 'q2':
            if simbolo == '1':
                self.estado_actual = 'q3' 
            elif simbolo == '0':
                self.estado_actual = 'q0'
        elif self.estado_actual == 'q3':
            
            pass
        print(f"Ahora en {self.estado_actual}")

    def aceptar(self, cadena):
       
        self.estado_actual = 'q0'
        for simbolo in cadena:
            self.transicion(simbolo)
        
        return self.estado_actual in ['q0', 'q1', 'q2']


afd = AFDUnosConsecutivos()
cadena = '1010'  
resultado = afd.aceptar(cadena)
print(f"La cadena {cadena} {'es aceptada' if resultado else 'no es aceptada'} por el autómata")
