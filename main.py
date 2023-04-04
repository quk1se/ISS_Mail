import requests
from datetime import datetime
import smtplib
LAT = 50.372194
LNG = 30.377229
my_email = "alexandrkalyan953@gmail.com"
password = "wsdmpioggbdiseil"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)

def is_iss_up():

    iss = requests.get("http://api.open-notify.org/iss-now.json")
    latitude = float(iss.json()["iss_position"]["latitude"])
    longitude = float(iss.json()["iss_position"]["longitude"])
    if latitude < LAT + 5 and latitude > LAT - 5 and longitude < LNG + 5 and longitude > LNG - 5:
        return True

def is_night():
    parameters = {"lat": LAT, "lng": LNG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json",params= parameters)
    data = response.json()["results"]
    sunrise = float(data["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


if is_night() and is_iss_up():
    connection.sendmail(from_addr=my_email, to_addrs="alexkalyan922@gmail.com", msg="Look up here), and im not a scary mob in your house, look at the sky)")

