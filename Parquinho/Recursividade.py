def calcular_fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*calcular_fatorial(n-1)

try:
    n=int(input("Digite o fatorial: "))
    resultado = calcular_fatorial(n)
    print(resultado)
except ValueError:
    print("Valor inválido!")
except RecursionError:
    print("Resultado muito grande!")
finally:
    print("\nPrograma encerrado.")