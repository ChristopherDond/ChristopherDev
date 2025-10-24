# EX 04
nota = float(input("Digite sua nota aqui: "))
if nota >= 7.0:
    print("Aprovado")
elif 5.0 <= nota < 7.0:
    print("Recuperação")
else:
    print("Reprovado")

# EX 05
usuario = input("Digite seu nome aqui:")
senha = input("Digite sua senha aqui:")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")

# EX 06
peso = float(input("Digite seu peso em KG:"))
altura = float(input("Digite sua altura em M:"))
imc = (peso / (altura ** 2))
print("O seu IMC e de:", imc)

if imc < 18.5:
    print("Abaixo do peso")
if 18.5 <= imc <= 24.9:
    print("Normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30.0:
    print("Obesidade")