print('Algoritimo para sequencia de Fibonacci')

num= int(input('Digite um número: '))

a,b = 1,0

while a < num:
    a,b=a+b,a
    
if a == num:
    print('Ação bem sucedida')
else:
    print('Ação não foi bem sucedida')