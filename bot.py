import requests
import random
from decouple import config
# from telegram.ext import commandhandler
token = config('token')
url = f"https://api.telegram.org/bot{token}/"
print(token)

def handle_hi(bot, update):

    return 0

get_chat_id = lambda update: update['message']['chat']['id']

get_message_text = lambda update: update['message']['text']

last_update = lambda req: requests.get(req + 'getUpdates').json()['result'][len(requests.get(req + 'getUpdates').json()['result']) - 1]

def send_message(chat_id, message_text):
    params = {"chat_id":chat_id, "text": message_text}
    return requests.post(url + "sendMessage", data=params)

# commandhandler.CommandHandler('hi', handle_hi)
def main():
    # update = last_update(url)
    # send_message()
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello":
                send_message(get_chat_id(update), "Hello Welcome to our bot. Type 'play' to roll the dice !")
            elif get_message_text(update).lower() == "play":
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                _3 = random.randint(1, 6)
                send_message(get_chat_id(update), f"You have {str(_1)} and {str(_2)} and {str(_3)} \n Your result is {str(_1 + _2 + _3)} !!!")
            else:
                send_message(get_chat_id(update), "Sorry I Don't Understand What You Have Typed")
            update_id += 1

# call the function to make it apply
if __name__ == "__main__":
    # print(locals())
    print("Running Bot !")
    main()
