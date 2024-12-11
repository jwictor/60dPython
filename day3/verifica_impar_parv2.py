entrada = input("Coloque o numero: ")

try: #tente rodar
    numero = int(entrada)
    if numero % 2 == 0:
        print("Numero par")
    else:
        print("Este numero nao e par")
except ValueError:
    print("Essa entrada não e um numero inteiro")