# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# fatorial = 8! = 8x7x6x5x4x3x2x1 = 40320
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1

for n in range(1, numero + 1):
    fatorial *= n

print("O resultado de {0}! é: {1}".format(numero, fatorial))
