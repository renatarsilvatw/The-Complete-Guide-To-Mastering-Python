##List
people: list[str] = ['Mario', 'Luigi', 'Peach']
print(len(people)) ##saber o tamanho da lista

print(people[0:3]) ##traz quem estao nessas posicoes

people[0] = 'Leonard' ##replace the first position tb pode ser -> people[0] = ['Leonard', 'Lucas']
print(people)

## Para concatenar duas listas:

people1: list[str] = ['Mario', 'Luigi', 'Peach']
people2: list[str] = ['Pedro', 'Gustavo', 'Maria']

people1 += people2

people1.insert(2, 'Heloisa') ##add em um lugar especifico

people1.append('José') # add no final da lista

people1.remove('Mario') # remove elemento da lista

people1.pop(2)

print(people1)