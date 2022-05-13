#print com o nome da aluna.
print('Bem Vindo a Loja da Renata de Andrade Sousa')
#Valor do produto.
valor = float(input('Digite o valor do produto:R$ '))
#Quantidade de produtos comprado.
quant = int(input('Digite a quantidade do produto: '))
#Cálculo para obter o valor total da compra.
total = valor * quant
#Cálculo para obter o valor do produto com descontos de 5% aplicado.
desconto5 = total - (5/100*total)
#Cálculo para obter o valor com descontos de 10% aplicado.
desconto10 = total - (10/100*total)
#Cálculo para obter o valor com descontos de 15% aplicado.
desconto15 = total - (15/100*total)
#Se foi comprado até 9 produtos, nenhum desconto é aplicado.
if quant <= 9:
    print('Quantidade de produtos não tem desconto a ser aplicado. O valor sem desconto foi:R$ {:.2f}'.format(total))
#Se foi comprado entre 10 e 99 produtos, o desconto é de 5%.
elif quant >= 10 and quant <= 99:
    print('O valor final da compra foi:R$ {:.2f}'.format(total))
    print('Desconto de 5% aplicado. Valor com desconto foi:R${:.2f}'.format(desconto5))
#Se foi comprado entre 100 e 999 produtos, o desconto é de 10%.
elif quant >= 100 and quant <= 999:
    print('O valor final da compra foi:R$ {:.2f}'.format(total))
    print('Desconto de 10% aplicado. Valor com desconto foi:R${:.2f}'.format(desconto10))
#Se foi comprado acima de 1000 produtos, o desconto é de 15%.
else:
    print('O valor final da compra foi:R$ {:.2f}'.format(total))
    print('Desconto de 15% aplicado. Valor com desconto foi:R${:.2f}'.format(desconto15))
