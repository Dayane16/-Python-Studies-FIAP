print('Este algoritimo calcula o fatorial dos minutos informados para a senha que irá liberar a máquina!')

m = int(input('Digite os minutos atuais: '))

fatorial = 1
for i in range(1,m+1):
    fatorial *= i   
    
print(f'A senha para o acesso é "LIBERDADE{fatorial}".')

input("Pressione Enter para sair...")
    



