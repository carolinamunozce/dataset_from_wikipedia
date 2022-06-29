pesos = input("Cuantos pesos chilenos tiene: ")
pesos = float(pesos)
valor_dolar = 792.61
dolares = pesos / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print ('Tienes $ ' + dolares + ' dolares')