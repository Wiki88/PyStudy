# Sending out letters. Рассылка писем

def send_email(messege, recipient, sender='university.help@gmail.com'):
    if '@' not in recipient and sender or \
            ('.com' not in recipient and '.ru' not in recipient and '.net' not in recipient) or \
            ('.com' not in sender and '.ru' not in sender and '.net' not in sender):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        return False
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    return messege
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

