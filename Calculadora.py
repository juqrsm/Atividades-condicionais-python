import os

#Limpando tela
os.system("cls")

#Passo 1

sinal = input("Tipo de conta (subtração, divisão etc.): ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("DIgite o segundo número: "))

#Passo 2

soma = n1 + n2
divisao = n1 / n2
multiplicacao = n1 * n2
subtracao = n1 - n2 

#Passo 3

if(sinal == "soma"):
    print("O resultado da equação é: ", soma)
    print("Tipo de conta realizada: ", sinal)

elif(sinal == "subtração"):
    print("O resulatdo da equação é: ", subtracao)
    print("Tipo de conta realizada: ", sinal)

elif(sinal == "multiplicacao"):
    print("O resulatdo da equação é: ", multiplicacao)
    print("Tipo de conta realizada: ", sinal)

else:
    print("O resulatdo da equação é: ", divisao)
    print("Tipo de conta realizada: ", sinal)