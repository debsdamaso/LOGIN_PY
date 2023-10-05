# RM 97836, Aluna: Débora Dâmaso Lopes. TURMA N
def validate_login(login):
    if len(login) < 6:
        return False

    if not login[0].isdigit():
        return False

    if not any(c.isalpha() for c in login[1:]):  # Verificar se há pelo menos uma letra nas posições restantes
        return False

    return True

def validate_email(email):
    # Divide o email em partes pelo arroba
    partes = email.split('@')
    # Verifica se há duas partes após dividir pelo arroba
    if len(partes) != 2:
        return False
    nome_sobrenome = partes[0]
    dominio = partes[1]
    # Verifica se começa com letra
    if not nome_sobrenome[0].isalpha():
        return False
    # Verifica se não há caracteres especiais no nome e sobrenome
    if not nome_sobrenome.replace('.', '').isalnum():
        return False
    # Verifica se há mais de um ponto no email
    if dominio.count('.') > 2:
        return False
    # Verifica se o ponto não está na sequência do arroba
    if dominio[0] == '.' or dominio[-1] == '.':
        return False
    # Verifica se não há dois pontos juntos
    if '..' in dominio:
        return False

    return True

def write_to_file(login, email):
    with open('rm97836.txt', 'a') as file:
        file.write(f"{email.lower()}, {login.upper()}\n")

def display_file_content():
    with open('rm97836.txt', 'r') as file:
        for line in file:
            print(line.strip())

def main():
    while True:
        print("MENU\n")
        print("0 - SAIR")
        print("1 - Digite as credenciais (Login e E-mail)")
        print("2 - Exiba o arquivo\n")

        choice = input("Escolha: ")

        if choice == '0':
            print("Programa encerrado")
            break
        elif choice == '1':
            while True:
                login = input("Digite o LOGIN: ")
                if validate_login(login):
                    break
                else:
                    print("ERRO! DIGITE UM LOGIN VÁLIDO")

            while True:
                email = input("Digite o E-MAIL: ")
                if validate_email(email):
                    break
                else:
                    print("ERRO! DIGITE UM E-MAIL VÁLIDO")

            print("LOGIN E E-MAIL GRAVADOS COM SUCESSO!")
            write_to_file(login, email)
        elif choice == '2':
            print("Conteúdo do arquivo:")
            display_file_content()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

