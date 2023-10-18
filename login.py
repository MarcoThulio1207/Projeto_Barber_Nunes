import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import mysql.connector

class Application:
    def __init__(self):
        self.janelaCadastro = ctk.CTk()
        self.tema()
        self.tela()
        self.tela_login()
        self.janelaCadastro.mainloop()
        

    def tema(self):
        ctk.set_appearance_mode("black")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        self.janelaCadastro.geometry("780x600")
        self.janelaCadastro.title("Tela de Login")
        self.janelaCadastro.resizable(False, False)

    def tela_login(self):
        img = PhotoImage(file="LOGO1.png")
        label_img = ctk.CTkLabel(master=self.janelaCadastro, image=img, text=None).place(x=5, y=75)

        login_frame = ctk.CTkFrame(master=self.janelaCadastro, width=375, height=430)
        login_frame.pack(side=RIGHT)

        label = ctk.CTkLabel(master=login_frame, text="Login", font=("Roboto", 30))
        label.place(x=25, y=10)

        username_entrada1 = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de Usuário", width=300,
                                         font=ctk.CTkFont("Roboto, 14"))
        username_entrada1.place(x=25, y=105)
        username_label1 = ctk.CTkLabel(master=login_frame, text="O Campo Nome de Usuário é obrigatório",
                                       text_color="green", font=("Roboto", 12))
        username_label1.place(x=35, y=135)

        senha_entrada2 = ctk.CTkEntry(master=login_frame, placeholder_text="Senha de Usuário", show="*", width=300,
                                      font=ctk.CTkFont("Roboto", 14))
        senha_entrada2.place(x=25, y=175)
        senha_label2 = ctk.CTkLabel(master=login_frame, text="O Campo Senha é Obrigatório",
                                    text_color="green", font=("Roboto", 12))
        senha_label2.place(x=35, y=205)

        chekbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar-se de mim sempre")
        chekbox.place(x=25, y=235)

        def login():
            if (username_entrada1.get() == "" or senha_entrada2.get() == ""):
                messagebox.showerror(title="Erro", message="Preencha todos os Campos!")
            else:
                msg = messagebox.showinfo(title="Login", message="Login efetuado com Sucesso!")
                pass

        botao_de_login = ctk.CTkButton(master=login_frame, text="Login", width=300, command=login)
        botao_de_login.place(x=25, y=285)

        registar_span = ctk.CTkLabel(master=login_frame, text="Não tem uma conta?").place(x=25, y=325)


        def tela_cadastro():
            login_frame.pack_forget()
            registrar_frame.pack(side=RIGHT)

        registrar_frame = ctk.CTkFrame(master=self.janelaCadastro, width=375, height=430)

        label = ctk.CTkLabel(master=registrar_frame, text="Faça seu Cadastro!", font=("Roboto", 30))
        label.place(x=25, y=10)

        mensagem = ctk.CTkLabel(master=registrar_frame, text="Preencha todos os Campos", font=ctk.CTkFont("Roboto", 12),
                                text_color="green").place(x=25, y=50)

        nome_entrada2 = ctk.CTkEntry(master=registrar_frame, placeholder_text="Nome de Usuário", width=300,
                                     font=ctk.CTkFont("Roboto", 14))
        nome_entrada2.place(x=25, y=105)

        email_entrada2 = ctk.CTkEntry(master=registrar_frame, placeholder_text="E-mail de Usuário", width=300,
                                      font=ctk.CTkFont("Roboto", 14))
        email_entrada2.place(x=25, y=150)

        password_entrada2 = ctk.CTkEntry(master=registrar_frame, placeholder_text="Senha do Usuário", show="*",
                                         width=300, font=ctk.CTkFont("Roboto", 14))
        password_entrada2.place(x=25, y=195)

        rpassword_entrada2 = ctk.CTkEntry(master=registrar_frame, placeholder_text="Repetir a Senha", show="*",
                                          width=300, font=ctk.CTkFont("Roboto", 14))
        rpassword_entrada2.place(x=25, y=240)

        chekbox = ctk.CTkCheckBox(master=registrar_frame, text="Aceito os Termos e Política de Privacidade").place(
            x=25, y=285)
        

        
        def salvar_registro():
            nome = nome_entrada2.get()
            email = email_entrada2.get()
            senha = password_entrada2.get()
            rsenha = rpassword_entrada2.get()

            if (nome == "" or email == "" or senha == ""):
                messagebox.showerror(title="Erro", message="Preencha todos os Campos!")
            elif senha != rsenha:
                messagebox.showerror(title="Erro", message="As senhas não coincidem!")
            else:
                conexao = self.conectar_bd()
                if conexao:
                    cursor = conexao.cursor()
                    self.inserir_dados(cursor, nome, email, senha, rsenha)
                    conexao.commit()
                    conexao.close()

                    nome_entrada2.delete(0, END)
                    email_entrada2.delete(0, END)
                    password_entrada2.delete(0, END)
                    rpassword_entrada2.delete(0, END)

                msg = messagebox.showinfo(title="Cadastro", message="Cadastro efetuado com Sucesso!")

        botao_cadastro = ctk.CTkButton(master=registrar_frame, text="Cadastrar Conta", width=145, fg_color="green",
                                       hover_color="#014B05", command=salvar_registro).place(x=180, y=345)

        def retorno():
            registrar_frame.pack_forget()
            login_frame.pack(side=RIGHT)

        botao_voltar = ctk.CTkButton(master=registrar_frame, text="Voltar", width=145, command=retorno).place(x=25,
                                                                                                               y=345)

        botao_registar = ctk.CTkButton(master=login_frame, text="Cadastar", width=150, fg_color="green",
                                       hover_color="#2D9334", command=tela_cadastro).place(x=175, y=325)
        
        

    def conectar_bd(self):
        try:
            conexao = mysql.connector.connect(
                host="",
                user="root",
                password="",
                database="CADASTRO"
            )
            if conexao.is_connected():
                print("Conexão ao banco de dados estabelecida.")
            return conexao
        except mysql.connector.Error as erro:
            print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

    def inserir_dados(self, cursor, nome, email, senha, rsenha):
        conexao = self.conectar_bd()
        if conexao:
            cursor = conexao.cursor()
        query = "INSERT INTO cadastro_usuario (T_NOME, T_EMAIL, T_SENHA, T_RSENHA) VALUES ( %s, %s, %s, %s)"
        valores = (nome, email, senha, rsenha)
        cursor.execute(query, valores)
        conexao.commit()
        conexao.close()


Application()