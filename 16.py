num = float(input("Digite um número de 3 dígitos: "))

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
sd = cen + dez + uni
mult = sd % 4

if (sd == 1 or sd == 2 or sd == 4 or sd == 8 or sd == 16):
    if(mult == 0):
        print("O número é divisor de 16 e múltiplo de 4 ao mesmo tempo.")
else:
    print("O número não é divisor de 16 e múltiplo de 4 ao mesmo tempo.")