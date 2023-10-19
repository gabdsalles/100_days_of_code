#LIST COMPREHENSION
import random

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers] #adicione mais 1 para cada número da lista

name = "Angela"
new_list = [letter for letter in name] #separa cada letra do nome
print(new_list)

range = range(1,5)
list_range = [i*2 for i in range] #range(1,5) = 1, 2, 3, 4
print(list_range)

#Condicional
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5] #se o if for verdadeiro, adiciona na lista nova
print(short_names)

big_caps_names = [name.upper() for name in names if len(name) > 5] #podemos utilizar outras funções dentro tbm
print(big_caps_names)

#DICTIONARY COMPREHENSION
students_scores = {student:random.randint(1,100) for student in names} #cria um dicionário a partir de uma lista. o nome do student vem da lista e a nota vem do random
print(students_scores)

passed_students = {student:grade for (student, grade) in students_scores.items() if grade > 60} #a partir do dict anterior, usa condicional p/pegar apenas notas acima de 60
print(passed_students)

