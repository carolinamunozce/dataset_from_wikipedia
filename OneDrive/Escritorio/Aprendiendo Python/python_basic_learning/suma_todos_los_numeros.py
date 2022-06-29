#  calcular la suma de todos los numeros comprendidos entre el 0 y el numero natural que quiera el usuario.

def run():
    i = 0
    sumar = 0
    
    numero = int(input('Ingrese un número : '))
    while i < numero:
        if i % 2 == 0:
            if i == 6:
                sumar = sumar + i
                break
        i= i + 1
        continue
    return sumar
total = run()
print (total)

# if __name__ =='__main__':
#     run()

