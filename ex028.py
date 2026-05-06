from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n1 = randint(0, 5)
n2 = int(input('Escreva seu chute: '))
if n1 == n2:
    print('Parabéns! Você acertou.')
else:
    print(f'Você errou. O número que eu pensei era {n1}.')