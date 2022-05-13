ano_nasc = int(input('Informe seu ano de nascimento: '))
ano_atual = int(input('Informe o ano atual: '))
idade = ano_atual - ano_nasc
print('Pelos dados informados, sua idade é: ',idade)
if (idade < 18):
    print('Sendo assim, não é possível tirar carteira de motorista, pois você é de menor!')
else:
    print('Sendo assim, já é possível tirar sua carteira de motorista!')