# Escreva um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura em Fahrenheit. Sabe-se que F = ( 180*C)/100 + 32

print("Digite a seguir uma temperatura em Celsius")
cels = int(input("Insira o valor em Celsius"))   
far = (180 * cels) / 100 + 32
print("A temperatura inserida corresponde à: ", far, "Fahrenheit")
