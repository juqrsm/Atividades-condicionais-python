import os

#Limpando tela
os.system ("cls")

#Passo 1 - Entrada

produto = input("Digite o produto a ser comprado: ")
preco = float(input("Preço da unidade: "))
quantidade = int(input("Quantidade de unidades: "))

#Passo 2 - Processo 

valor = preco * quantidade

if(quantidade <= 5):
    desconto = preco - (preco * 0.2)

elif(quantidade > 5 or quantidade <= 10):
    desconto = preco - (preco * 0.3)

else:
    desconto = preco - (preco * 0.5)

#Passo 3 - Saída

os.system("cls")

print("---------- FINALIZAÇÃO DA COMPRA ----------")
print("Item a ser comprado: " , produto)
print("Quantidade de unidades: " , quantidade)
print("Preço sem desconto: " , valor)
print("Preço total: " , valor - desconto)