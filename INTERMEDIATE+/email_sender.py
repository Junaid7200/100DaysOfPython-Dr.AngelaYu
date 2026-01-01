import smtplib

password = "your_password"
my_email = "your_email"


def send_email(message,receiver):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs= receiver,
                            msg = f"Subject: This is Coding practice, in case this mail gets sent to the wrong email, just ignore it!!!\n\n{message}")
    print("Email send successfully!")
