ln = []
ma = 0
mn = 0
while ln != 'pare':
    for i in range(5):
        n = int(input('Digite um número: '))
        ln.append(n)
        if i == 0:
            ma = mn = n
        else:
            if n > ma:
                ma = n
            if n < mn:
                mn = n
print('__' * 20)
print(f'Você digitou os números: {ln}')
print(f'O maior número digitado foi: {ma}')
print(f'O menor número digitado foi: {mn}')