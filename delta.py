import math

def delta(a,b,c):
    return b** 2 - 4* a* c

def main():
    a = float(input("digite o valor de a: "))
    b = float(input("digite o valor de b: "))
    c = float(input("digite o valor de c: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a,b,c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d))/(2*a)
        print("a unica raiz é', raiz1")
        
    else:
        if d <0:
            print("esta equção não possui raizes reais")
        else:
            raiz1 = (-b + math.sqrt(d))/(2*a)
            raiz2 = (-b - math.sqrt(d))/(2*a)
            print("A primeia raiz é : ", raiz1)
            print("A segunda raiz é : ", raiz2)
