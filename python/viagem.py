print('Desconto em passagens aereas!')

valor_pacote = float(input('Qual valor do pacote? '))
categoria_assento= input('Qual a categoria do assento? ')
viajantes = float(input('Quantos vijantes? '))

if categoria_assento.upper() == 'ECONOMICA':
    if viajantes == 2:
        desconto = valor_pacote - valor_pacote * 0.03
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
    elif viajantes == 3:
        desconto = valor_pacote - valor_pacote * 0.04
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
    elif viajantes >= 4:
        desconto = valor_pacote - valor_pacote * 0.05
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
elif categoria_assento.upper() == 'EXECUTIVA':
    if viajantes == 2:
        desconto = valor_pacote - valor_pacote * 0.05
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
    elif viajantes == 3:
        desconto = valor_pacote - valor_pacote * 0.07
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
    elif viajantes >= 4:
        desconto = valor_pacote - valor_pacote * 0.08
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
elif categoria_assento.upper() == 'PREMIUM':
    if viajantes == 2:
        desconto = valor_pacote - valor_pacote * 0.10
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
    elif viajantes == 3:
        desconto = valor_pacote - valor_pacote * 0.15
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
    elif viajantes >= 4:
        desconto = valor_pacote - valor_pacote * 0.20
        print('O valor da sua passagem com desconto será de R${}'.format(desconto))
        
    
            