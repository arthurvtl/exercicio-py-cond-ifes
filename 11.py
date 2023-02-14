a = int(input('Digite o ano: '))
m = int(input('Digite o mês: '))


if m in [1, 3, 5, 7, 8, 10, 12]:
        print('31')

elif m in [4, 6, 9, 11]:
        print('30')

elif m == 2:

     if a%4 == 0:
            print('29')

     else:
        print('28')


        