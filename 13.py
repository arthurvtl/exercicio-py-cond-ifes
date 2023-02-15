a = float(input('Digite quantas hastes de aço quer comprar: '))
c = float(input('Digite quantas hastes de cobre deseja comprar: '))
al = float(input('Digite quantas hastes de aluminio deseja comprar: '))

valorA = a * 2.5
valorC = c * 4.0
valorAl = al * 5.0

qtdTotal = a + c + al

if qtdTotal < 6:
    valorTotal = (valorA * 1) + (valorC * 1) + (valorAl * 1)
    print('O valor total da compra é de R${}'.format(valorTotal))

elif qtdTotal <= 15:
    valorTotal = (valorA * 0.9) + (valorC * 0.9) + (valorAl * 0.9)
    print("O valor total da compra deu R${}".format(valorTotal))

elif qtdTotal <= 20:
    valorTotal = (valorA * 0.85) + (valorC * 0.85) + (valorAl * 0.85)
    print("O valor total da compra deu R${}".format(valorTotal))

elif qtdTotal > 20:
    valorTotal = (valorA * 0.80) + (valorC * 0.80) + (valorAl * 0.80)
    print("O valor total da compra deu R${}".format(valorTotal))
