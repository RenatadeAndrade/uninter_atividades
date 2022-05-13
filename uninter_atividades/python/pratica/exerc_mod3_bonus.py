ano_entrada = int(input('Em qual ano você foi contratado pela empresa? '))
ano_atual = int(input('Qual ano atual? '))
tempo_servico = ano_atual - ano_entrada
salario = float(input('Qual o seu salário mensal? '))
bonus1 = salario+(salario*(10/100))
bonus2 = salario+(salario*(20/100))


if (tempo_servico < 5):
    print('Você presta serviços nessa empresa há {} anos. Seu salário mensal é: R$ {:.2f} Você receberá um bônus de 10% em cima do seu salário. Seu novo salário será: R$ {:.2f}'.format(tempo_servico, salario, bonus1))
else:
    print('Você presta serviços nessa empresa há {} anos. Seu salário mensal é: R$ {:.2f} Você receberá um bônus de 20% em cima do seu salário atual. Seu novo salário será: R$ {:.2f}'.format(tempo_servico, salario, bonus2)) 