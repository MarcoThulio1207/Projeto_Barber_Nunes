import mysql.connector

def registros():
    nome = nome_entrada2.get()
    email = email_entrada2.get()
    senha = password_entrada2.get()
    rsenha = rpassword_entrada2.get()

    conexao = conectar_bd()
    if
        conexao:
        cursor = conexao.cursor()
        inserir_dados(cursor, nome, email, senha)
        conexao.commit()
        conexao.close()

    nome_entrada2.delete(0, END)
    email_entrada2.delete(0, END)
    password_entrada2.delete(0, END)
    rpassword_entrada2.delete(0, END)


def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="seu_host",
            user="seu_usuario",
            password="sua_senha",
            database="CADASTRO"
        )
        if conexao.is_connected():
            print("Conexão ao banco de dados estabelecida.")
            return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

def inserir_dados(cursor, nome, email, senha):
    query = "INSERT INTO sua_tabela (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(query, valores)

    
