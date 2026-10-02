frase = " O curso de Lógica de Programação é supimpa! "
# print(f'Primeira letra: {frase[0]}')
# print(f'Última letra: {frase[-1]}')
# print(f'Tamanho da frase: {len(frase)} caracteres')
# print()
# print(f'Frase em maiúsculas: {frase.upper()}')
# print(f'Frase em minúsculas: {frase.lower()}')
# print()
# print(f'Fatiando{frase.split()}')
# print(f'Fatiando{frase.split("a")}')
# print()
# print(f'Frase origianal: {frase}')
# print(f'Limpado{frase.strip()}')
# print(f'Tamanho da string limpa: {len(frase.strip())}')

def analisadorDeTexto(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    num_caracteres_sem_espacos = num_caracteres - texto.count(" ")
    return num_palavras, num_caracteres, num_caracteres_sem_espacos

num_p, num_c, num_cse = analisadorDeTexto(frase)
print(f'Número de palavras: {num_p}')
print(f'Número de caracteres: {num_c}')
print(f'Número de caracteres sem espaços: {num_cse}')

  