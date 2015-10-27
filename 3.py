from decimal import Decimal, getcontext
summa=int(input('Введите размер предоставляемого кредита'))
stavka=int(input('Введите процентную ставку'))
goda=int(input('Введите количество лет'))
n=goda*12
getcontext().prec = 2
k=stavka/1200
platyog=summa*(k+k/(((1+k)**n)-1))
platyog=1*Decimal(platyog)
print(Decimal(platyog))



