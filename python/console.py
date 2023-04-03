print('Qual console?')

v1=input('Qual console você escolhe? PLAYSTATION, XBOX OU NINTENDO')
v2=input('Qual console você escolhe? PLAYSTATION, XBOX OU NINTENDO')
v3=input('Qual console você escolhe? PLAYSTATION, XBOX OU NINTENDO')
v4=input('Qual console você escolhe? PLAYSTATION, XBOX OU NINTENDO')
v5=input('Qual console você escolhe? PLAYSTATION, XBOX OU NINTENDO')

playstation=0
xbox=0
nintendo=0

if v1.upper() == 'PLAYSTATION':
    playstation=playstation + 1
elif v1.upper() == 'XBOX':
    xbox = xbox + 1
elif v1.upper() == 'NINTENDO':
    nintendo = nintendo + 1
else: print('O colaborador votou em um console Inesistente')

if v2.upper() == 'PLAYSTATION':
    playstation=playstation + 1
elif v2.upper() == 'XBOX':
    xbox = xbox + 1
elif v2.upper() == 'NINTENDO':
    nintendo = nintendo + 1
else: print('O colaborador votou em um console Inesistente')

if v3.upper() == 'PLAYSTATION':
    playstation=playstation + 1
elif v3.upper() == 'XBOX':
    xbox = xbox + 1
elif v3.upper() == 'NINTENDO':
    nintendo = nintendo + 1
else: print('O colaborador votou em um console Inesistente')

if v4.upper() == 'PLAYSTATION':
    playstation=playstation + 1
elif v4.upper() == 'XBOX':
    xbox = xbox + 1
elif v4.upper() == 'NINTENDO':
    nintendo = nintendo + 1
else: print('O colaborador votou em um console Inesistente')

if v5.upper() == 'PLAYSTATION':
    playstation=playstation + 1
elif v5.upper() == 'XBOX':
    xbox = xbox + 1
elif v5.upper() == 'NINTENDO':
    nintendo = nintendo + 1
else: print('O colaborador votou em um console Inesistente')

if playstation > xbox and playstation > nintendo:
    print('O GANHADOR É O PLAYSTATION, COM UM TOTAL DE {} VOTOS \n Xbox: {} \n Nintendo: {}'.format(playstation,xbox,nintendo))
elif xbox > playstation and xbox > nintendo:
    print('O GANHADOR É O XBOX, COM UM TOTAL DE {} VOTOS \n playstation: {} \n Nintendo: {}'.format(xbox,playstation,nintendo))
elif nintendo > playstation and nintendo > xbox:
     print('O GANHADOR É O NINTENDO, COM UM TOTAL DE {} VOTOS \n playstation: {} \n Xbox: {}'.format(nintendo,playstation,xbox))
else: 
    print('O GANHADOR É INCONCLUSIVO')