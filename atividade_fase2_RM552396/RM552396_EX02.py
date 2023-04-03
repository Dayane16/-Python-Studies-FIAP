# Os alunos da sua turma fizeram uma votação para escolher qual 
# dia da semana é o melhor para a realização das lives. Desenvolva 
# um programa em que o usuário informe a quantidade de votos que 
# cada um dos 5 dias da semana  (segunda-feira, terça-feira, quarta-feira, 
# quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

seg = int(input('Qual total de votos que a segunda-feira teve? '))
ter = int(input('Qual total de votos que a terça-feira teve? '))
quar = int(input('Qual total de votos que a quarta-feira teve? '))
qui = int(input('Qual total de votos que a quinta-feira teve? '))
sext = int(input('Qual total de votos que a sexta-feira teve? '))

voto = 0
vencedor = ''
empate = ''

if seg > voto:
    voto = seg
    vencedor = 'Segunda-Feira'
if ter > voto:
    voto = ter
    vencedor = 'Terça-Feira'
if quar > voto:
    voto = quar
    vencedor = 'Quarta-Feira'
if qui > voto:
    voto = qui
    vencedor = 'Quinta-Feira'
if sext > voto:
    voto = sext
    vencedor = 'Sexta-Feira'


if seg == voto and vencedor != 'Segunda-Feira':
    empate = empate + ' Segunda-Feira,'
if ter == voto and vencedor != 'Terça-Feira':
    empate = empate + ' Terça-Feira,'
if quar == voto and vencedor != 'Quarta-Feira':
    empate = empate + ' Quarta-Feira,'
if qui == voto and vencedor != 'Quinta-Feira':
    empate = empate + ' Quinta-Feira,'
if sext == voto and vencedor != 'Sexta-Feira':
    empate = empate + ' Sexta-Feira,'
    
if empate:
    print(f'Houve empate entre os dias {vencedor}{empate} com {voto} votos! \nTotal de votos: \nSegunda-Feira: {seg} \nTerça-Feira: {ter} \nQuarta-Feira: {quar} \nQuinta-Feira: {qui} \nSexta-Feira: {sext}')
else:
    print(f'O dia vencedor foi {vencedor} com {voto} votos! \nTotal de votos: \nSegunda-Feira: {seg} \nTerça-Feira: {ter} \nQuarta-Feira: {quar} \nQuinta-Feira: {qui} \nSexta-Feira: {sext}')
