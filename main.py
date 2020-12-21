import requests
import colorama
import os
from colorama import Fore

def SlayWH(url):
    payload = {
        "content": 'WebhookSlayer slayed your webhook!'
    }
    for x in range(15):
        requests.post(url, json=payload)

    requests.delete(url, json=payload)
    
    print('Slayed Webhook!')
    exit(0)

def SpamWH(url):
    payload = {
        "content": 'WebhookSlayer slayed your webhook!'
    }
    try:
        while True:
            requests.post(url, json=payload)
    except KeyboardInterrupt:
        print('Spammer has been stopped!')
    
def deleteWH(url):
    requests.delete(url)
    print("Deleted Webhook!")
    exit(0)
    

b = Fore.BLUE
r = Fore.RED

intro = f"""
  {b}╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═{r}╔═╗╦  ╔═╗╦ ╦╔═╗╦═╗
  {b}║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗{r}╚═╗║  ╠═╣╚╦╝║╣ ╠╦╝
  {b}╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩{r}╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═
  {b}[1]{r} Slay Webhook
  {b}[2]{r} Spam Webhook
  {b}[3]{r} Delete Webhook
  {b}[4]{r} Exit
"""

os.system('clear')
print(intro)
optionx = input("Option: ")
if optionx == '1':
    try:
        webhookurl = input("Webhook URL: ")
        src = requests.get(webhookurl)
        if src.status_code == 200:
            print("Slaying Webhook..")
            SlayWH(webhookurl)
        else:
            print('Invalid webhook.')
            exit(0)
    except Exception:
        print('Invalid link.')
elif optionx == '2':
    try:
        webhookurl = input("Webhook URL: ")
        src = requests.get(webhookurl)
        if src.status_code == 200:
            print("Spamming Webhook..")
            SpamWH(webhookurl)
        else:
            print('Invalid webhook.')
            exit(0)
    except Exception:
        print('Invalid link.')
elif optionx == '3':
    try:
        webhookurl = input("Webhook URL: ")
        src = requests.get(webhookurl)
        if src.status_code == 200:
            print("Deleting Webhook..")
            deleteWH(webhookurl)
        else:
            print('Invalid webhook.')
            exit(0)
    except Exception:
        print('Invalid link.')
elif optionx == '4':
    print('Exiting..')
    exit(0)
else:
    print('Invalid option, please select a valid option.')
