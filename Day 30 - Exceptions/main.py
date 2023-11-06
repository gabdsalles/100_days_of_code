#FileNotFound

# try:
#     file = open("./Day 30 - Exceptions/a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("./Day 30 - Exceptions/a_file.txt", "w")
#     file.write("Alguma coisa")
# except KeyError as error_message:
#     #print("essa chave não existe.")
#     print(f"A chave {error_message} não existe.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("Arquivo fechado.")
#     # raise KeyError("Mensagem de erro.")

# Exemplo IMC

altura = float(input("Altura: "))
peso = float(input("Peso: "))

if altura > 3:
    raise ValueError("Altura não deve ser maior que 3 metros!")

imc = peso / altura ** 2

print(imc)