import smtplib
import random
import datetime as dt
import pandas

gmail = "seanbean156@gmail.com"
password = "3hlT+P7u&Mr*z!A"

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        birthday_letter = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=gmail, password=password)
        connection.sendmail(
            from_addr=gmail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{birthday_letter}"
        )

