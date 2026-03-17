print('Informe os dados para o cálculo dos juros')

capital = float(input('Capital: '))

taxa = float(input('Taxa de juros: '))

tempo = float(input('Tempo: '))

juros = capital * taxa * tempo / 100

# Formatando para exibir como valor monetário (opcional)

print(f'O valor dos juros é: R$ {juros:.2f}')
