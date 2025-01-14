try:
    N1 = float(input("Insira um número decimal: "))
    funcaoInt = int(N1)
    print(funcaoInt)
except ValueError:
    print("O valor é inválido!")
finally:
    print("Programa encerrado.")