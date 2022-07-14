lista = [[1,'salario',3,4], ['salario',10]]

print(lista[1][0])

lista = ['impostos', 'salarios', 'altos', 'baixos']
lista[2] = "Altos"
lista[3] = "Baixos"

print(lista)

if lista:
    print("Sempre sou executado")

if not lista:
    print("Nunca sou executado")

lista = []
if lista:
    print("NUNCA sou executado vazio")

if not lista:
    print("Sempre sou executado vazio")
