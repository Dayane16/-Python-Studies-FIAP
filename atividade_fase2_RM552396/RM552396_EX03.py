print('Este algoritimo calcula a média das notas dos alunos da sala!')

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