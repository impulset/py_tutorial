from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import filters

from aiogram.utils.markdown import hbold, bold, text, link
from aiogram.types import ChatType, ParseMode, ContentTypes

bot = Bot('BOT_TOKEN')
dp = Dispatcher(bot)

#Make style 
@dp.message_handler(filters.Text(startswith=['/menu']))
async def on_message(message: types.Message):
    await bot.send_message(message.chat.id, '<b>Example message</b>', parse_mode=ParseMode.HTML)

#Message filtering by message ond ID
@dp.message_handler(filters.Text(startswith=['/menu']),
                    filters.builtin.IDFilter(user_id=["user1","user2"]))  
async def on_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Example message')  


