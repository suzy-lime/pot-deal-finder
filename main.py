import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.com/Creuset-Round-Cast-iron-Dutch-Oven/dp/B07G2R8TN9/ref=sr_1_4?" \
      "crid=3O3W30C6DTJYL&dchild=1&keywords=le+crusette+dutch+ovens+7.25+qt&qid=1631047086&" \
      "s=home-garden&sprefix=le+cru%2Cgarden%2C207&sr=1-4"

suzy_email = os.environ.get("SECRET_EMAIL_1")
suzy_password = os.environ.get("SECRET_PASSWORD")
josh_email = os.environ.get("SECRET_EMAIL_2")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                  " like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

price = float(soup.find(name="span", id="newBuyBoxPrice").getText().split("$")[1])

if price < 500:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=suzy_email, password=suzy_password)
        connection.sendmail(from_addr=suzy_email, to_addrs=josh_email,
                            msg=f"Subject: It's Dutch Oven Time!!\n"
                                f"The price on your dream dutch over has dropped to ${price}.\n"
                                f"Go forth and follow your bread making dreams!")
