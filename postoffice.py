import smtplib
import mimetypes
from email.message import EmailMessage


password = "nrexjbkmwebjnvcn"
sender_email = "StIgorLeon@yandex.ru"
recipient_email = ["aligol6573@gmail.com", "stigorleon@gmail.com" ]
subject = 'Проверка связи'
body = 'текст проверочного сообщения '

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email
# --- Вложение ---
image_path = Path("picture.jpg")          # путь к файлу
data = image_path.read_bytes()

# определяем MIME-тип по расширению
mime_type, _ = mimetypes.guess_type(image_path.name)
maintype, subtype = mime_type.split("/", 1)   # например "image/jpeg"

msg.add_attachment(
    data,
    maintype=maintype,          # "image"
    subtype=subtype,            # "jpeg"
    filename=image_path.name,
)
server = None
try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print('Письмо отправлено')
except Exception as e:
    print(f'Ошибка {e}')

finally:
    if server:
        server.quit()


