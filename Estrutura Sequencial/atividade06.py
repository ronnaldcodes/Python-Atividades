#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def main():

    #declaração de variáveis
    l = 0
    area = 0
    dobro_area = 0

    #entrada de dados
    l = float(input("Digite o valor do lado do quadrado: \n"))

    #processamento de dados
    area = l**2
    dobro_area = area * 2

    #saída de dados
    print(f'A área do quadrado é: {area}')
    print(f'O dobro da área é: {dobro_area}')

    return 0
if __name__ == '__main__':
    main()