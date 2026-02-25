lista = []

for i in range(5):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    soma = sum(lista)
print(f'Seus números são: {numeros}')
print(f'A soma de seus números são: {soma}')
