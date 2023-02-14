sb = float(input('Digite o valor do seu salário bruto: '))

i1 = 0
sl1 = sb - i1

i2 = (sb * 0.075) - 142.80
sl2 = sb - i2

i3 = (sb * 0.15) - 548.82
sl3 = sb - i3

i4 = (sb * 0.225) - 636.13
sl4 = sb - i4

i5 = (sb * 0.275) - 869.36
sl5 = sb - i5

if sb > 4664.68:
    print('O valor do seu salário bruto é de R${:.2f}, você paga R${:.2f} de imposto e por fim, seu salário líquido é de R${:.2f}'.format(sb,i5,sl5))

elif 4664.68 < sb <= 3751.06:
    print('O valor do seu salário bruto é de R${:.2f}, você paga R${:.2f} de imposto e por fim, seu salário líquido é de R${:.2f}'.format(sb,i4,sl4))

elif 3751.05 < sb <= 2826.66:
    print('O valor do seu salário bruto é de R${:.2f}, você paga R${:.2f} de imposto e por fim, seu salário líquido é de R${:.2f}'.format(sb,i3,sl3))

elif 2826.65 < sb <= 1903.99:
    print('O valor do seu salário bruto é de R${:.2f}, você paga R${:.2f} de imposto e por fim, seu salário líquido é de R${:.2f}'.format(sb,i2,sl2))

else:
    print('Você é isento de taxas.')



