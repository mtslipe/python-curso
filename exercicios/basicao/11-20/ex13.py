# Exercício Python #013 - Reajuste Salarial

def aumento():
    salaumento = sal + ((aumentoPorc / 100) * sal)
    return salaumento

sal = float(input("Qual o salário do Funcionário? R$"))
aumentoPorc = int(input("Qual a porcentagem do aumento? %")) # por cento

print(f"Um funcionário que ganhava R${sal:.2f}, na com aumento de {aumentoPorc}%, passa a receber R${aumento():.2f}")