import requests
from bs4 import BeautifulSoup
import smtplib


url = "Your amazon product link"

header = {
    # GO to this site http://myhttpheader.com/ and copy user agent and accept language and paste is here
    "User-Agent": "Your user agent",
    "Accept-Language": "Your accept language"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

product_title = soup.find(id="productTitle").get_text().strip()
print(product_title)

price = soup.find(id="priceblock_ourprice").get_text()
stripped_price = price.strip("₹ ,")
replaced_price = stripped_price.replace(",", "")
find_dot = replaced_price.find(".")
to_convert_price = replaced_price[0:find_dot]
converted_price = int(to_convert_price)

price_full = converted_price
print(int(price_full))

BUY_PRICE = # Your buy price in INT


if price_full < BUY_PRICE:
    message= f"{product_title} is now {price_full}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("Your email", "Your password")
        connection.sendmail(
            from_addr="Your Email",
            to_addrs="Receivers Email",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

