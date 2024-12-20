from imap_tools import MailBox, AND

username = "seu email"
password = "sua senha ou chave"
meu_email = MailBox('imap do email').login(username, password)


def pegar_hora():
    comprovante_ponto = meu_email.fetch(AND(seen=False, from_='email do remetente'))
    palavra_inicial = "HORA"
    palavra_final = "HORA"
    mensagem = ""
    texto = ""

    for email in comprovante_ponto:
        texto = email.html
        if palavra_inicial in texto:
            inicio = texto.find(palavra_inicial)
            fim = texto.find(palavra_final)
            if inicio != -1:
                hora = texto[inicio + 6:fim + 11]
                return hora
