a1 = int(input('Digite o valor do ângulo 1: '))
print(' ')
a2 = int(input('Digite o valor do ângulo 2: '))
print(' ')
a3 = int(input('Digite o valor do ângulo 3: '))
print(' ')

# VERIFICANDO EXISTENCIA

if a1 + a2 + a3 == 180:
    print('Ele é um triângulo')
    if a1 < 90 or a2 < 90 or a3 < 90:
        print('Triângulo acutângulo')

    elif a1 == 90 or a2 == 90 or a3 == 90:
        print('Triângulo Retângulo')

    elif a1 > 90 or a2 > 90 or a3 > 90:
        print('Triângulo obstângulo')

else:
    print('Não é um tiângulo')