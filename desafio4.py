print('--- CALCULADORA SIMPLES ---')

num1 = float(input('Primeiro número: '))

num2 = float(input('Segundo número: '))

operacao = input('Escolha a operação (+, -, *, /): ')

if operacao == '+':

resultado = num1 + num2

elif operacao == '-':

resultado = num1 - num2

elif operacao == '*':

resultado = num1 * num2

elif operacao == '/':

# Verificação para evitar divisão por zero

if num2 != 0:

resultado = num1 / num2

else:

resultado = 'Erro! Divisão por zero.'

else:

resultado = 'Operação inválida.'

print(f'Resultado: {resultado}')
