i = 0
while True:
    try:
        nome = input("Por favor digite o seu nome ")
        ind = int(input("Digite um índice do seu nome digitado "))
        print(nome[ind])
        break
    except ValueError:
        print("Ooops! Nome inválido. Tente novamente...")
    except IndexError:
        print("Ooops! Índice inválido. Tente novamente...")
    finally:
        print(f"Tentativa {i}")
        i += 1
        