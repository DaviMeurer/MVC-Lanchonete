try:
    N1, N2 = float(input("Digite um valor válido: ")), float(input("Digite outro valor válido: "))
    resultado = N1 / N2
    print (resultado)
except ZeroDivisionError:
    print ("Não é possível dividir por zero!")
finally:
    print ("Programa encerrado.")

