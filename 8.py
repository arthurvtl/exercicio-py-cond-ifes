km = float(input('Digite quantos km foram percorridos: '))
l = float(input('Digite quantos litros de gasolina foram consumidos: '))

kmL = km/l

if kmL < 8:
    print('Venda o carro!')
elif 8 <= kmL <= 14:
    print('Econômico!')
elif kmL > 12:
    print('Super econômico!')