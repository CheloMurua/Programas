def collatz(num):
    pasos = 0
    while num != 1:
        print(num, end=" → ")
        num = num // 2 if num % 2 == 0 else 3 * num + 1
        pasos += 1
    print(f'Total de pasos: {pasos}')

try:
    num = int(input("Ingrese un número entero positivo: "))
    if num > 0:
        collatz(num)
    else:
        print("Debe ser un número mayor que cero.")
except:
    print("Entrada inválida.")
