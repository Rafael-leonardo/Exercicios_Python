a = int(input('Por favor, entre com o numero de segundos que deseja converter: '))
dias = a // 86400
horas = (a % 86400) // 3600
minutos = ((a % 86400) % 3600) // 60
segundos = ((a % 86400) % 3600) % 60
print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')