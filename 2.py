d1 = float(input('Digite a distância que o carro um percorreu: '))
v1 = float(input('Digite a velocidade do carro um: '))

print(' ')

d2 = float(input('Digite a distância que o carro dois percorreu: '))
v2 = float(input('Digite a velocidade do carro dois: '))

print(' ')

vm1 = d1/v1
vm2 = d2/v2

if vm1 > vm2:
    print('O carro um tem a velocidade média maior.')
elif vm1 == vm2:
    print('Os dois carros tem a mesma velocidade média.')
else:
    print('O carro dois tem a maior velocidade média.')