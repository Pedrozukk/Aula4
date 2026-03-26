def faixa_etaria(idade):
    if idade <= 0:
        return "idade inválida"
    elif idade < 12:
        return "criança"
    elif idade < 17:
        return "adolescente"
    else: 
        return "adulto"

while True:
    idade = input("Digite a idade ou SAIR: ")
    if idade.lower() == "sair":
        break
    print(faixa_etaria(int(idade)))

print("Até mais...")