d = int(input('Dias de aluguel: '))
k = float(input('Km percorridos: '))
p = (d * 60) + (k * 0.15)
print(f'O preço a pagar é de R$ {p:.2f}.')