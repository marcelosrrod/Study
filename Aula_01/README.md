# Desafio da Aula 01 - Jornada de Dados - Bootcamp de Python.
****
1) Faça uma aplicação que receba um nome e conte quantas letras aquele nome tem.

*Gabarito*:

**print(len(input("Digite seu nome: ")))**
****
2) Faça uma aplicação que receba do usuário dois números e some eles, mostrando o resultado ao usuário.

*Gabarito:*

**print(int(input("Digite o primeiro número: ) + int("Digite o segundo número: )))**

****
3) Refatore as soluções anteriores agora com a utilização de variavéis.

*Gabarito:*

1. Primeiro desafio:

**nome = input("Informe seu nome: ")**

**print(len(nome))**

2. Segundo desafio:

**n1 = int(input("Informe o primeiro número: "))**

**n2 = int(input("Informe o segundo número: "))**

**soma = n1 + n2**
****

### Desafio final
**Faça uma aplicação para calcular o KPI de bônus anual do salário de um funcionário.**

*Dica: A métrica do KPI é: salário * % do bônus + 1000*

*Gabarito:*

**CONSTANTE_BONUS = 1000**

**nome_usuario = input("Digite seu nome: ")**

**salario_usuario = float(input("Digite seu salário: ))**

**bonus_usuario = float(input("Digite o valor do seu bônus: ))**

**valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario**

**print(f"O usuário {nome_usuario} possui bônus de R${valor_bonus}")**