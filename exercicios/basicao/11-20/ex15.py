# Exercício Python #015 - Aluguel de Carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugados = int(input("Quantos dias alugados?: "))
kmRodados = float(input("Quantos Km rodados?: "))

total = (60 * diasAlugados) + (0.15 * kmRodados)

print(f"\nO total a pagar é de R${total:.2f}")