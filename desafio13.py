print('Programa usado para calcular aumento salarial:')
print('DIGITE SOMENTE O NÚMERO')
sal = float(input('Qual o salário atual? R$'))
aum = float(input('De quantos % será o aumento?, se for desconto, por favpr digite 0:'))
des = float(input('Caso seja desconto, por favor digite o valor, se não for o caso, digite 0:'))
aume = sal + (sal * aum / 100)
desc = sal - (sal * des / 100)
print(f'Com o aumento de {aum}%, o salário passa a ser: R${aume}')
print(f'Com desconto de {des}%, o salário passa a ser: R${desc}')
