# Desenvolvido por: Wesley Grignani
# Data: 26/03/2021
# Trabalho: Comunicação digital

import hamming
import checksum
import os

def main():
# menu criado para seleção de opçoes do trabalho
    try:
        os.system('cls')
        questao = int(input("""1 - Questao 1 (Hamming)
2 - Questao 2 (Checksum)
3 - Sair 
    Escolha: """))
        # codificação de hamming
        if questao == 1:
            os.system('cls')
            hamming.cod_hamming()

        # codificação por checksum
        elif questao == 2:
            os.system('cls')
            checksum.cod_checksum()

        elif questao == 3:
            os.system('cls')
            exit()

        else:
            print("Opção inválida. Tente novamente.\n")
            os.system('pause')
            main()

    except ValueError:
        print("Opção inválida. Tente novamente.\n")
        os.system('pause')
        main()
        


if __name__ == '__main__':
    os.system('cls')
    main()
    