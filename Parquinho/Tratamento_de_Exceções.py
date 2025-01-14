try:
    num = int(input("Digite um número: "))
    result = 10 / num
    print("resultado é:", result)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Entrada inválida! Por favor,"+"insira um número inteiro.")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    print("Bloca finally executado.")