print('Olá, eu sou a sua assistente, Pythrina. O que você quer fazer hoje?')
comando = input('Digite um comando: ')

match comando:
    case 'oi' | 'olá' | 'ola':
        print('Oi, como vai você?')
    case 'tchau' | 'sair' | 'fim' | 'exit':
        print('Tchau, foi bom conversar com você!')
    case 'piada':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login!')
    case 'clima' | 'previsão do tempo':
        print('Tá muuuuito quente!! Deve ter passado dos 40ºC!')
    case _ :
        print('Desculpe, não entendi o comando. Tente novamente.')

