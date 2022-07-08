#Início da função que irá receber os dados de altura, comprimento e largura
do objeto.
def dimensoesObjeto():
#Repetir enquanto bloco de código for verdadeiro.
while True:
#Tratamento de erro quando for digitado um valor que não seja numérico.
try:
#Variável que irá receber os dados de comprimento.
comprimento = float(input('Digite o comprimento do objeto em
cm: '))
#Variável que irá receber os dados de largura.
largura = float(input('Digite a largura do objeto em cm: '))
#Variável que irá receber os dados de altura.
altura = float(input('Digite a altura do objeto em cm: '))
#Variável que irá calcular o volume do objeto.
volume = comprimento * largura * altura
#Condições que irão receber o volume em cm e retornar o valor
correspondente.
if volume <= 1000:
print('O volume do objeto em cm³ é: {:.2f}'.format(volume))
return 10.00
elif volume >= 1001 and volume <= 10000:
print('O volume do objeto em cm³ é: {:.2f}'.format(volume))
return 20.00
elif volume >= 10001 and volume <= 30000:
print('O volume do objeto em cm³ é: {:.2f}'.format(volume))
return 30.00
elif volume >= 30001 and volume <= 100000:
print('O volume do objeto em cm³ é: {:.2f}'.format(volume))
return 50.00
#Caso o volume ultrapasse os valores condicionais, irá informar que não
aceita.
else:
print('O volume do objeto em cm³ é: {:.2f}'.format(volume))
print('Não aceitamos objetos com dimensões tão
grandes.\nDigite as dimensões desejadas novamente.')
#Irá retornar ao inicio da função solicitando dados novamente, até que o
valor corresponda às condicionais.
continue
#Final do try, para tratar erros.
except ValueError:
print('Você digitou alguma dimensão do objeto com valor não
numérico.\nPor favor, digite as dimensões desejadas novamente.')
#Irá retornar ao início da função, solicitando dados novamente, até que o
usuário digite um valor numérico.
continue
#Fim da função dimensoesObjeto
#Início da função que irá receber os dados de peso do objeto.
def pesoObjeto():
#Repetir enquanto bloco de código for verdadeiro.
while True:
#Tratamento de erro quando for digitado um valor que não seja numérico.
try:
#Variável que irá receber os dados de peso do objeto.
peso = float(input('Digite o peso do objeto em kg: '))
#Condições que irão receber o peso em kg e retornar o valor correspondente.
if peso <= 0.1:
return 1.0
elif peso >= 0.11 and peso <= 1:
return 1.5
elif peso >= 1.10 and peso <= 10:
return 2.0
elif peso >= 10.1 and peso <= 30:
return 3.0
#Caso o peso ultrapasse os valores condicionais, irá informar que não
aceita.
else:
print('Não aceitamos objetos tão pesados.\nDigite o peso
desejado novamente.')
#Irá retornar ao inicio da função solicitando dados novamente, até que o
valor corresponda às condicionais.
continue
#Final do try, para tratar erros.
except ValueError:
print('Você digitou peso do objeto com valor não numérico.\nPor
favor, digite o peso desejado novamente.')
continue
#Fim da função pesoObjeto
#Início da função que irá receber a rota desejada.
def rotaObjeto():
#Repetir enquanto bloco de código for verdadeiro.
while True:
#Variável que irá informar as rotas disponíveis do objeto e em seguida
receber a rota desejada.
rota = input('Rotas disponíveis:\n|SP - De Sergipe para
Paraíba|\n|SR - De Sergipe para Recife |\n|PS - Da Paraíba para
Sergipe|\n|PR - De Paraíba para Recife |\n|RP - De Recife para Paraíba
|\n|RS - De Recife para Sergipe |\nInforme a rota desejada: ')
#Condições que irão receber a rota desejada e retornar o valor
correspondente.
if rota == "SP":
return 1.0
elif rota == "SF":
return 1.0
elif rota == "PS":
return 1.2
elif rota == "PR":
return 1.2
elif rota == "RP":
1.5
elif rota == "RS":
return 1.5
#Caso o usuário digite algum caracter que não esteja na tabela de rotas,
irá informar que rota não existe.
else:
print('Você digitou uma rota que não existe!\nPor favor, digite
a rota desejada novamente.')
#Irá solicitar para usuário digitar a rota novamente.
continue
#Fim da função rotaObjeto
#Print com o nome do aluno.
print('Bem-vindo a Companhia de Logística Renata de Andrade Sousa!')
#Imprimindo valor final, chamando as funções e multiplicando-as.
print('Valor total a pagar: R$ {:.2f}'.format(dimensoesObjeto() *
pesoObjeto() * rotaObjeto()))
print('********** Volte Sempre! **********')