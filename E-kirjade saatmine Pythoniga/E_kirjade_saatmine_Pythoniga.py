import smtplib
from email.message import EmailMessage

def send_email():
    email_subject = "E-kirjade saatmine Pythoniga"

    while True:
        sender_email_address = input("Teie e-posti aadress: ")
        if "@" not in sender_email_address or "." not in sender_email_address:
            print("Palun sisesta kehtiv e-posti aadress.")
        else:
            receiver_email_address = input("Saaja e-posti aadress: ")
            email_password = input("Sisesta oma e-posti rakenduse parool: ")
            break

    # doip ffcu fpwt hced 
    email_smtp = "smtp.gmail.com"
    message = EmailMessage()

    with open("message.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    message.set_content(html_content, subtype="html")

    with open("python_gmail.jpg", "rb") as file:
        message.add_attachment(
            file.read(),
            maintype="image",
            subtype="jpg",
            filename="python_gmail.jpg"
        )

    message["Subject"] = email_subject
    message["From"] = sender_email_address
    message["To"] = receiver_email_address

    server = smtplib.SMTP(email_smtp, 587)
    server.starttls()
    server.login(sender_email_address, email_password)
    server.send_message(message)
    server.quit()

    print("E-kiri saadetud edukalt!")

send_email()