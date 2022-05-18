#Cardápio expositivo da lanchonete.
print('Bem Vindo a Lanchonete da Renata de Andrade Sousa.') #Nome do aluno.
print('**************** Cardápio ***************')
print('| Código |       Descrição       | Valor |')
print('|   100  |    Cachorro Quente    |  9,00 |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |         X-Egg         | 12,00 |')
print('|   103  |        X-Salada       | 12,00 |')
print('|   104  |        X-Bacon        | 14,00 |')
print('|   105  |         X-Tudo        | 17,00 |')
print('|   200  |  Refrigerante Lata    |  5,00 |')
print('|   201  |      Chá Gelado       |  4,00 |')
print('\n')

#Valor inicial para ir acumulando os valores dos itens pedidos.
valor_total = 0

#Repetir enquanto for verdadeiro.
while True:
#Entrar com o código disponível na tabela Cardápio.
    codigo = int(input('Entre com o código referente ao pedido:'))
#Quando for escolhido o item de acordo com o código, irá entrar no if, elif, seguindo a descrição da tabela Cardápio.
    if codigo == 100:
        valor_total = valor_total + 9
        print('Você pediu um Cachorro Quente no valor de R$ 9,00.')
    elif codigo == 101:
        valor_total = valor_total + 11
        print('Você pediu um Cachorro Quente Duplo no valor de R$ 11,00.')
    elif codigo == 102:
        valor_total = valor_total + 12
        print('Você pediu um X-Egg no valor de R$ 12,00.')
    elif codigo == 103:
        valor_total = valor_total + 12
        print('Você pediu um X-Salada no valor de R$ 12,00.')
    elif codigo == 104:
        valor_total = valor_total + 14
        print('Você pediu um X-Bacon no valor de R$ 14,00.')
    elif codigo == 105:
        valor_total = valor_total + 17
        print('Você pediu um X-Tudo no valor de R$ 17,00.')
    elif codigo == 200:
        valor_total = valor_total + 5
        print('Você pediu um Refrigerante Lata no valor de R$ 5,00.')
    elif codigo == 201:
        valor_total = valor_total + 4
        print('Você pediu um Chá Gelado no valor de R$ 4,00.')
#Mensagem de erro, caso cliente digite um código ausente no cardápio, retornando ao inicio do bloco de código.
    else:
        print('Opção Inválida! Por favor, digite o código novamente.\n')
        continue
#Se o cliente desejar pedir algo mais, escolhe Sim ou Não.
    opcao = input('Deseja pedir mais alguma coisa? Digite: \n- s para Sim\n- n para Não\n')
    if opcao == "s":
        continue
#Caso o cliente não deseje pedir mais nada, apresentar o valor final.
    else:
        print('Pedido encerrado. O total a ser pago é: R$ {:.2f}\n***************** Volte sempre! *****************'.format(valor_total))
        break
