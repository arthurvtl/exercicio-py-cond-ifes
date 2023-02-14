ano = int(input('Em que ano estamos? '))

n1 = str(input('Digite seu nome completo: '))
a1 = int(input('Digite o ano em que você nasceu: '))
print(' ')
print('=-'*100)
print(' ')
n2 = str(input('Digite seu nome completo: '))
a2 = int(input('Digite o ano em que você nasceu: '))
print(' ')

ip1 = ano - a1
ip2 = ano - a2

if ip1 > ip2:
    print('{} é mais velho.'.format(n1))
elif ip1 == ip2:
    print('{} e {} tem quase a mesma idade, apenas alguns meses de diferença'.format(n1,n2))
else:
    print('{} é mais velho'.format(n2))