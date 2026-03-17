print('Segundos para H:M:S')

total_segundos = int(input('Informe número total de segundos: '))

minutos = total_segundos // 60

segundos = total_segundos % 60

horas = minutos // 60

minutos %= 60

print(horas, ':', minutos, ':', segundos)

print('H:M:S para Segundos')

print('Informe os dados')

horas = int(input('Horas: '))

minutos = int(input('Minutos: '))

segundos = int(input('Segundos: '))

total_segundos = horas * 60 * 60 + minutos * 60 + segundos

print('O total de segundos é', total_segundos)
