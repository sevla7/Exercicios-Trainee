
# Exercício 1 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# F = 9/5C + 32

temperatura_c = float(input('Informe a temperatura em Celsius: '))
temperatura_f = 9/5 * temperatura_c + 32
print(temperatura_f, "\n")


# =============
# Exercício 2 - Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:

# P = 72,7h - 58

altura = float(input('Informe a altura em metros: '))
peso_ideal = 72.7 * altura - 58
print(f'O peso ideal é: {peso_ideal:.2f} kg\n')


# =============
# Exercício 3 - Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

largura = float(input('Informe a largura da sala em metros: '))
comprimento = float(input('Informe o comprimento da sala em metros: '))
area = largura * comprimento
print('A área da sala é:', area, 'm²\n')


# =============
# Exercício 4 - Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

comprimento_m = float(input('Informe um comprimento em metros: '))
comprimento_cm = comprimento_m * 100
print('Este comprimento em centímetros é:', comprimento_cm, 'cm\n')


# =============
# Exercício 5 - Análise de funcionários
funcionarios = [
    ["João", "Maria", "Arthur", "Pedro", "Rodrigo", "Eduardo", "Gabriel"],
    [14000, 6000, 8000, 5000, 8000, 10000, 6500]
]

# Qual o funcionário com maior remuneração?
maior_salario = 0
ind_func= 0
for i, salario in enumerate(funcionarios[1]):
    if salario > maior_salario:
        maior_salario = salario
        ind_func = i

print(f"Funcionário com maior remuneração: {funcionarios[0][ind_func]}\n"
      f"Salário: {maior_salario}")



# Exercício 6 - Calculadora de Desconto Progressivo
# Crie uma calculadora de desconto que aplica descontos progressivos baseados no valor da compra:

"""
Compras até R$100: sem desconto
Compras entre R$100 e R$500: 5%
Compras entre R$500 e R$1000: 10%
Compras acima de R$1000: 15% de desconto
Além disso, se o cliente for VIP (True/False), adicione 2% de desconto extra.

O programa deve:

Solicitar o valor da compra
Solicitar se é cliente VIP
Calcular o desconto baseado na faixa de valor
Adicionar desconto VIP se aplicável
Calcular o valor final
Exibir: valor original, desconto aplicado (%), valor do desconto (R$), valor final

"""

valor_compra = float(input('Digite o valor da compra: '))
cliente_vip = input('É cliente VIP? (Sim/Não): ').lower()

if valor_compra < 100:
    desconto = 0.00
elif valor_compra >= 100 and valor_compra < 500:
    desconto = 0.05
elif valor_compra >= 500 and valor_compra < 1000:
    desconto = 0.10
else:
    desconto = 0.15

if cliente_vip == 'sim':
    desconto += 0.02

valor_com_desconto = valor_compra * desconto
valor_final = valor_compra * (1 - desconto)

print(f'Valor original: R${valor_compra:.2f}')
print(f'Desconto aplicado: {desconto:.2%}')
print(f'Valor do desconto: R${valor_com_desconto:.2f}')
print(f'Valor final: R${valor_final:.2f}')


# Exercício 7 - Classificador de Idade
# Crie um programa que classifique uma pessoa em categorias de idade:

"""
Menor de 18 anos: "Menor de idade"
Entre 18 e 64 anos: "Adulto"
65 anos ou mais: "Idoso"
Solicite a idade ao usuário e exiba a classificação usando if, elif e else.
"""

while True:

  idade = int(input('Digite sua idade (-1 para sair): '))

  if idade == -1:
      break
  elif idade < 18:
      print('Menor de idade')
  elif idade < 65:
      print('Adulto')
  else:
      print('Idoso')



# Exercício 8 - Sistema de Cadastro Completo
# Crie um programa que solicite ao usuário:

"""
Crie um programa que solicite ao usuário:

Nome completo
Idade (converta para inteiro)
Altura em metros (converta para float)
Depois, exiba uma mensagem formatada com todas as informações coletadas.

"""
nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF (apenas números): ")
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
salario = float(input("Digite seu salário: "))
status = input("É funcionário ativo? (Sim/Não): ").lower()

match(status):
    case 'sim':
        ativo = True
    case 'não':
        ativo = False

print("\n=== Sistema de Cadastro ===")
print("Nome: ", nome)
print("CPF: ", cpf)
print("Data de Nascimento:", data_nascimento)
print("Salário: ", salario)
print(f"Status: {'Ativo' if ativo else 'Inativo'}")



# Exercício 9 - Validador de Senha com WHILE
# Crie um programa que valide uma senha. A senha deve:

""""
Ter pelo menos 8 caracteres
Conter pelo menos uma letra maiúscula
Conter pelo menos uma letra minúscula
Conter pelo menos um número
O programa deve solicitar a senha repetidamente até que uma senha válida seja fornecida, usando while.

"""

while True:

    senha = input('Digite uma senha: ')

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    if len(senha) >= 8:
        for caractere in senha:
            if caractere.islower():
                tem_minuscula = True

            if caractere.isupper():
                tem_maiuscula = True

            if caractere.isnumeric():
                tem_numero = True

        if tem_minuscula and tem_maiuscula and tem_numero:
            print('Cadastro realizado com sucesso.\n')
            break
        else:
            print('Senha inválida! Tente novamente.')

    else:
        print('Senha inválida! Tente novamente.')


# Exercício 10 - Menu Interativo com While True
# Crie um menu interativo que permite ao usuário:

"""
Calcular área de um retângulo
Calcular área de um círculo
Verificar se um número é par ou ímpar
Sair do programa
O programa deve:

Exibir um menu numerado
Solicitar a opção do usuário
Executar a operação escolhida
Voltar ao menu após cada operação (exceto ao sair)
Usar while True com break para sair
Usar continue para voltar ao início do loop em caso de opção inválida

"""

while True:
    print ('=== MENU ===')
    print ('1. Calcular área do retângulo')
    print ('2. Calcular área do círculo')
    print ('3. Verificar se número é par/ímpar')
    print ('4. Sair')

    opcao = int(input('Escolha uma opção: '))
    match(opcao):
        case 1:
            largura = float(input('Digite a largura: '))
            altura = float(input('Digite a altura: '))
            print(f'Área do retângulo: {largura * altura:}')
            break

        case 2:
            from math import pi
            raio = float(input('Digite o raio: '))
            print(f'Área do círculo: {pi * (raio * raio):.2f}')
            break
  
        case 3:
            numero = int(input('Digite um número: '))
            if numero % 2 == 0:
                print(f'O número {numero} é par')
                
            else:
                print(f'O número {numero} é ímpar')
            break

        case _:
            print('Opção inválida!')
            continue