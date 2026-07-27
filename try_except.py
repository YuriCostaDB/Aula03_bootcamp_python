"""
try:
    gols = int(input("Quantos gols o Brasil fez? "))
    print(f"O Brasil fez {gols} gols!")
except Exception as e:
    print(e)
"""

numero_valido = False
while numero_valido == False:
    try:
        gols: int = int(input("Quantos gols o Brasil fez?: "))
        numero_valido = True
    except:
        print("Digite um número válido!")

print(f"O Brasil fez {gols} gols!")
