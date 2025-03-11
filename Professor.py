import os

#Limpando tela
os.system("cls")

#Passo 1 - Entrada
nome = input("Nome do professor: ")
nivel = int(input("Nível do professor: "))
aulas = int(input("Quantidade de aulas semanais: "))

#Passo 2 - Processo

if(nivel == 1):
    salario = (12 * aulas) * 4

elif(nivel == 2):
    salario = (17 * aulas) * 4

else:
    salario = (25 * aulas) * 4

#Passo 3 - Saída

os.system("cls")

print("----- PERFIL FINAL ----- \n")
print("Nome do professor: ", nome)
print("Nível do professor: ", nivel)
print("Salario mensal: ", salario , "reais")