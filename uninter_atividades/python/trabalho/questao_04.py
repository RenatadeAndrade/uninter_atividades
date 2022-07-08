#Array que irá receber os dados de dicionário.
listaPeca = []
#Função que irá cadastrar as peças.
def cadastrarPeca(codigo):
print('----- Cadastro de peças -----')
#Print que irá receber o código e exibi-lo adicionando +1 a
cada cadastro.
print('O CÓDIGO da peça a ser cadastrado é {}'.format(codigo))
#Nome da peça
nome = input('Digite o NOME da peça: ')
#Fabricante da peça
fabricante = input('Digite o FABRICANTE da peça: ')
#Valor da peça
valor = float(input('Digite o VALOR (R$) da peça: '))
#Dicionário que irá alocar os dados inseridos no cadastro.
dicionarioPeca={'codigo':codigo,
'nome':nome,
'fabricante':fabricante,
'valor':valor
}
#Irá exibir uma cópia dos dados contidos em dicionário.
listaPeca.append(dicionarioPeca.copy())
#Irá remover itens contidos no dicionário.
dicionarioPeca.clear()
#Função que irá permitir a consulta das peças cadastradas.
def consultaPeca():
#Enquanto for verdadeiro irá repetir o bloco de código.
while True:
#Irá tratar os erros de exceção
try:
print('----- Consulta de peças -----')
#Opção que irá definir o que o usuário deseja consultar.
menuPecas = int(input('O que deseja fazer?\n- 1 - Consultar
todas as peças.\n- 2 - Consultar peças por código.\n- 3 - Consultar peças
por fabricante.\n- 4 - Retornar.\nDigite a opção desejada:\n>>'))
#Condições que, irá ser exibida de acordo com as opções de
consulta disponíveis.
if menuPecas == 1:
print('Bem-vindo a consultar TODAS AS PEÇAS')
#Selecionar cada dicionário da minha lista.
for pecas in listaPeca:
#Selecionar cada campó do dicionário.
for key, value in pecas.items():
#Exibir campos do dicionário.
print('{} : {}\n'.format(key,value))
elif menuPecas == 2:
print('Bem-vindo a consultar por CÓDIGO')
#Dado que irá comparar o código digitado com os códigos da
lista
entrada = int(input('Digite o CÓDIGO desejado: '))
#Selecionar items específicos da lista.
for pecas in listaPeca:
#Verificar códigos existentes
if(pecas['codigo'] == entrada):
for key, value in pecas.items():
#Exibir código digitado.
print('{} : {}'.format(key,value))
elif menuPecas == 3:
print('Bem-vindo a consultar por FABRICANTE')
#Dado que irá comparar o fabricante digitado com os
fabricantes da lista
entrada = input('Digite o FABRICANTE desejado: ')
#Selecionar items específicos da lista.
for pecas in listaPeca:
#Verificar fabricantes existentes
if(pecas['fabricante'] == entrada):
for key, value in pecas.items():
#Exibir fabricante digitado.
print('{} : {}'.format(key,value))
#Se opção for sair, encerrar o laço.
elif menuPecas == 4:
break
#Se usuário digitar opção não existente, exibir mensagem de
erro e retornar às opções.
else:
print('Opção não disponível. Digite novamente.')
continue
#Tratamento de erro caso usuário digite caracteres inválidos,
retornando às opções.
except ValueError:
print('Você digitou opção não inteira, ou caracteres inválidos.
Digite novamente')
continue
#Função para remover itens da lista.
def removerPeca():
print('----- Remoção de peças -----')
print('Bem-vindo a remover por CÓDIGO')
#Dado que irá comparar o código digitado com os código da lista que
deseja remover.
entrada = int(input('Qual CÓDIGO deseja remover?'))
#Selecionar items específicos da lista.
for pecas in listaPeca:
#Verificar códigos existentes
if(pecas['codigo'] == entrada):
#Remover código digitado.
listaPeca.remove(pecas)
#Se usuário digitar código não existente, exibir mensagem de erro e
retornar à opção.
else:
print('Você digitou um código inexistente. Por favor, digite o
código novamente.')
continue
#Print com o nome do aluno.
print('Bem-vindo ao Controle de estoque da Bicicletaria da Renata de
Andrade Sousa\n')
#Acumulador
codigoPeca = 0
#Bloco de código principal, contendo as opções.
#Repetir enquanto bloco for verdadeiro.
while True:
#Tratamento de erros.
try:
#Dado que irá receber opção desejada.
escolhaOpcao = int(input('Escolha a opção desejada:\n- 1 -
Cadastrar Peças\n- 2 - Consultar Peças\n- 3 - Remover Peças\n- 4 - Sair\n>>
'))
#Condições que irá ser exibida de acordo com as opções de consulta
disponíveis.
if escolhaOpcao == 1:
#Contador que irá acumular os códigos que serão cadastrados.
codigoPeca += 1
#Chamada da função, para cadastrar peças
cadastrarPeca(codigoPeca)
elif escolhaOpcao == 2:
#Chamada da função para consultar peças
consultaPeca()
elif escolhaOpcao == 3:
#Chamada da função para remover peças
removerPeca()
elif escolhaOpcao == 4:
#Encerrando programa.
print('Programa Encerrado. Até a próxima!')
break
#Se usuário digitar código não existente, exibir mensagem de erro e
retornar à opção.
else:
print('Opção não disponível. Digite novamente.')
continue
#Tratamento de erro caso usuário digite caracteres inválidos,
retornando às opções.
except ValueError:
print('Você digitou opção não inteira, ou caracteres inválidos.
Digite novamente')
continue