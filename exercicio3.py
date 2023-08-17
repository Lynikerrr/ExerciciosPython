# Faça um programa que leia 2 numeros reais e calcule e mostre a soma, a multiplicação, a subtração, a divisão, o resto da divisão, a potenciação e a média entre eles 
num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma = num1 + num2
mult = num1 * num2
sub = num1 - num2
div = num1 / num2
rest = num1 % num2
pot = num1 ** num2
med = (num1 + num2) / 2

print("Soma: ", soma, "Multiplicação: ", mult, "Subtração: ", sub, "Divisão: ", div, "Resto: ", rest, "Potencia: ", pot, "Media: ", med)