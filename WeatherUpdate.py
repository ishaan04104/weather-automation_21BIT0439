#weather report automation
from bs4 import BeautifulSoup
import requests
import smtplib

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    weather = soup.select('#wob_dc')[0].getText().strip()
    temperature = soup.select('#wob_tm')[0].getText().strip()
    subject = "Weather update"
    body = f"TODAYS WEATHER REPORT\nToday the weather is {weather}  and temperature is {temperature} °C in {loc}. \n Good day ahead!"
    msg = f"Subject:{subject}\n\n{body}\n\nRegards,\n21BIT0439".encode('utf-8')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print(server.ehlo())
    print(server.starttls())
    server.login('xxxxxxxxxxxx', 'xxxxxxxxxxxx')
    server.sendmail('xxxxxxxxxxxxxx', 'xxxxxxxxxxxxx', msg)
    print("Email Sent!")
    server.quit()
loc = 'Hyderabad'
city = loc + " weather"
weather(city)
