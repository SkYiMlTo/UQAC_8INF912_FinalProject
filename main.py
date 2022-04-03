import smtplib
from email.message import EmailMessage


def sendMail(EMAIL_ADDRESS, EMAIL_PASSWORD, msg):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            return False
    except:
        return True


def sendNotificationMail(subj, contenu, dest):
    EMAIL_ADDRESS = "notification.proche.aidant@gmail.com"
    EMAIL_PASSWORD = "PSX74FJPq@KzDfg6byagTNJ#MKRJisGAEECerFt5"

    msg1 = EmailMessage()
    msg1['Subject'] = str(subj)
    msg1['From'] = EMAIL_ADDRESS
    msg1['To'] = str(dest)  # "hugo.bourreau@isen-ouest.yncrea.fr"
    msg1.set_content(str(contenu))

    error = sendMail(EMAIL_ADDRESS, EMAIL_PASSWORD, msg1)

    if not error:
        print("Mail envoyé")
        return True
    else:
        print("Erreur d'envoi")
        return False


sendNotificationMail("Notification proche aidant", "Anomalie détectée", "gogo.bourreau@hotmail.fr")

# def main():
#     path = '/var/www/html/mainRaspberry/jsonFiles/smtpSpammer'
#     bashCommand = "sudo rm /var/www/html/mainRaspberry/jsonFiles/smtpSpammer/"
#     while 1:
#         files = os.listdir(path)
#         if files:
#             for file in files:
#                 with open(path + '/' + file) as json_data:
#                     data_dict = json.load(json_data)
#                     spam(data_dict["subject"], data_dict['message'], data_dict['mail'])
#                     delFile = bashCommand + file
#                     process = subprocess.Popen(delFile.split(), stdout=subprocess.PIPE)
#                     output, error = process.communicate()
#         time.sleep(15)



# while a:
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         while 1:
#             try:
#                 smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#                 smtp.send_message(msg)
#                 break
#             except:
#                 print("Interrupt" + str(a))
#                 a = 0
#                 break
#                 time.sleep(60)
#         if a != 0:
#             print("Email " + str(a) + " sent")
#             time.sleep(0.1)
#             smtp.quit()
