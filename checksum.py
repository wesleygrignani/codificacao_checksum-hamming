# Desenvolvido por: Wesley Grignani
# Data: 26/03/2021
# Trabalho: Comunicação digital
# Questao 2: Codificação por checksum

import os 
import numpy as np
import main
from random import randint

def gera_numero(tam): # gerar numero aleatorio dentro de um limite
    return (randint(0, tam-1))


def soma_binario(num1, num2): 
# somar dois numeros binarios, retorna tambem o bit de carry 
    carry = 0
    soma = np.zeros(9)

    i = 8

    while i != -1:
        if(int(num1[i]) == 1 and int(num2[i]) == 1):
            if(carry == 1):
                soma[i] = 1
                carry = 1
            else:
                soma[i] = 0
                carry = 1
        else:
            soma[i] =  int(num1[i])+ int(num2[i]) + carry
            if(soma[i] == 2):
                soma[i] = 0
                carry = 1
            else:
                carry = 0

        i-= 1 

    return soma, carry


def receiver(dado_1, dado_2, dado_3, edc):
    # mostrando dados recebidos 
    os.system('cls')
    print("Dados recebidos no receiver: ")
    print("Mensagem 1: ", dado_1)
    print("Mensagem 2: ", dado_2)
    print("Mensagem 3: ", dado_3)
    print("EDC       : ", edc)
    os.system('pause')

    # realizando somas
    aux = str("000000001")

    # primeira soma
    soma, carry = soma_binario(dado_1, dado_2)
    while carry == 1:
        soma, carry = soma_binario(soma, aux)

    # segunda soma
    soma, carry = soma_binario(soma, dado_3)
    while carry == 1:
        soma, carry = soma_binario(soma, aux)

    # soma final com o EDC calculado pelo transceiver
    soma_final, carry = soma_binario(soma, edc)
    if (0 in soma_final):
        print("\nHouve erros na transmissao")
        print("Soma(MSG1 + MSG2 + MSG3) + edc: ", soma_final)
    else:
        print("\nNão Houve erros na transmissao")
        print("Soma(MSG1 + MSG2 + MSG3) + edc: ", soma_final)
    
    os.system('pause')
    main.main()


def caminho(msg1, msg2, msg3, edc):
# função que simula o meio de transmissao entre transceiver e receiver para injetar erros
    os.system('cls')
    escolha = int(input("""Deseja injetar erros em alguma mensagem?
1- Injetar erro aleatorio na mensagem 1
2- Injetar erro aleatorio na mensagem 2
3- Injetar erro aleatorio na mensagem 3
4- Não injetar erros
Escolha:"""))

    dado_1 = np.zeros(9)
    dado_2 = np.zeros(9)
    dado_3 = np.zeros(9)

    for i in range(len(msg1)):
        dado_1[i] = int(msg1[i])
        dado_2[i] = int(msg2[i])
        dado_3[i] = int(msg3[i])

    # Mostrando as mensagens sem injeção de erros 
    os.system('cls')
    print("Mensagem 1: ", dado_1)
    print("Mensagem 2: ", dado_2)
    print("Mensagem 3: ", dado_3)

    try:
        if escolha == 1: # Injetar erro na mensagem 1 
            tam = len(dado_1)
            pos = gera_numero(tam)
            dado_1[pos] = not dado_1[pos]
            print("-------------------")
            print("Mensagem 1 alterada: ", dado_1)
            print("Enviando para Receiver...")
            os.system('pause')
            receiver(dado_1,dado_2,dado_3,edc)

        elif escolha == 2: # Injetar erro na mensagem 2
            tam = len(dado_2)
            pos = gera_numero(tam)
            dado_2[pos] = not dado_2[pos]
            print("-------------------")
            print("Mensagem 2 alterada: ", dado_2)
            print("Enviando para Receiver...")
            os.system('pause')
            receiver(dado_1,dado_2,dado_3,edc)

        elif escolha == 3: # Injetar erro na mensagem 3 
            tam = len(dado_3)
            pos = gera_numero(tam)
            dado_3[pos] = not dado_3[pos]
            print("-------------------")
            print("Mensagem 3 alterada: ", dado_3)
            print("Enviando para Receiver...")
            os.system('pause')
            receiver(dado_1,dado_2,dado_3,edc)

        
        elif escolha == 4: # Não injetar erros
            print("Enviando para Receiver...")
            os.system('pause')
            receiver(dado_1,dado_2,dado_3,edc)

        
        else:
            print("Opção invalida !!")
            os.system('pause')
            caminho(msg1, msg2, msg3, edc)

    except ValueError:
        print("Opção invalida !!")
        os.system('pause')
        caminho(msg1, msg2, msg3, edc)

    

def transceiver(msg1, msg2, msg3):
    edc = np.zeros(9)
    aux = str("000000001")
    # primeira soma
    soma, carry = soma_binario(msg1, msg2)
    while carry == 1:
        soma, carry = soma_binario(soma, aux)

    # segunda soma
    soma, carry = soma_binario(soma, msg3)
    while carry == 1:
        soma, carry = soma_binario(soma, aux)

    for i in range(len(soma)):
        edc[i] = not soma[i]

    
    print("Soma calculada:",soma)
    print("EDC calculado: ",edc)
    print("Enviando para receiver...")
    os.system('pause') 
    caminho(msg1, msg2, msg3, edc)



def cod_checksum():
    os.system('cls')
    print("""Checksum:
    Insira as 3 mensagens de 9bits abaixo:""")

    msg1 = str(input("Mensagem 1: "))
    msg2 = str(input("Mensagem 2: "))
    msg3 = str(input("Mensagem 3: "))

    transceiver(msg1, msg2, msg3)

