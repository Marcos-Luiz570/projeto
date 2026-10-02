# Tipos primitivos de dados em Python

# - int (integer): números inteiros
# - float (floating-point): números decimais (ponto flutuante)
# - str (string): cadeia de caracteres (texto)
# - bool (boolean): valores lógicos (True ou False)

# Operadores aritméticos: +, -, *, /, //, %, **
# - + : adição
# - - : subtração
# - * : multiplicação
# - / : divisão
# - // : divisão inteira
# - % : módulo (resto da divisão)
# - ** : potenciação

# Operadores lógicos: and, or, not
# - and : e lógico
# - or : ou lógico
# - not : não lógico

# Operadores de strings: + concatenação de strings, * repetição de strings, in, not in

# Operadores de comparação: ==, !=, >, <, >=, <=
# recebem valores de diversos tipos e retornam um valor booleano (True ou False)
# - == : igual a
# - != : diferente de
# - > : maior que
# - < : menor que
# - >= : maior ou igual a
# - <= : menor ou igual a

# Estruturas de dados: listas, tuplas, dicionários, conjuntos

# Listas: conjuntos de dados ordenados e mutáveis de elementos
lista = [1, 2, 3, 4, 5]
frutas = ['maçã', 'banana', 'laranja']
mista = [1, 'maçã', 3.14, True]

#Tuplas: conjuntos de dados ordenados e imutáveis de elementos
coordenadas = (5, 6)
tupla = (5, 4, 3, 2)

# Dicionários (dict): conjuntos de dados não ordenados e mutáveis de pares na formachave e valor 
pessoa = {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}
carro = {'marca': 'Toyota',
         'modelo': 'Corolla',
         'ano': 2020,
         'cor': 'prata'
}

# Conjuntos (set): conjuntos de dados não ordenados e sem repetições de elementos
c1 = {1, 2, 3}
c2 = {3, 2, 1}
c3 = {1, 2, 2, 3, 3, 3}  # c3 será igual a {1, 2, 3}