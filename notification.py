from bs4 import BeautifulSoup
import requests
import smtplib

import vlc
import time
import schedule

prices_list = []

def check_price():
    URL = 'https://immense-springs-17358.herokuapp.com/'
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="menu-item-name").get_text()
    prices = soup.find(class_="menu-item-price").get_text()
    converted_price = float(prices.replace("€", ""))

    prices_list.append(converted_price)

    print(title)
    print(converted_price)
    return converted_price

def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("nu83359@gmail.com", "zxcasdqwe!@#")
    s.sendmail("nu83359@gmail.com", "ginggeli@hotmail.com", message)
    print("Email has been send to ginggeli@hotmail.com, Please check your mail")
    s.quit()

def price_decreased(prices_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False

def price_not_changed(prices_list):
    if prices_list[-1] == prices_list[-2]:
        return True
    else:
        return False

def price_increased(prices_list):
    if prices_list[-2] < prices_list[-1]:
        return True
    else:
        return False

def Scream():
    sound_file = vlc.MediaPlayer("./audio/screaming.mp3")
    sound_file.play()

def Silence():
    sound_file = vlc.MediaPlayer("./audio/Silence.mp3")
    sound_file.play()

def Sad():
    sound_file = vlc.MediaPlayer("./audio/SAD.mp3")
    sound_file.play()

count = 1
while True:
    current_price = check_price()
    if count > 1:
        decreased = price_decreased(prices_list)
        no_changes = price_not_changed(prices_list)
        increased = price_increased(prices_list)
        if decreased:
            decrease = prices_list[-1] - prices_list[-2]
            message = f"Price decreased buy now MF decreased by € {decrease} jaja."
            print(f"Price decreased buy now MF decreased by € {decrease} jaja.")
            Scream()
        if no_changes:
            message = f"Price Not changed"
            print(f"{message} it is still € {prices_list[-1]}")
            Silence()
            
        if increased:
            increase = prices_list[-1] - prices_list[-2]
            print(f"Price increased Kanker gayyy € {increase} NOOOO")
            Sad()


    time.sleep(30)
    count += 1
