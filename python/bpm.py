print ('Taxa de BPM')

idade=float(input('Informe sua idade: '))
bpm=float(input('Informe seu BPM: '))

if idade <= 2:
    if bpm < 120:
        print('Seu BPM encontra-se abaixo do indicado')
    elif bpm > 146:
        print('Seu BPM encontra-se acima do indicado')    
    else:
        
        print('Seu BPM encontra-se no total indicado')    
elif idade >= 8 and idade <= 17:
    if bpm < 80:
        print('Seu BPM encontra-se abaixo do indicado')
    elif bpm > 100:
        print('Seu BPM encontra-se acima do indicado')    
    else:
        print('Seu BPM encontra-se no total indicado')        
elif idade >= 18 and idade <= 59:
    if bpm < 70:
        print('Seu BPM encontra-se abaixo do indicado')
    elif bpm > 80:
        print('Seu BPM encontra-se acima do indicado')    
    else:
        print('Seu BPM encontra-se no total indicado')
else:
    if bpm < 50:
        print('Seu BPM encontra-se abaixo do indicado')
    elif bpm > 60:
        print('Seu BPM encontra-se acima do indicado')    
    else:
        print('Seu BPM encontra-se no total indicado')         