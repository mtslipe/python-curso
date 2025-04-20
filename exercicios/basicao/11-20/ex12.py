# Exercício Python #012 - Calculando Descontos

class Desconto:
    def aplicarDesconto(preco : float, porcentagemDesconto : int):
        valor = preco - ((porcentagemDesconto / 100) * preco) # porcentagem de desconto sobre cem, vezes o preco = valor de desconto. preco - valor de desconto.
        return valor
    
desconto = Desconto()

preco = float(input("Qual o preço do produto? R$"))
porcentagemDesconto = int(input("Qual o desconto? %")) # por cento

print(f"\nO produto que custava R${preco:.2f}, na promoção com desconto de {porcentagemDesconto}% vai custar R${desconto.aplicarDesconto(preco, porcentagemDesconto):.2f}")