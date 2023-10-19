sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
# A entrada é uma lista de palavras, ou uma frase.
list_words = sentence.split(' ')
#print(list_words)

result = {word:len(word) for word in list_words}

print(result)
