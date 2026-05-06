while True:
    ln = []
    for i in range(5):
        n = int(input('Digite um número: '))
        ln.append(n)

    ma = max(ln)
    mn = min(ln)

    print('__' * 20)
    print(f'Você digitou os números: {ln}')
    print(f'O maior número digitado foi: {ma}')
    print(f'O menor número digitado foi: {mn}')

    sair = input('Quer continuar? (s/n): ').lower()
    if sair == 'n':
        break
