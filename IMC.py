import os

#Limpando tela
os.system("cls")

#Passo 1 - Entrada

nome = input("Nome da pessoa: ")
peso = float(input("Peso da pessoa: "))
altura = float(input("Altura da pessoa: "))

#Passo 2 - Processo

IMC = peso / (altura * altura)

if(IMC <= 16.9):
    classificacao = "muito abaixo do peso"

elif(IMC == 17 or IMC <= 18.4):
    classificacao = "abaixo do peso"

elif(IMC == 18.5 or IMC <= 24.9):
    classificacao = "peso normal"

elif(IMC == 25 or IMC <= 29.9):
    classificacao = "acima do peso"

elif(IMC == 30 or IMC <= 34.9):
    classificacao = "obesidade grau I"

elif(IMC == 35 or IMC <= 40):
    classificacao = "obesidade grau II"

else:
    classificacao = "obesidade grau III"

#Passo 3 - Saída

os.system("cls")

print("=========== FICHA DO PACIENTE =========== \n")
print("Nome: ", nome)
print("Peso: ", peso)
print("Altura: ", altura)
print("IMC: ", round(IMC, 2) , ", classificado como" , classificacao)