#import numpy as np

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Solução utilizando Numpy
#print(round(np.mean(student_heights)))

#Solução com for, sem utilizar as funções len() e sum() do python

total_sum = 0
students_count = 0

for height in student_heights:
  students_count += 1
  total_sum += height

mean = round(total_sum / students_count)
print(mean)

for i in range(10):
 print(i)



