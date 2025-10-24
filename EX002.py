# EX 2

# Casas

Grifinória = 0
Corvinal = 0
LufaLufa = 0 
Sonserina = 0 

# Perguntas

print('Q1) Você gosta do amanhecer ou do anoitecer?')
print('  1) Amanhacer')
print('  2) Anoitecer')
resp1 = int(input('Qual você escolher (1 ou 2)?  '))

if resp1 == 1:
 Grifinória += 1
 Corvinal += 1
elif resp1 == 2:
 LufaLufa += 1
 Sonserina += 1
else:
  print('Resposta errada! Tente novamente.')

print('Q2) Quando eu morrer, quero que lembrem de mim como ...')
print('  1) O bom')
print('  2) O grande')
print('  3) O sábio')
print('  4) O ousado')
resp2 = int(input('Qual número você escolhe?'))

if resp2 == 1:
 LufaLufa += 2
elif resp2 == 2:
 Sonserina += 2
elif resp2 == 3:
 Corvinal += 2
elif resp2 == 4:
 Grifinória += 2
else:
  print('Resposta errada! Tente novamente.')

print('Q3) Qual instrumento mais te agrada?')
print('  1) Violino')
print('  2) Trompete')
print('  3) Piano')
print('  4) Tambor')
resp3 = int(input('Qual número você escolhe?'))

if resp3 == 1:
 Sonserina += 4
elif resp3 == 2:
 LufaLufa += 4
elif resp3 == 3:
 Corvinal += 4
elif resp3 == 4:
 Grifinória += 4
else:
 print('Resposta errada! Tente novamente.')

# Resultado

print('\n--- Pontuação final ---')
print('Grifinória:', Grifinória)
print('Corvinal:', Corvinal)
print('LufaLufa:', LufaLufa)
print('Sonserina:', Sonserina)

# Bônus: mostrar a casa com mais pontos
max_score = max(Grifinória, Corvinal, LufaLufa, Sonserina)

print("\n✨ A casa escolhida é... ✨")
if Grifinória == max_score:
    print("🦁 Grifinória!")
elif Corvinal == max_score:
    print("🦅 Corvinal!")
elif LufaLufa == max_score:
    print("🦡 LufaLufa!")
elif Sonserina == max_score:
    print("🐍 Sonserina")