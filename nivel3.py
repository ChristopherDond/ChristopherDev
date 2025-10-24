# EX 07
ano = int(input("Digite um ano aqui: "))
if ano % 4 == 0:
    print("Ano Bissexto")
elif ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano nao e bissexto")

# EX 08
valor = int(input("Digite o valor a ser sacado: "))
notas = [100, 50, 20, 10, 5, 2]
quantidades = {}
for nota in notas:
    quantidades[nota] = valor // nota
    valor = valor % nota
print("Notas entregues:")
for nota in notas:
    print(f"{quantidades[nota]} nota(s) de R$ {nota}")

# EX 09
temp = float(input("Digite uma tmperatura em Celsius: "))
Fahrenheit = (temp * 9/5) + 32
print("A temperatura em Fahrenheit e de:", Fahrenheit)