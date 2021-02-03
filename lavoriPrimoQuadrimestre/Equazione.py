a= int(input("inserisci il coefficiente con la x elevato alla seconda: "))

b= int(input("inserisci il coefficiente con la x: "))

c= int(input("inserisci il coefficiente del termine noto :"))


import math
def eq2grado(a,b,c):
    delta=(b*b)-(4*a*c)
    if delta < 0:
        return "non esistono soluzioni"
    else:
        valsomma=(-b + math.sqrt(delta))/(2*a)
        valdifferenza=(-b - math.sqrt(delta))/(2*a)
        return valsomma,valdifferenza

print(eq2grado(a,b,c))
