import random

palpite = 0
numero_secreto = random.randint (1,100)


while True:
    

    palpite = int(input("digite seu palpite:"))

    

    if palpite == numero_secreto:
        print(f"parabéns você acertou!!")
        break

    elif palpite < numero_secreto:
        print("o número é maior!")

    elif palpite > numero_secreto:
        print("o número é menor!")

    