def process_text():
    while True:
        print("Insira o texto desejado: ")
        text = input("") #pede para o usuário inserir o texto
        # Divide o texto em linhas
        lines = text.splitlines()
        # Remove espaços extras de cada linha
        clean_lines = [" ".join(line.split()) for line in lines]
        # Junta as linhas novamente, preservando quebras de linha
        clean_text = "\n".join(clean_lines)

        print("Resultado:\n",clean_text)

        print("Você gostaria de processar mais texto? Responda com 's' ou 'n'")
        answer = input()

        if answer.lower() != "s":
            break

    print("Obrigado por usar o programa.")

process_text()


