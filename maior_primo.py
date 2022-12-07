def éPrimo(n):
    i = n - 1
    while i > 0:
        if i == 1:
            return True
            break
        elif (n%i == 0):
            return False
            break
        else:
            i -= 1

def maior_primo(x):
    while x > 0:
        if éPrimo(x) == True:
            return x
            break
        else:
            x -= 1
            return x
