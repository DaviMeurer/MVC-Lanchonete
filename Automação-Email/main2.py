from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import mysql.connector
import os
from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()

def listaProdutos():
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("Conectado!")

        cursor = conexao.cursor()
        
        SQL_qtd0 = "SELECT * from PRODUTOS where qtd=0"
        cursor.execute(SQL_qtd0)
        resultado_qtd0 = cursor.fetchall()

        SQL_vendas = "SELECT SUM(preco) AS VendasTotal From PRODUTOS"
        cursor.execute(SQL_vendas)
        resultado_vendas = cursor.fetchall()

        return resultado_qtd0, resultado_vendas
    except mysql.connector.Error as e:
        print(f"Erro ao conectar com o BD: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        print("\nConexão encerrada.")

def send_mail(produtos):
    destinatario = os.getenv("GERENTE_EMAIL")
    remetente = os.getenv("SMTP_USER")
    senha = os.getenv("SMTP_PASSWORD")
    servidor = os.getenv("SMTP_SERVER")
    porta = os.getenv("SMTP_PORT")
    titulo = "Alerta: Produtos com estoque zerado"

    table = PrettyTable(['Produto', 'Quantidade'])
    for produto in produtos:
        table.add_row([produto[1], produto[3]])

    corpo = "Prezado gerente, os seguintes produtos estão com estoque zerado:\n\n"
    corpo += table.get_string()
    corpo += "\nPor favor, providencie a reposição!"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = titulo
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        with smtplib.SMTP(servidor, porta) as server:
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario, msg.as_string())
            print("E-mail enviado")
    except Exception as e:
        print("Erro ao enviar e-mail: ", e)

#Nova função de enviar o e-mail da soma dos produtos
def send_soma(preco):
    destinatario = os.getenv("GERENTE_EMAIL")
    remetente = os.getenv("SMTP_USER")
    senha = os.getenv("SMTP_PASSWORD")
    servidor = os.getenv("SMTP_SERVER")
    porta = os.getenv("SMTP_PORT")
    titulo = "Soma total dos produtos"

    table = PrettyTable(['Produto', 'Preço'])
    for p in preco:
        table.add_row(['Total', f"R$ {p[0]}"])

    corpo = "Prezado gerente, a soma total dos preços dos produtos é:\n\n"
    corpo += table.get_string()

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = titulo
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        with smtplib.SMTP(servidor, porta) as server:
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario, msg.as_string())
            print("E-mail da soma enviado")
    except Exception as e:
        print("Erro ao enviar e-mail: ", e)
        
#junção para enviar cada e-mail separadamente
produtos_zerados, soma_precos = listaProdutos()

send_mail(produtos_zerados)
send_soma(soma_precos)