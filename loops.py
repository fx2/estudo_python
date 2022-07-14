# salario = int(input('Digite o salario'))
# imposto = 27
#
# while imposto > 0:
#     imposto = input("imposto ou (s) para sair")
#     if not imposto:
#         imposto = 27
#     elif imposto == "s":
#         break
#     else:
#         imposto = float(imposto)
#
#     print("Valor real: {0}" .format(salario - (salario * imposto * 0.01)))

impostos = ['Mei', 'Simples']

for imposto in impostos:
    if imposto.startswith("S"):
        continue
    print(imposto)

for i, imposto in enumerate(impostos):
    print(i, imposto)

lista = [0,1,2,3,4,5,6,7,8,9]

for list in lista:
    print(list)

for i in range(0,5):
    print(i)