lista = []

for i in range(6):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    
    if numeros % 2 == 0:
        print(f'{numeros} é par')
    
    else:
        print('Número é impar')
    
    len(lista)