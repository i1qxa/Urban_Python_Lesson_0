def send_email(message: str, recipient: str, sender: str = "university.help@gmail.com") -> None:
    is_email_correct: bool = True
    list_email = [recipient, sender]
    valid_domains = ["com", "net", "ru"]
    for i in range(0, list_email.__len__()):
        if not list_email[i].__contains__("@"):
            is_email_correct = False
            break
        if not valid_domains.__contains__(list_email[i].split('.')[-1]):
            is_email_correct = False
            break
    if not is_email_correct:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
