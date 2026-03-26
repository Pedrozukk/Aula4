soma = 0 
cont = 0 

while True: 
    n = int(input("Digite o n: "))
    if n == 0:
        break
    soma += n
    cont += 1

if cont > 0:
    print(f"Média {soma / cont}" )
else: 
    print("Sem media")