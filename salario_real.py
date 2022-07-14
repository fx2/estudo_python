salario = int(input('Salario? '))
imposto = input('Imposto em % (ex: 27.5)? ')

if imposto != '':
    imposto = float(imposto)

if imposto == '':
    imposto = float(27.5)


print('Valor real: {0}' .format(salario - (salario * imposto * 0.01)))

if imposto < 10:
    print("Médio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito Alto")

ganhando_bem = "Está ganhando muito bem: " if salario > 5000 else "Ganhando mal"
print(ganhando_bem)