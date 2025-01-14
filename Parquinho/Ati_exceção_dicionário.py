try:
    dicionario = {
        "um" : 1,
        "dois" : 2,
        "tres" : 3 
    }
    buscar = input("Encontre a chave: ")
    checa_valor = dicionario[buscar]
    print("Chave encontrada!")
except KeyError:
    print("Chave não encontrada ou inexistente!")
finally:
    print("Programa encerrado.")