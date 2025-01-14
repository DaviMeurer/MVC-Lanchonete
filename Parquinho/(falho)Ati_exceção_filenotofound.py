try:
    endereco = input("Coloque o endereço de um arquivo: ")
    with open (endereco, 'r') as arquivo:
        print("Endereço encontrado!")
except (FileNotFoundError, IOError):
    print("Endereço não encontrado ou inexistente!")
finally:
    print("Programa encerrado.")