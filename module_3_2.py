def send_email(message, recipient, sender ="university.help@gmail.com"):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")) or "@" not in sender or not sender.endswith((".com", ".ru" , ".net")):
        print(f"Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
    elif recipient == sender:
        print("Письмо нельзя отправить самому себе")
    elif sender == "university.help@gmail.com" :
        print("Письмо успешно отправлено с адреса <sender> на адрес <recipient> ")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")

send_email('message', 'vasyok1337@gmail.com')
send_email('message', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('message','urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('message', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
