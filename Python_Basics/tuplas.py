people: tuple = ('Mario', 'Augusto', 'Valentim')

people_list: list[str] = list(people)
people_tuple: tuple = tuple(people_list)

print('Mario' in people)

print(people_tuple)

print(people.count('Mario')) ## contar quantas vezes esse nome aparece na tupla

print(people.index('Valentim')) ## mostrar a posicao do nome