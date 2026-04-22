contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        print("Pulei o número 3!")
        continue
    print(f"Número válido: {contador}")
print("Contagem finalizada")