palavra = input(":")
for letra in palavra:
    print("_", end=" ")

print("\n")

resposta = ["_"] * len(palavra)
tentativa = input("Coloque uma letra:")
for i, letra in enumerate(palavra):
    if letra == tentativa:
        resposta[i] = letra
resultado = " ".join(resposta)
print(resultado)

        

