def get_user_age():
    while True:
        try:
            idade = int(input("Qual é a sua idade? "))
            if idade < 0:
                raise ValueError("A idade não pode ser um número negativo.")
            return idade
        except ValueError as e:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")
            print(f"Detalhes do erro: {e}")

def check_age(idade):
    if idade >= 60:
        print("Você é idoso.")
    elif idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

def main():
    idade = get_user_age()
    check_age(idade)

if __name__ == "__main__":
    main()
