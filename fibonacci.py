def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return(fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2))

n_terms = int(input("Quantos termos você quer? "))

if n_terms <= 0:
    print("Por favor, insira um número positivo.")
else:
    print("Sequência de Fibonacci:")
    for i in range(n_terms):
        print(fibonacci_recursivo(i))