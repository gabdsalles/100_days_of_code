def correct_list(list):
  temp_list = []
  for num in list:
    temp_list.append(int(num.strip()))
  return temp_list

with open('./Day 26 - List Comprehension/file1.txt') as file1:
  list = file1.readlines()
  list1 = correct_list(list)

with open('./Day 26 - List Comprehension/file2.txt') as file2:
  list = file2.readlines()
  list2 = correct_list(list)

result = [num for num in list1 if num in list2]

# Write your code above 👆
print(result)
