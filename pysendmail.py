# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate


"""
# メール送信設定
smtp_server = '__送信サーバー__'
smtp_port = '__送信ポート__'
smtp_id = '__送信ユーザーID__'
smtp_pw = '__パスワード__'
mail_from = '__送信元アドレス__'
mail_to = '__宛先アドレス（リスト）__'
subject = '__件名__'
message = '__メール本文__'
"""

# メール送信
def sendToInfoMail(smtp_server, smtp_port, smtp_id, smtp_pw, mail_from, mail_to, subject, message):

    # メール送信処理
    mail = MIMEText(massage)
    mail['Subject'] = subject
    mail['From'] = mail_from
    mail['To'] = mail_from
    mail['Date'] = formatdate(localtime=True)

    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(smtp_id, smtp_pw)
    smtp.sendmail(mail_from, mail_to.split(','), mail.as_string())
    smtp.close()

def main():
    sendToInfoMail(smtp_server, smtp_port, smtp_id, smtp_pw, mail_from, mail_to, subject, message):


if __name__ == '__main__':
    main()
