class Aritmetica:

    def __init__(self,operando1,operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado de la Suma: {resultado}')

    def resta(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado de la Resta: {resultado}')

    def multiplicar (self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado de la Multiplicacion: {resultado}')

    def division (self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado de la Division:{resultado:.2f}')

if __name__ == '__main__':
    while True:
        print(f''' Ingresa la Operacion a Realizar
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir''')

        opcion = int(input(f'Ingresa la Opcion: '))
        if opcion == 5:
            print('Saliendo de la Calculadora. Hasta Luego')
            break

        valor1 = float(input('Ingresa el Valor 1: '))
        valor2 = float(input('Ingresa el Valor 2: '))
        aritmetica1 = Aritmetica(valor1,valor2)

        if opcion == 1:
            aritmetica1.sumar()
        elif opcion == 2:
            aritmetica1.resta()
        elif opcion == 3:
            aritmetica1.multiplicar()
        elif opcion == 4:
            aritmetica1.division()
        else:
            print('Opcion Invalida Intenta de nuevo')
            break
