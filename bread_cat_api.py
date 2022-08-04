import bread_cat_bot
import requests
from config import bot_token

def second_state(chat_id):
    first = input('У него есть уши?')
    if first in bread_cat_bot.replies_no:
        response_no1 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Это кот, а не хлеб! Не ешь его!'}
        ).json()
        print(response_no1)
    elif first in bread_cat_bot.replies_yes:
        response_yes1 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Это хлеб, а не кот! Ешь его!'}
        ).json()
        print(response_yes1)

    else:
        print('wrong reply')


def first_state(chat_id):
    first = input('Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?')
    if first in bread_cat_bot.replies_no:
        response_no0 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Это кот, а не хлеб! Не ешь его!'}
        ).json()
        print(response_no0)
        return
    elif first in bread_cat_bot.replies_yes:
        response_yes0 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'У него есть уши?'}
        ).json()
        print(response_yes0)
        second_state(chat_id)
    else:
        print('wrong')


def api():
    try:
        chat_id = int(input('enter your chat id with the bot:\n'))
        response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?'}
        ).json()
        print(response)
        first_state(chat_id)
    except ValueError:
        print('Your id must be a number')
    except Exception as e:
        print(e)


api()
