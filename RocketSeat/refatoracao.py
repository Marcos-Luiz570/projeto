def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

media = calcular_media(7, 4)
print(f'status: {verificar_aprovacao(media)} Média: {media}')

media2 = calcular_media(8, 9)
print(f'status: {verificar_aprovacao(media2)} Média: {media2}')