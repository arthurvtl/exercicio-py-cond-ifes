m = float(input('Digite o valor da sua média: '))
print(' ')
f = float(input('Digite quantas faltas você tem: '))
print(' ')

if m >= 7 and f <= 32: # TUDO OK
    print('Aprovado')
elif m < 7 and f <= 32: # MEDIA BAIXA
    print('Reprovado')
elif m < 7 and f > 32: # MEDIA BAIXA E MUITAS FALTAS
    print('Reprovado') 
else:
    print('Reprovado')