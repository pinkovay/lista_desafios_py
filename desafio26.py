frase = str(input('Digite uma frase: ')).upper().strip()
a = frase.count('A')
print(f'A letra (A) aparece {a} vezes nesta frase/palavra/nome. ')
print('E a primeira vez que ela aparece é na casa:', frase.find('A')+1)
print('A ultima vez é na casa:', frase.rfind('A')+1)

