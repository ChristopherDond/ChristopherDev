# EX 1
import random

opcoes = ["pedra", "papel", "tesoura"]
jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)
 
print(f"\nVocê escolheu: {jogador}")
print(f"O computador escolheu: {computador}\n")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") \
     or (jogador == "tesoura" and computador == "papel") \
     or (jogador == "papel" and computador == "pedra"):
    print("Você ganhou! 🎉")
elif jogador in opcoes:
    print("Você perdeu! 😢")
else:
    print("Opção inválida. Tente de novo.")