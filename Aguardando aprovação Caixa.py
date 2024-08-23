import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email():
    # Obter os valores dos campos de entrada
    chamado_numero = chamado_numero_entry.get()
    email_destino = email_destino_entry.get()

    # Corpo do e-mail com a formatação correta
    email_body = f"""\
    https://atlassian.net/browse/-{chamado_numero}

    Prezado, tudo bem?
    
Texto
    
    Vinícius Crepaldi.
    """
    
    # Configurações do servidor de e-mail corporativo
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    email_remetente = ''
    senha_remetente = ''

    # Configuração da mensagem
    msg = MIMEMultipart()
    msg['From'] = email_remetente
    msg['To'] = email_destino
    msg['Subject'] = f'Solicitação de acesso ({chamado_numero})'
    
    # Corpo do e-mail
    msg.attach(MIMEText(email_body, 'plain'))
    
    # Enviar o e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Ativa a segurança
        server.login(email_remetente, senha_remetente)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao enviar e-mail: {e}")

# Interface gráfica utilizando tkinter
root = tk.Tk()
root.title("Enviar E-mail") 
root.geometry("200x150")

# Campos de entrada
tk.Label(root, text="Número do Chamado:").pack()
chamado_numero_entry = tk.Entry(root)
chamado_numero_entry.pack()

tk.Label(root, text="E-mail de Destino:").pack()
email_destino_entry = tk.Entry(root)
email_destino_entry.pack()

# Botão enviar
enviar_button = tk.Button(root, text="Enviar", command=enviar_email)
enviar_button.pack(pady=10)

root.mainloop()
