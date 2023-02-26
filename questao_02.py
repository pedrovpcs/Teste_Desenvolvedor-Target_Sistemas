num = int(input("Digite um número inteiro positivo: "))

fib_list = [0, 1]

while fib_list[-1] < num:
    fib_list.append(fib_list[-1] + fib_list[-2])

if num in fib_list:
    print(f"O número {num} pertence à sequência de Fibonacci.")

else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
