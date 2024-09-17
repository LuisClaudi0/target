def is_fibonacci(n):
    # Função para verificar se um número é um número de Fibonacci
    if n < 0:
        return False
    
    # Função auxiliar para verificar se um número é um quadrado perfeito
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x

    # Um número é um número de Fibonacci se e somente se uma (ou ambas) das seguintes expressões é um quadrado perfeito
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Solicita ao usuário um número
num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica e exibe se o número pertence à sequência de Fibonacci
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
