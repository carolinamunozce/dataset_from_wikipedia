#  calcular la suma de todos los numeros comprendidos entre el 0 y el numero natural que quiera el usuario.

def es_primo(numero):
    contador = 0
    if numero == 1:
        return False
    for i in range (2,numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador +=1
    if contador == 0:
        return True
    else:
        return False


def run():
    
   numero = int(input('Escribe un numero : '))
   if es_primo(numero):
       print('Es primo')
   else:
       print('No es primo')

       
if __name__ =='__main__':
    run()

