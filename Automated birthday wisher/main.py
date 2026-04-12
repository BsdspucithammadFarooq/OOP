##################### Extra Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib
PLACE_HOLDER="[NAME]"
email_from="asaprogrammer42@gmail.com"
password_from="zygackxmozcyyfni"
df=pandas.read_csv("birthdays.csv")
print(df)
for (index,row) in df.iterrows():
    month=row.month
    day=row.day
    email=row.email
    now=datetime.datetime.now()
    current_year=now.year
    current_month=now.month
    month_day=now.day
    if month==current_month and day==month_day:
        print("happy birthday!")
        the_person = df["name"][index]
        random_number=random.randint(1,3)
        if random_number==1:
            with open("letter_templates/letter_1.txt") as file:
                data=file.read()
                x=data.replace(PLACE_HOLDER,the_person)
                print("letter1")
        elif random_number == 2:
            with open("letter_templates/letter_2.txt") as file:
                data = file.read()
                x = data.replace(PLACE_HOLDER, the_person)
                print("letter 2")
        elif random_number == 3:
            with open("letter_templates/letter_3.txt") as file:
                data = file.read()
                x = data.replace(PLACE_HOLDER, the_person)
                print("letter 3")
        with smtplib.SMTP("smtp.gmail.com") as mail:
            mail.starttls()
            mail.login(user=email_from, password=password_from)
            mail.sendmail(from_addr=email_from, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{x}")
