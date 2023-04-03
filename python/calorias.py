#Contador de calorias

print('Este é um contador de clarorias!')

calorias_total = 0
total_alimentos = int(input('Escreva o total de alimentos que você consumiu hoje: '))

while (total_alimentos != 0):
    calorias = int(input('Qual total de calorias do alimento?'))
    calorias_total = calorias + calorias_total
    total_alimentos = total_alimentos - 1
    
print(f'O total de calorias é de {calorias_total}')
