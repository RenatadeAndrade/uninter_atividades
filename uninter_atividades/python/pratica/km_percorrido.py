km = int(input('Informe a quantidade de Km percorrido: '))
dias = int(input('Informe por quantos dias irá alugar o carro: '))
preco = (dias*60)+(km*0.15)
print('O preço a pagar é: R$ {:.2f}'.format(preco))
