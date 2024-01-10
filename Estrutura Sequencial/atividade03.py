#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def main():

    nota1 = float(input("Nota 1: \n"))
    nota2 = float(input("Nota 2: \n"))
    nota3 = float(input("Nota 3: \n"))
    nota4 = float(input("Nota 4: \n"))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"A média das notas é: {media}")

    return 0
if __name__ == "__main__":
    main()