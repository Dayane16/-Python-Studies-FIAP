print('Este programa calcula o valor do bônus a ser pago com base na assinatura do cliente!')

assinatura = input('Escreva qual seu tipo de assinatura (BASIC, SILVER, GOLD OU PLATINUM): ')
faturamento = float(input('Qual foi o seu faturamento anual? '))

if assinatura.upper() == 'BASIC':
    bonus = faturamento * 0.3
elif assinatura.upper() == 'SILVER':
    bonus = faturamento * 0.2
elif assinatura.upper() == 'GOLD':
    bonus = faturamento * 0.1
elif assinatura.upper() == 'PLATINUM':
    bonus = faturamento * 0.05
else:
    print('Você digitou uma assinatura inválida')
    bonus = None
    
if bonus is not None:
    print('O valor do bônus a ser pago é de R${:.2f}'.format(bonus))