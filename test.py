from telethon import events

import bread_cat_bot
import config
from telethon.sync import TelegramClient

bot = TelegramClient('bot', config.api_id, config.api_hash).start(bot_token=config.bot_token)


async def main():
    await bot.send_message('urusaitech', f'Я распознаю только {bread_cat_bot.replies_yes + bread_cat_bot.replies_no}')

    @bot.on(events.NewMessage(chats='chat_name'))
    async def normal_handler(event):
        # print(event.message)
        print(event.message.to_dict()['message'])


with bot:
    bot.loop.run_until_complete(main())
