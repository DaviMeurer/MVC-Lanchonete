try:
    N1 = float(input("Digite um número válido: "))
    resultado = N1 / 100
    print(resultado)
except:
    print("Erro no programa!")
finally:
    print("\nPrograma encerrado.")