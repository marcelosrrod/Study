## Inteiros - Exercício 01
n1_e1 = int(input("Digite o primeiro número: "))
n2_e1 = int(input("Digite o segundo número: "))
soma_e1 = n1_e1 + n2_e1
print(f"A soma entre {n1_e1} e {n2_e1} é igual a {soma_e1}")

## Inteiros - Exercício 02
n1_e2 = input("Digite um número: ")
resto_divisao_e2 = int(n1_e2) % 5
print(f"O resto da divisão de {n1_e2} por 5 é igual a {resto_divisao_e2}")

## Inteiros - Exercício 03
n1_e3 = int(input("Digite um número: "))
n2_e3 = int(input("Digite outro número: "))
produto_e3 = n1_e3 * n2_e3
print(f"O produto entre {n1_e3} e {n2_e3} é igual a {produto_e3}")

## Inteiros - Exercício 04
n1_e4 = int(input("Digite um número inteiro: "))
n2_e4 = int(input("Digite outro número inteiro: "))
divisao_e4 = n1_e4 // n2_e4
print(f"A divisão inteira entre {n1_e4} e {n2_e4} é igual a {divisao_e4}")

## Inteiros - Exercício 05
n1_e5 = int(input("Digite um número: "))
quad_n1_e5 = n1_e5 ** 2
print(f"O quadrado de {n1_e5} é igual a {quad_n1_e5}")

## --------------------------------------------------------------------------------##

## Números de ponto flutuante - Exercício 06
n1_e6 = float(input("Digite um número: "))
n2_e6 = float(input("Digite outro número: "))
soma_e6 = n1_e6 + n2_e6
print(f"A soma entre {n1_e6} e {n2_e6} é igual a {soma_e6}")

## Números de ponto flutuante - Exercício 07
n1_e7 = float(input("Digite um número: "))
n2_e7 = float(input("Digite outro número: "))
media_r7 = (n1_e7 + n2_e7) / 2
print(f"A média entre {n1_e7} e {n2_e7} é igual a {media_r7}")

## Números de ponto flutuante - Exercício 08
n1_e8 = float(input("Digite o número da base para exponenciação: "))
n2_e8 = float(input("Digite o número do expoente para exponenciação: "))
exp_e8 = n1_e8 ** n2_e8
print(f"O resultado de {n1_e8} elevado a {n2_e8} é igual a {exp_e8}")

## Números de ponto flutuante - Exercício 09
celsius_e9 = float(input("Digite a temperatura em Celsius: "))
fahrenheit_e9 = (celsius_e9 * 9/5) + 32
print(f"{celsius_e9}°C é igual a {fahrenheit_e9}°F")

## Números de ponto flutuante - Exercício 10
raio_e10 = float(input("Digite o raio do círculo: "))
area_e10 = 3.14159 * (raio_e10 ** 2)
print(f"A área do círculo com raio {raio_e10} é igual a {area_e10:.2f}")

## --------------------------------------------------------------------------------##

## Strings - Exercício 11
texto_e11 = input("Digite uma frase: ")
print(f"A frase digitada foi: {texto_e11.upper()}")

## Strings - Exercício 12
nome_e12 = input("Digite seu nome completo: ")
print(f"Seu nome em letras minúsculas é: {nome_e12.lower()}")

## Strings - Exercício 13
texto_e13 = input("Digite uma frase: ")
print(f"{texto_e13.strip()}")

## Strings - Exercício 14
data_e14 = input("Digite uma data no formato DD/MM/AAAA ou DD de MMMM de AAAA: ")
dia_e14, mes_e14, ano_e14 = data_e14.split('/' or 'de')
print(f"Dia: {dia_e14}, Mês: {mes_e14}, Ano: {ano_e14}")

## Strings - Exercícios 15
frase_e15 = input("Digite uma frase: ")
frase_2_e15 = input("Digite outra frase: ")
concatenacao_e15 = frase_e15 + " " + frase_2_e15
print(f"A concatenação das frases é: {concatenacao_e15}")

## --------------------------------------------------------------------------------##

## Booleanos - Exercício 16
escolha_e16 = bool(input("Digite TRUE ou FALSE: "))
escolha_2_e16 = bool(input("Digite TRUE ou FALSE: "))
combinacao_e16 = escolha_e16 and escolha_2_e16
print(f"O resultado da combinação lógica entre as duas escolhas é: {combinacao_e16}")

## Booleanos - Exercício 17
escolha_e17 = bool(input("Digite TRUE ou FALSE: "))
escolha_2_e17 = bool(input("Digite TRUE ou FALSE: "))
combinacao_e17 = escolha_e17 or escolha_2_e17
print(f"O resultado da combinação lógica entre as duas escolhas é: {combinacao_e17}")

## Booleanos - Exercício 18
escolha_e18 = bool(input("Digite TRUE ou FALSE: "))
negacao_e18 = not escolha_e18
print(f"O resultado da negação da escolha é: {negacao_e18}")

## Booleanos - Exercício 19
n1_e19 = int(input("Digite um número inteiro: "))
n2_e19 = int(input("Digite outro número inteiro: "))
comparacao_e19 = n1_e19 == n2_e19
print(f"O resultado da comparação entre os dois números é: {comparacao_e19}")

## Booleanos - Exercício 20
n1_e20 = int(input("Digite um número inteiro: "))
n2_e20 = int(input("Digite outro número inteiro: "))
comparacao_e20 = n1_e20 != n2_e20
print(f"O resultado da comparação entre os dois números é: {comparacao_e20}")
