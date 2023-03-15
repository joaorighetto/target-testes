def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


value = int(input("Digite um numero: "))

if value in [fibonacci(n) for n in range(21)]:
    print("O numero pertence a sequencia de Fibonacci com ate 20 elementos")
else:
    print("O numero nao pertence a sequencia de Fibonacci com ate 20 elementos")
