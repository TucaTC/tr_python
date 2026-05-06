s = float(input('Qual é o salário do funcionário? R$: '))
if s > 1250:
    print(f'O funcionário tem direito a um aumento de 10%, totalizando R${s * 1.10:.2f}.')
else:
    print(f'O funcionário tem direito a um aumento de 15%, totalizando R${s * 1.15:.2f}.')