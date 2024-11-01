from notifier_botty import login_to_chegg, refresh_chegg, telegram_bot_sendtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
import pytz
import requests
import multiprocessing


# Account credentials (you can add more accounts here)
accounts = [
    {"username": "nrama1219@gmail.com", "password": "Bujji@56789", "user_bot_chatID": '809899065', "account_name": "ramu", "user_bot_token" : "7716677970:AAHMAtvPRlzr4Iu3Ob0cNF9LVQ1-YhOmrq0"},
    {"username": "takeadpay@gmail.com", "password": "Mail@202", "user_bot_chatID": '7091969636', "account_name": "pusph", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "sakshichoudharysak31@gmail.com", "password": "ihsk@S#31", "user_bot_chatID": '1125920838', "account_name": "Avnish", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "ahmadme8299@gmail.com", "password": "Kala8299@", "user_bot_chatID": '1879499039', "account_name": "Umeed", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "shaurya875875@gmail.com", "password": "Chegg@123", "user_bot_chatID": '1505060701', "account_name": "Physics", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "irfaa3553@gmail.com", "password": "Chegg@00", "user_bot_chatID": '1505060701', "account_name": "Alam", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "mohammadshahfaisal07@gmail.com", "password": "Faisal@07", "user_bot_chatID": '1505060701', "account_name": "Faizan", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},

    # Add more accounts if necessary
]

accept_option = True
start_time = 0  # Starting time. Default 0. In 24-hour format
end_time = 25  # Ending time. Default 25. In 24-hour format


def refresh_account(account):
    username = account["username"]
    password = account["password"]
    user_bot_chatID = account["user_bot_chatID"]
    account_name = account["account_name"]
    user_bot_token = account["user_bot_token"]  # Same token for all accounts

    # Set up Chrome WebDriver for this account
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Each account gets its own Chrome instance
    driver = webdriver.Chrome(options=options)

    # Attempt to log in
    flag_login = True
    while flag_login:
        flag_login = login_to_chegg(username, password, driver)


    # Start refreshing for the account
    refresh_chegg(driver, accept_option, start_time, end_time, user_bot_token, user_bot_chatID, account_name)
   


if __name__ == "__main__":
    # Create a process for each account
    processes = []
    for account in accounts:
        process = multiprocessing.Process(target=refresh_account, args=(account,))
        processes.append(process)
        process.start()

    # Optionally join the processes to ensure the script waits for all to finish (though in infinite loops, this won't happen)
    for process in processes:
        process.join()
