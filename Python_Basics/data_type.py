from random import randrange

#this is a comment
greeting = "Hello,"

print(greeting)
print(greeting + " João")
print(greeting + " Maki")

happy_end = "End"

print(happy_end)

##

# data types
text = "text" #string
number = 100
decimal = 0.5
com = 8j


lotto_numbers = (1, 2, 3, 4, 5)

numbers = randrange(1, 1000) ##precisa importar a biblioteca 
print(numbers)

users = {'user1' : 'Maki123', 'user2' : 'Pipoca'}
print(users)

##
name: str = "Mário"
number2: int = 100
print(name)
print(number2)

##
name1 = 'João'
number1 = 10

result = name1 + str(number)

print(type(result)) ## descobrir o tipo de dado de uma variavel

print(result)

## 
number_hundred = '100' #str
number3 = 10

result = number3 + int(number_hundred) # conversao de tipos, castingx
print(result)

print(10!=10)

## F-String
var = "Text"

new_String = f"1 {var} 2"
print(new_String)

