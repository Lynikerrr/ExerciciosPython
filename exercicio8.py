# Faça um programa que leia o seu ano de ingresso no curso, duração do curso e calcule o ano de sua formatura e dê parabens
primeiro = int(input("Digite o ano que você ingressou na faculdade: "))
tempo = int(input("Digite a duração do seu curso: "))
forma = primeiro + tempo - 1
print("Parabens, voce se forma no ano de: ", forma)