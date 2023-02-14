n1 = float(input('Digite um valor qualquer: '))
print(' ')
n2 = float(input('Digite outro valor qualquer: '))
print(' ')
n3 = float(input('Digite só mais um valor qualquer: '))
print(' ')

if n1 > n2 and n1 > n3:
    print('{} é o maior valor dentre os três.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior valor dentre os três'.format(n2))
else:
    print('{} é o maior valor dentre os três.'.format(n3))