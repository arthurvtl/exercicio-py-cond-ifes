tp = str(input('Digite o qual seu tipo de consumidor (I, C ou R): '))
consumo = float(input('Digite qual foi o seu consumo mensal: '))
c1 = "I"
c2 = "C"
c3 = "R"

#Condições
if (tp == c1):
    valor = (0.68 * consumo) + 34
    print('O valor da conta mensal de energia é R${}'.format(valor))
elif (tp == c2):
    valor = (0.37 * consumo) + 45
    print('O valor da conta mensal de energia é R${}'.format(valor))
elif (tp == c3):
    valor = (0.77 * consumo) - 22
    print('O valor da conta mensal de energia é R${}'.format(valor))