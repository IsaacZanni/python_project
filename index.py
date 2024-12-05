print("* Calculadora INCRÍVEL *")

print("Indique a operação matemática:")
operacao = int(input("(1) Adição \n(2) Subtração \n(3) Multiplicação \n(4) Divisão \n"))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == 1:
    resultado = (num1+num2)
    print(f"Resultado = {resultado}")

elif operacao == 2:
    resultado = (num1-num2)
    print(f"Resultado = {resultado}")

elif operacao == 3:
    resultado = (num1*num2)
    print(f"Resultado = {resultado}")

elif operacao == 4:
    resultado = (num1/num2)
    print(f"Resultado = {resultado}")