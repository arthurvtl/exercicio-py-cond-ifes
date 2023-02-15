w = float(input("Digite o valor de W: "))
z = float(input("Digite o valor de Z: "))


if (w > 0 and z < 7):
    x = ((5*w) + 1) / 3
    t = (5*z) + 2
    print("Primeira condição")
else:
    x = (5*z) + 2
    t = ((5*w) + 1) / 3
    print("Segunda condição")


y = ( ((7*x)**3) - ((3*x)**0.5) - (8*t) ) / ( 5 * (x + 1))
print("O resultado da equação é: {:.2f}".format(y))