nom = str(input('Qual seu nome?: '))
print(' ')
n1 = float(input('Digite o valor da sua primeira nota: '))
print(' ')
n2 = float(input('Digite o valor da sua segunda nota: '))
print(' ')

m = n1+n2/2

if 0 <=  m < 5:
    print('{}, você está reprovado'.format(nom))
elif 5 <= m <= 7:
    print('{}, você está de recuperação.'.format(nom))
else:
    print('{}, você está aprovado!'.format(nom))