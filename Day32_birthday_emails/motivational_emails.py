import smtplib
import random
import datetime as dt

yahoomail = "myleslangston@hotmail.com"
gmail = "seanbean156@gmail.com"
password = "3hlT+P7u&Mr*z!A"

# finding the day of the week
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 3:
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
            to_addrs=yahoomail,
            msg=f"Subject:Motivation\n\n{random_quote}"
        )

