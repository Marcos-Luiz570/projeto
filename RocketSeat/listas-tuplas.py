# lista = [1, 2, 3, 4, 5]
# tupla = (1, 2, 3, 4, 5)
import os

tarefas = []
def adicionaTarefa(tarefa):
   novaTarefa = (tarefa, 'pendente')
   tarefas.append(novaTarefa)

def exibeTarefas():
   if not tarefas:
      print("A Lista está vazia.")
      return
   for tarefa in tarefas:
      print(f'Tarefa: {tarefa[0]} - Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas
    tarefas = [(t[0], 'concluída') if t[0] == tarefa else t for t in tarefas]

def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa]

def buscarTarefa(tarefa):
    resultado = [t for t in tarefas if t[0].lower() == tarefa.lower()]
    if len(resultado) > 0:
        for titulo, status in resultado:
            print(f'Tarefa encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada. "{tarefa}"')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Boas Vindas ao Gerenciador de Listas de Tarefas!")
    print()
    print("O que você quer fazer agora?")
    print("1. Listar Tarefas")
    print("2. Adicionar Tarefa")
    print("3. Remover Tarefa")
    print("4. Marcar Tarefa como Concluída")
    print("5. Buscar Tarefa")
    print("0. Sair")

    opcao = input("Digite uma opção: ")

    match opcao:
        case '1':
            exibeTarefas()
        case '2':
            tarefa = input("Digite a tarefa: ")
            adicionaTarefa(tarefa)
        case '3':
            tarefa = input("Digite a tarefa: ")
            removerTarefa(tarefa)
        case '4':
            tarefa = input("Digite a tarefa: ")
            concluirTarefa(tarefa)
        case '5':
            tarefa = input("Digite a tarefa: ")
            buscarTarefa(tarefa)
        case '0':
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida.")
    print()
    input("Pressione Enter para continuar...")
   
  