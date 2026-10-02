lista = None

def exibeLista():
    if not lista:
        print("Lista vazia.")
        return ()
    elemento = lista

    while elemento != None:
        print(f'Valor: {elemento["valor"]}', end="  ")
        elemento = elemento["proximo"]

    print(".")

def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = {"valor": elemento, "proximo": None }
        return
    atual = lista
    while atual["proximo"] != None:
        atual = atual["proximo"]
    atual["proximo"] = {"valor": elemento, "proximo": None }  

exibeLista()
print("Adicionando o 5...")
adicionaNoFim(5)
exibeLista()
print("Adicionando o 8...")
adicionaNoFim(8)
print("Adicionando o 13...")
adicionaNoFim(13)
exibeLista()

  