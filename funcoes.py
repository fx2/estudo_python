def sum(a, b):
    return a + b


print(sum(1, 2))


def salario_desconto_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)


parametroNormal = salario_desconto_imposto(1000)
print(parametroNormal)

parametroNomeado = salario_desconto_imposto(1000, imposto=10)
print(f"Nomeado {parametroNomeado}")
