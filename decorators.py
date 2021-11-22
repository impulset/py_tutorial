#simple decorator
def if_user_exists(func):
    async def wrapper(message):
        if 5 > 4:
            return await func(message)
        else:
            await bot.send_message(message.chat.id, "You don't have permissions")    
    return wrapper        

@if_user_exists()
async def on_message(message):
    await message.reply('Menu button added')



#decorator with arguments
bot = "bot"
def if_user_exists(bot):
    def decorator(func):
        async def wrapper(message):
            if 5 > 4:
                return await func(message)
            else:
                await bot.send_message(message.chat.id, "You don't have permissions")    
        return wrapper        
    return decorator

@if_user_exists(bot)
async def on_message(message):
    await message.reply('Menu button added') 