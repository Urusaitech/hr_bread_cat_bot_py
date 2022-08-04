import bread_cat_bot
import requests
from config import bot_token


def second_state(chat_id):
    first = input('У него есть уши?\n')
    if first in bread_cat_bot.replies_no:
        response_no1 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Это кот, а не хлеб! Не ешь его!'}
        ).json()
        print('Это кот, а не хлеб! Не ешь его!')
    elif first in bread_cat_bot.replies_yes:
        response_yes1 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Это хлеб, а не кот! Ешь его!'}
        ).json()
        print('Это хлеб, а не кот! Ешь его!')

    else:
        print('wrong reply')


def first_state(chat_id):
    first = input('Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?\n')
    if first in bread_cat_bot.replies_no:
        response_no0 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Это кот, а не хлеб! Не ешь его!'}
        ).json()
        print('Это кот, а не хлеб! Не ешь его!')
        return
    elif first in bread_cat_bot.replies_yes:
        response_yes0 = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'У него есть уши?'}
        ).json()

        second_state(chat_id)
    else:
        print('wrong')


def api():
    try:
        chat_id = int(input('enter your chat id with the bot:\n'))
        response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
            data={'chat_id': chat_id, 'text': 'Привет! Я помогу отличить кота от хлеба! Объект перед тобой '
                                              'квадратный?'}
        ).json()

        first_state(chat_id)
    except ValueError:
        print('Your id must be a number')
    except Exception as e:
        print(e)


api()
