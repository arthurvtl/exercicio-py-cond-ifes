sexo = str(input('Qual seu sexo? (masculino ou feminino): '))
print(' ')
peso = float(input('Digite seu peso: '))
print(' ')
altura = float(input('Digite sua altura em cm: '))
print(' ')
idade = float(input('Digite sua idade: '))
print(' ')

cDH = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
cDM = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

if sexo == 'masculino':
    cDH = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    print('{} é a quantidade ideal de calorias que você precisa ingerir diáriamente.'.format(cDH))

else:
    cDM = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    print('{} é a quantidade ideal de calorias que você precisa ingerir diáriamente'.format(cDM))

