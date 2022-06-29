def palindromo(palabra):
    palabra = palabra.replace(' ', '') #Reemplaza los caracteres vacios para hacer una sola palabra
    palabra = palabra.lower()          # Pasa todos los caracteres a minusculas o mayusculas
    palabra_invertida = palabra[::-1]  # Toma la palabra y la invierte
    if palabra == palabra_invertida:   # Compara la palabra y lo invertido para saber si son iguales
        return True
    else:
        return False


def run():
    palabra = input ('Escribe una palabra : ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print ('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()