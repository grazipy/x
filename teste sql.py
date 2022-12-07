import requests
from tkinter import *
import math

def consulta_de_licitação():
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
    
janela = Tk()
janela.title("Licitações")

texto_orientacao = Label(janela, text= "Clique no botão para consultar suas licitações")
texto_orientacao. grid(column=0, row=0)

botao = Button(janela, text="Licitações", command=consulta_de_licitação)
botao.grid(column=0, row=1)

janela.mainloop()
