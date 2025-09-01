# Primeiro desafio da aula 01
nome = input("Qual seu nome? ")

contador = 0
for i in nome:
    contador = contador +1

print("Seu nome tem " + str(contador) + " letras.")
print("Olá, " + nome + "!")

# Segundo desafio da aula 01
num2 = input("Digite outro número: ")
num1 = input("Digite um número: ")
print("A soma dos números é: " + str(int(num1) + int(num2)))

# Desafio final da aula 01
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")
print("Por favor, responda as perguntas a seguir:")
salario = int(input("Digite seu salário: "))
bonus = float(input("Digite o bônus em porcentagem: "))
salario_bonus = salario + 1000 + (salario * int(bonus) / 100)
print(nome + ", seu salário com bônus é: " + str(salario_bonus))