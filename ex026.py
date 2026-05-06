fr = input('Digite uma frase: ')
print(f'A letra "A" aparece {fr.upper().count("A")} vezes.')
print(f'A letra "A" aparece pela primeira vez na posição {fr.upper().find("A") + 1}.')
print(f'A letra "A" aparece pela última vez na posição {fr.upper().rfind("A") + 1}.')