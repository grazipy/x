if __name__ == "__main__":
    largura = int(input("digite a largura: "))
    altura = int(input("Digite a altura: "))

print(largura * "#")

while altura > 2:
    print("#" + (largura - 2) * " " + "#")
    altura -= 1

print(largura * "#")
