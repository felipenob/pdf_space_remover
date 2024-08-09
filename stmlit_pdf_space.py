import streamlit as st

def process_text():
    st.title("Removedor de espaços (PDF)")
    st.write("Insira o texto desejado:")

    # Cria uma área de texto para o usuário inserir o texto
    text = st.text_area("Texto de entrada", "", height=150)

    if st.button("Processar Texto"):
        # Divide o texto em linhas
        lines = text.splitlines()
        # Remove espaços extras de cada linha
        clean_lines = [" ".join(line.split()) for line in lines]
        # Junta as linhas novamente, preservando quebras de linha
        clean_text = "\n".join(clean_lines)

 # Exibe o resultado
        st.write("Resultado:")
        st.text(clean_text)  # Usa st.text para preservar a formatação do texto

# Executa a função
process_text()

st.html('''<p style="text-align: center;"><b>Criado por Felipe Nobrega</b><br>Contato: <a href="mailto:felipeaugnobrega@gmail.com">felipeaugnobrega@gmail.com</a><br>Github: <a href="https://github.com/felipenob">felipenob</a></p>''')