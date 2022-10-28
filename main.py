from datetime import datetime
import pandas
import random
import smtplib

# Placeholder data:
MY_EMAIL = "testemail@gmail.com"
MY_PASSWORD = "qwerty"

# Check if today matches a birthday in the birthdays.csv (Create a tuple from today's month and day):
today = datetime.now()
today_tuple = (today.month, today.day)
#    or this can be written as:
#           today = (datetime.now().month, datetime.now().day)


# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
# Use dictionary comprehension to create a dictionary from birthday.csv that is formatted like this:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # change range if more letter templates are added:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    # ensure proper SMTP port is used for MY_EMAIL you selected:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
