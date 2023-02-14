sexo = str(input('Digite o seu sexo (masculino ou feminino: )'))
idade = int(input('Digite sua idade: '))

if sexo == 'masculino':
    if idade > 18:
        print('Maior de idade')
    else:
        print('Menor de idade')
else:
    if idade > 21:
        print('Maior de idade')
    else:
        print('Menor de idade')