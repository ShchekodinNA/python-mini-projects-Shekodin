import datetime as dt
import os
import random
import smtplib
import pandas

DIR_WITH_LETTERS = "letter_templates"
FILES_WITH_BRTHD = "birthdays.csv"
REPLACEABLE_STR = "[NAME]"
SUBJECT_BEFORE_NAME = "Happy Birthday"
my_email = "Enter_yours"
smtp_setting = "smtp.inbox.ru"
my_password = "Enter"

wish_letters = os.listdir(DIR_WITH_LETTERS)
if len(wish_letters) == 0:
    quit()

for i in range(len(wish_letters)):
    wish_letters[i] = f"{DIR_WITH_LETTERS}/{wish_letters[i]}"

if os.path.exists(FILES_WITH_BRTHD):
    dtfrm = pandas.read_csv(FILES_WITH_BRTHD)
else:
    quit()

today = dt.datetime.now()

lst_to_cngrts = [[value[0], value[1]]
                 for (indx, value)
                 in dtfrm.iterrows()
                 if value[3] == today.month and value[4] == today.day]

if len(lst_to_cngrts) == 0:
    quit()

for born in lst_to_cngrts:
    letter = random.choice(wish_letters)
    with open(letter) as file:
        letter = file.read()
    letter = letter.replace(REPLACEABLE_STR, born[0])
    with smtplib.SMTP(smtp_setting) as cnnctn:
        cnnctn.starttls()
        cnnctn.login(user=my_email, password=my_password)
        cnnctn.sendmail(from_addr=my_email,
                        to_addrs=born[1],
                        msg=f"Subject:{SUBJECT_BEFORE_NAME} {born[0]}\n\n{letter}")
