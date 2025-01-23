"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule 
a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.
"""

def fibonacci_check(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

numero = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
if fibonacci_check(numero):
    print(f"{numero} está na sequência de Fibonacci.")
else:
    print(f"{numero} não está na sequência de Fibonacci.")