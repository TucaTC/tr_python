v = float(input('qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h.')
    print(f'Você deve pagar uma multa de R${(v - 80) * 7:.2f}.')
print('Tenha um bom dia! Dirija com segurança!')