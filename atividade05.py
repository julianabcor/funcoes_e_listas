lista = ['morango', 'banana', 'uva', 'melancia', 'abacate', 'lichia']
print(lista)
frutas = str(input(f'Escolha uma das frutas para remover: {lista}'))
lista.remove(frutas)
print(lista)