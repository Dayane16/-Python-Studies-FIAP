import math
print('Descubra formula de Baskhara!')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = b * b - 4 * a * c

if delta>0.0:
    x1= (-b + math.sqrt(delta)) / (2 * a)
    x2= (-b - math.sqrt(delta)) / (2 * a)
    print('O valor de delta é {}, o valor de x1 é {} e o valor de x2 é {}'.format(delta,x1,x2))
elif delta==0.0:
    x= (-b - math.sqrt(delta)) / (2 * a)
    print('O valor de delta é {}, o valor de x1 é {}, não possui outro valor para x'.format(delta,x))
else:
    print('Não possui valor de X, porém este é o valor de delta {}'.format(delta))
    