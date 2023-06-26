print("Digite dois numeros: ")
a = int(input())
b = int(input())

if a > b:
    menor = b
    b = a
    a = menor
soma = 0
for i in range(a+1, b):
    if i % 2 != 0:
       soma = soma + i
print(f"SOMA DOS IMPARES = {soma} ")       