from datetime import datetime

try:
    data = input("Digite uma data válida (dia/mês/ano): ")
    valida_data = datetime.strptime(data, "%d/%m/%Y")
    print("Data válida!")
except ValueError:
    print("Data inválida!")
finally:
    print("Programa encerrado.")