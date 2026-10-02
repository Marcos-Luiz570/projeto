def calcular_media(notas):
    return sum(notas) / len(notas)
def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"
    

# snake_case - funções e variáveis em Python: calcular_media
# camelCase - funções e variáveis em JavaScript: calcularMedia, usado em linguagens como JavaScript, Java e C# mas não em Python.
# PascalCase - recomendado para nome de classes em Python. Usado para palavras compostas, como MinhaClasse. Exemplo: MinhaClasse
# kebab-case - não pode ser usado para nome de funções e variáveis em Python, por que no código pode ser interpretado como subtração, mas é usado em nomes de arquivos e URLs. Exemplo: boas-praticas.py
# SCREAMING_SNAKE_CASE - usado para constantes em Python. Exemplo: MINHA_CONSTANTE; PI_3,14
# lowercase - usado para nomes de módulos e pacotes em Python. Exemplo: meu_modulo, meu_pacote; com letras minúsculas e sem espaços, com palavras separadas por underline. Exemplo: meu_modulo, meu_pacote
# powercase - usado para nomes de pacotes em Python. Exemplo: MeuPacote; com letras maiúsculas e sem espaços, com palavras juntas. Exemplo: MeuPacote
