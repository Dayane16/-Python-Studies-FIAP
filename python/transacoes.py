num_transacoes = int(input('Escreva o total de transações realizadas: '))
gasto_total = 0

for i in range (num_transacoes):
    gasto=float(input(f'Qual foi o valor total desta transção {i+1}? '))
    gasto_total = gasto_total + gasto
    
media = gasto_total/num_transacoes

print(f'O gasto total foi de {gasto_total}, e a media de gastos foi de {media}')