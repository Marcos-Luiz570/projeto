# nomes = [
#   "João",
#   "Antonio",
#   "Maria",
#   "Ermengarda",
#   "Ana",
#   "Anacleto",
#   "Bianca",
#   "José",
#   "Adão",
#   "Josi"
# ]

# tabela = {}

# for nome in nomes:
#     qtd = nome [0]
#     if qtd not in tabela:
#         tabela[qtd] = []
#     tabela[qtd].append(nome)

# print(tabela)


# criar um texto com várias palavras e separar as palavras em uma tabela hash, onde a chave é a primeira letra da palavra e o valor é uma lista de palavras que começam com essa letra.

palavras = 'texto'.split()

tabela = {}
for palavra in palavras:
    indice = palavra[0].upper()
    if indice not in tabela:
        tabela[indice] = []
    tabela[indice].append(palavra)

for chave, valor in tabela.items():
    print(f"{chave}: {len(valor)}")

print(len('texto'.split()))
