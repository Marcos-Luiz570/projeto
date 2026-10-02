# f(x) = y
# f(x) = 2x
# f(2) = 4
# f(5) = 10

def olaMundo():
    print('Olá, mundo!')

def olaPessoa(nome):
    print(f'Olá, {nome}!')

def dobro(numero):
    return numero * 2

def multiplicaDoisNumeros(a, b = 2):
  """
  Multiplica dois números.
  """
  return a * b

# print(multiplicaDoisNumeros(3, 6))
# print(multiplicaDoisNumeros(3))

x = 5 # variável global
def soma():
      x = 10 # variável local
      print(x)
      return x + 1
soma()
print(x)








