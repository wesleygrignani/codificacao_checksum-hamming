# Desenvolvido por: Wesley Grignani
# Data: 26/03/2021
# Trabalho: Comunicação digital
# Questao 1 - Codificação Hamming


import os
import main
import numpy as np
from random import randint

def cod_hamming():
    os.system('cls')
    escolha = int(input("""Codificação Hamming:   
           1 - Utilizar codigo de aluno 6495621 (13,9)
           2 - Utilizar Hamming (12,8)
           3 - Retornar ao menu
           Escolha: """))
    try:
        if escolha == 1:
            hamming13_9()
        elif escolha == 2:
            hamming12_8()
        elif escolha == 3:
            os.system('cls')
            main.main()
        else:
            print("Opção inválida. Tente novamente.\n")
            os.system('pause')
            cod_hamming()
    except ValueError:
        print("Opção inválida. Tente novamente.\n")
        os.system('pause')
        cod_hamming()

def gera_numero(tam):
    return (randint(0, tam-1))


# inversor de um bit na mensagem 
def injetor_erro(mensagem):
    qnt = int(input("Quantidade de erros: "))
    # tam = len(mensagem)
    # aux = 15

    for i in range(qnt):
        # pos = gera_numero(tam)

        # while pos == aux:
        #     pos = gera_numero(tam)

        # mensagem[pos] = not mensagem[pos]
        # aux = pos
        pos = int(input("Qual posição trocar: "))
        mensagem[pos-1] = not mensagem[pos-1]

    return mensagem


def corrigi_inversao(msg, k):
    pos = 0
    for i in range(len(k)):
        if(k[i] == 1):
            if(i == 0):
                pos += 1
            elif(i == 1):
                pos += 2
            elif(i == 2):
                pos += 4
            else:
                pos += 8
    msg[pos - 1] = not msg[pos - 1] 
    print("Erro detectado e corrigido na posição:", pos)
    print("Retornando para receiver...")
    os.system('pause')
    return msg


def receiver(msg):
# receiver responsavel por verificar algum erro na mensagem 
# detecta 1 erro e corrigi 
# detecta 2 erros mas nao corrigi
    os.system('cls')

    if (len(msg) == 12):
        k = np.zeros(4)
        k[0] = int(msg[0]) ^ int(msg[2]) ^ int(msg[4]) ^ int(msg[6]) ^ int(msg[8]) ^ int(msg[10])
        k[1] = int(msg[1]) ^ int(msg[2]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[9]) ^ int(msg[10])
        k[2] = int(msg[3]) ^ int(msg[4]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[11])
        k[3] = int(msg[7]) ^ int(msg[8]) ^ int(msg[9]) ^ int(msg[10]) ^ int(msg[11])

        p = int(msg[0]) ^ int(msg[1]) ^ int(msg[2]) ^ int(msg[3]) ^ int(msg[4]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[7]) ^ int(msg[8]) ^ int(msg[9]) ^ int(msg[10]) ^ int(msg[11]) 

        if (p == 0 and (1 in k)):
            print("Dois ou erros detectados") 
            os.system('pause')
            main.main()
        elif(1 in k):
            print("Mensagem: ", msg)
            print("Houve 1 erro na posição em binario:", k)
            print("Corrigindo inversão de bit...")
            os.system('pause')
            msg = corrigi_inversao(msg, k)
            print("Correção efetuada, mensagem: ", msg)
            os.system('pause')
            main.main()
        else:
            print("Não houve erros na transmissão")
            print("Mensagem: ", msg)
            print(k)
            os.system('pause')
            main.main()
    else:
        k = np.zeros(4)
        k[0] = int(msg[0]) ^ int(msg[2]) ^ int(msg[4]) ^ int(msg[6]) ^ int(msg[8]) ^ int(msg[10]) ^ int(msg[12])
        k[1] = int(msg[1]) ^ int(msg[2]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[9]) ^ int(msg[10])
        k[2] = int(msg[3]) ^ int(msg[4]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[11]) ^ int(msg[12])
        k[3] = int(msg[7]) ^ int(msg[8]) ^ int(msg[9]) ^ int(msg[10]) ^ int(msg[11]) ^ int(msg[12])

        p = int(msg[0]) ^ int(msg[1]) ^ int(msg[2]) ^ int(msg[3]) ^ int(msg[4]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[7]) ^ int(msg[8]) ^ int(msg[9]) ^ int(msg[10]) ^ int(msg[11]) ^ int(msg[12])

        if (p == 0 and (1 in k)):
            print("Dois erros detectados") 
            os.system('pause')
            main.main()
        elif(1 in k):
            print("Mensagem: ", msg)
            print("Houve 1 erro na posição em binario:", k)
            print("Corrigindo inversão de bit...")
            os.system('pause')
            msg = corrigi_inversao(msg, k)
            print("Correção efetuada, mensagem: ", msg)
            os.system('pause')
            main.main()
        else:
            print("Não houve erros na transmissão")
            print("Mensagem: ", msg)
            print(k)
            os.system('pause')
            main.main()
    



# funcao que recebe a mensagem e possui a opçao de injecação de erro para simular quando for enviado ao receiver
def transceiver(mensagem):
    os.system('cls')
    print("Dado pronto para ser enviado pelo transceiver: ",mensagem)
    escolha = int(input(("""1- Simular injeçao de erros
2- Enviar mensagem como esta
Escolha:""")))
    try:        
        if escolha == 1:
            os.system('cls')
            print("Mensagem anterior:        ", mensagem)
            mensagem = injetor_erro(mensagem)
            print("Mensagem com bit alterado:", mensagem)
            print("Enviando para receiver...")
            os.system('pause')
            # enviando para o receiver
            receiver(mensagem)

        elif escolha == 2:
            print("\nEnviando para receiver...")
            os.system('pause')
            # enviando para o receiver
            receiver(mensagem)

        else:
            print("Opção invalida!!")
            os.system('pause')
            transceiver(mensagem)
    except ValueError:
        print("Opção invalida!!")
        os.system('pause')
        transceiver(mensagem)


def hamming13_9():
    # funcao para hamming com codigo do aluno 6495621 9bits 
    os.system('cls')
    msg = str(input("Insira a mensagem de 9bits aqui: "))
    if(len(msg) != 9):
        print("Voce deve inserir uma mensagem com 9bits")
        os.system('pause')
        hamming13_9()
    else:
        data = np.zeros(13)
        # calculo dos bits de paridade
        data[0] = int(msg[0]) ^ int(msg[1]) ^ int(msg[3]) ^ int(msg[4]) ^ int(msg[6]) ^ int(msg[8])
        data[1] = int(msg[0]) ^ int(msg[2]) ^ int(msg[3]) ^ int(msg[5]) ^ int(msg[6])              
        data[2] = msg[0] 
        data[3] = int(msg[1]) ^ int(msg[2]) ^ int(msg[3]) ^ int(msg[7]) ^ int(msg[8]) 
        data[4] = msg[1]
        data[5] = msg[2]
        data[6] = msg[3]
        data[7] = int(msg[4]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[7]) ^ int(msg[8]) 
        data[8] = msg[4]
        data[9] = msg[5]
        data[10] = msg[6]
        data[11] = msg[7]
        data[12] = msg[8]
        # enviar mensagem para o transceiver
        transceiver(data)



def hamming12_8():
    # funcao para hamming de mensagem 8bits 
    os.system('cls')
    msg = str(input("Insira a mensagem de 8bits aqui: "))
    if(len(msg) != 8):
        print("Voce deve inserir uma mensagem com 8bits")
        os.system('pause')
        hamming12_8()
    else:
        data = np.zeros(12)
        # calculo dos bits de paridade
        data[0] = int(msg[0]) ^ int(msg[1]) ^ int(msg[3]) ^ int(msg[4]) ^ int(msg[6])
        data[1] = int(msg[0]) ^ int(msg[2]) ^ int(msg[3]) ^ int(msg[5]) ^ int(msg[6])              
        data[2] = msg[0] 
        data[3] = int(msg[1]) ^ int(msg[2]) ^ int(msg[3]) ^ int(msg[7])
        data[4] = msg[1]
        data[5] = msg[2]
        data[6] = msg[3]
        data[7] = int(msg[4]) ^ int(msg[5]) ^ int(msg[6]) ^ int(msg[7])
        data[8] = msg[4]
        data[9] = msg[5]
        data[10] = msg[6]
        data[11] = msg[7]
        # enviar mensagem para o tranceiver
        transceiver(data)





