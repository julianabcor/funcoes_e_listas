lista = []

for i in range(4):
    notas = int(input('Digite sua nota: '))
    lista.append(notas)
print(f'Suas notas são: {lista}')
media = sum(lista) / 4
print(f'Sua média é: {media}')