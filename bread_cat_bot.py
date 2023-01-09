import asyncio
import logging
import config

from aiogram import Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# detected bot commands 
replies_yes = ('конечно', 'ага', 'пожалуй', 'да')
replies_no = ('нет, конечно', 'ноуп', 'найн', 'нет')


# this class sets up bot's state after the command is detected
class DetectObject(StatesGroup):
    waiting_for_answer1 = State()
    waiting_for_answer2 = State()


async def bot_start(message: types.Message):
    print(message)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Да', 'Нет')
    await message.answer('Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?',
                         reply_markup=keyboard)
    await DetectObject.waiting_for_answer1.set()


async def first_state(message: types.Message, state: FSMContext):
    if message.text.lower() not in replies_yes + replies_no:
        await message.answer(f'Я распознаю только {replies_yes + replies_no}')
        return
    await state.update_data(first_choice=message.text.lower())
    if message.text.lower() in replies_no:
        await message.answer('Это кот, а не хлеб! Не ешь его!', reply_markup=types.ReplyKeyboardRemove())
        return
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Да', 'Нет')
    await DetectObject.next()
    await message.answer('У него есть уши?', reply_markup=keyboard)


async def second_state(message: types.Message, state: FSMContext):
    if message.text.lower() not in replies_yes + replies_no:
        await message.answer(f'Я распознаю только {replies_yes + replies_no}')
        return
    if message.text.lower() in replies_no:
        await message.answer('Это хлеб, а не кот! Ешь его!', reply_markup=types.ReplyKeyboardRemove())
        return
    user_data = await state.get_data()
    await message.answer(f'Это кот, а не хлеб! Не ешь его!', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


# this func launches bot's functionality in telegram
def register_handlers_state(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start', state='*')
    dp.register_message_handler(first_state, state=DetectObject.waiting_for_answer1)
    dp.register_message_handler(second_state, state=DetectObject.waiting_for_answer2)

# logger, TODO: wrap in func 
logger = logging.getLogger(__name__)


async def main():
    # remove '#' for logs in stdout
    # logging.basicConfig(
    #    level=logging.INFO,
    #    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    # )
    # logger.error('Starting bot')

    bot = Bot(token=config.bot_token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_state(dp)

    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())

