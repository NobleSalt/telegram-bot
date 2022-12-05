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

# get_message_text = lambda update: update['message']['text']

def get_message_text(update):
    message = update.get('message')
    return message.get('text')

def last_update(req):
    response = requests.get(req + 'getUpdates').json()
    result=response['result']
    # print("response",response)
    # print("result",result)
    return result[len(result) - 1]

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
        msg = get_message_text(update).lower()
        if update_id == update['update_id']:
            if str(msg).startswith('/'):
                if msg == "/hi" or msg == "/hello" or msg == "/start":
                    chat = update
                    message = chat.get('message')
                    user_chat = message.get('chat')
                    first_name = user_chat.get('first_name')
                    print("user_chat", user_chat)
                    # print("get_chat_id(update)",update)
                    send_message(get_chat_id(chat), f"Hello {first_name or 'User'} , Welcome to our bot. Type '/play' to roll the dice !")
                elif msg == "/play":
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
