# Exercício Python #009 - Tabuada

num = int(input("Digite um numero que voce deseja ver a tabuada: \n"))

aux = 1
while aux <= 10:
    print(f"{num} x {aux} = {num * aux}")
    aux += 1
