# Exercício Python #011 - Pintando Parede
# cada 2m² de parede precisa de 1l de tinta

def tinta():
    a = metrosq / 2 
    return a

l = float(input("Largura da parede em Metros: "))
a = float(input("Altura da parede em Metros: "))
metrosq = l * a

print(f"\nSua parede tem a dimensão de {l}x{a} e sua área é de {metrosq}m²")
print(f"Para pintar essa parede, você precisará de {tinta()}l de tinta.")