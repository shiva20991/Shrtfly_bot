from os import environ
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', '9cb4bd5502494531ca397429e90209097c51b4a8')

bot = Client('Shrtfly_bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**ððððð¢ð{message.chat.first_name}!**\n\n"
        "ð'ðº ð¾ðððððð ð¿ððð ð­ðð ð´ð ð¸ððð ð­ð @ððððð ð¬ððððð.\n\n ð¿ððð ð­ðð ðð ð¸ððð ð±ðð ðºðð ð»ððððððð ððð \n\n ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ð¸ðððð ð®ðððððð', url='https://t.me/trvpn')
                ],
                [
                    InlineKeyboardButton('ð²-ð¯ðððð ð¸ðððð ð®ðððððð', url='https://t.me/tamilblasters_win')
                ]
            ]
        )
    )


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'Here is yourð [ð¾ððððððð ððððð]({short_link}) \n\n ðððð ð¾ððððððð ðððð = {short_link} \n\n ðð²ð¯ ðð¢ð©ð¢ð¤ð¯ððª â­ð¥ðð«ð«ð¢ð© ', quote=True,reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ð¸ðððð ð®ðððððð', url='https://t.me/trvpn'),
                    InlineKeyboardButton('Your Shorten Link', url=short_link)
                ],
                [
                    InlineKeyboardButton('ð²-ð¯ðððð ð¸ðððð ð®ðððððð', url='https://t.me/tamilblasters_win')
                ]
            ]
        )
    )
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://dulink.in/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
