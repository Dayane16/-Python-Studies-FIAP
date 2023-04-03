#Muitos professores preferem adotar modelos diferentes 
#de provas quando dão aulas para turmas muito grandes. 
#Por essa razão, a escola de inglês JoWell Sant’ana, 
#em que todas as turmas são compostas por 50 alunos, 
#solicitou que você criasse um sistema capaz de atender
#ao seguinte requisito: o professor deve digitar primeiro
#as notas dos 25 alunos que têm número ímpar na chamada
#(1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que 
#têm número par (2, 4, 6..., 48, 50). O sistema deve calcular 
#e exibir a média de cada uma das metades da sala e informar, 
#ao final, qual delas teve a maior nota.

#Há ainda um pedido especial do mantenedor: para que os 
#professores não se confundam, ao digitar cada uma das notas, 
#deve ser exibida uma mensagem no seguinte padrão:

#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
nota_par = 0
nota_impar = 0

print('Você está digitando as notas dos alunos ímpares.')

for i in range(1,50,2):  
    nota = float(input(f'Por favor, insira a nota do aluno de número {i}: '))
    while nota < 0 or nota > 10:
        nota = float(input(f'Você digitou uma nota inválida, por favor, insira novamente a nota do aluno de número {i}: ')) 
    nota_impar = nota_impar + nota          
    
print('Você está digitando as notas dos alunos pares.')
for i in range(2,51,2):
    nota = float(input(f'Por favor, insira a nota do aluno de número {i}: '))
    while nota < 0 or nota > 10:
        nota = float(input(f'Você digitou uma nota inválida, por favor, insira novamente a nota do aluno de número {i}: ')) 
    nota_par = nota_par + nota
    
media_par = nota_par/25
media_impar = nota_impar/25

print(f'A média da metade da sala de nùmero par é de {media_par}, e a metade ímpar é de {media_impar}.')

if media_par > media_impar:
    print(f'A maior média é da metade da turma de número par!')
else:
    print(f'A maior média é da metade da turma de número ímpar!')
    
input("Pressione Enter para sair...")