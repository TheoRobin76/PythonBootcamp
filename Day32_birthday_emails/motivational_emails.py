import smtplib
import random
import datetime as dt

myles = ""
theo = ""
antonia = ""
gmail = "seanbean156@gmail.com"
password = ""

# finding the day of the week
now = dt.datetime.now()
year = now.year
hour = now.hour
day_of_week = now.weekday()

# choosing a random motivational quote
with open("quotes.txt", 'r') as quotes:
    all_quotes = quotes.readlines()
    random_quote = random.choice(all_quotes)
print(random_quote)

# emailing the quote
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=gmail, password=password)
    connection.sendmail(
        from_addr=gmail,
        to_addrs=(myles, theo, antonia),
        msg=f"Subject:Motivation\n\n{random_quote}"
    )
