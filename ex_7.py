opc = int(input("1-cad \n2-alt \n3-exc \n4-sair"))

match opc:
    case 1:
        print("Cadastrar")
    case 2: 
        print("Alterar")
    case 3:
        print("Excluir")
    case 4:
        print("Sair")
    case _:
        print("Valor errado")