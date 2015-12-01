#Машина дает сотню, но реальный предел 5(переходим к пределу в рекуррентном соотношении, получаем три корня: 3, 5, 100, по индукции доказываем, что все члены меньше 5, следовательно 100 - не предел. Машина считает неправильно т. к. начиная с некоторого члена последовательности машина округляет неправильно и получает нереальное значение)
from fractions import Fraction
def nchlen(g):
    if g==1:
        return 4
    if g==2:
        return 4.25
    if g==3:
        xn_1=4
        xn_2=4.25
        return 108-Fraction(Fraction(815-Fraction(1500,Fraction(xn_1))),Fraction(xn_2))
    return 108-Fraction(Fraction(815-Fraction(1500,Fraction(nchlen(g-2)))),Fraction(nchlen(g-1)))
f=nchlen(int(input('Введите номер члена последовательности')))
print(f,eval(str(f)))

