# Exercício Python #012 - Calculando Descontos

def aplicarDesconto():
    valor = preco - ((porcentagemDesconto / 100) * preco) # porcentagem de desconto sobre cem, vezes o preco = valor de desconto. preco - valor de desconto.
    return valor



preco = float(input("Qual o preço do produto? R$"))
porcentagemDesconto = int(input("Qual o desconto? %")) # por cento

print(f"\nO produto que custava R${preco:.2f}, na promoção com desconto de {porcentagemDesconto}% vai custar R${aplicarDesconto():.2f}")