#Exercício Python #004 - Dissecando uma Variável

a = str(input("Digite algo: "))

print(f"O tipo primitivo desse valor é: {type(a)}") 
print(f"Só tem espaços?: {a.isspace()}")
print(f"É um número?: {a.isnumeric()}")
print(f"É alfabético?: {a.isalpha()}")
print(f"Está em maiúscula?: {a.isupper()}")
print(f"Está em minúscula?: {a.islower()}")
print(f"Está captalizada?: {a.istitle()}")