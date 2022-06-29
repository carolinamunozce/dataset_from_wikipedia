#Adivinar el número al azar
import random()

def run():
    numero_aleatorio = random.randonint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un número mas pequeño')
            numero_elegido = int(input('Elige otro número: '))
            
    print('Ganaste!!!')

# Entry point
       
if __name__ =='__main__':
    run()

