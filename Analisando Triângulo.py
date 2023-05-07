c1 = float(input("Digite o comprimento de um segmento de reta: "))
c2 = float(input("Digite o comprimento de um segmento de reta: "))
c3 = float(input("Digite o comprimento de um segmento de reta: "))
if (c2 - c3) < c1 < (c2 + c3) and (c1 - c3) < c2 < (c1 + c3) and (c1 - c2) < c3 < (c1 + c2):
    print("Esses segmentos de reta podem formar um triângulo")
else:
    print("Esses segmentos de reta não podem formar um triângulo")