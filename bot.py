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
        f"**𝗛𝗘𝗟𝗟𝗢🎈{message.chat.first_name}!**\n\n"
        "𝗜'𝗺 𝕾𝖍𝖗𝖙𝖋𝖑𝖞 𝕿𝖍𝖎𝖘 𝕭𝖔𝖙 𝕴𝖘 𝕸𝖆𝖉𝖊 𝕭𝖞 @𝖙𝖗𝖛𝖕𝖓 𝕬𝖉𝖒𝖎𝖓𝖘.\n\n 𝕿𝖍𝖎𝖘 𝕭𝖔𝖙 𝖎𝖘 𝕸𝖆𝖉𝖊 𝕱𝖔𝖗 𝕺𝖚𝖗 𝕻𝖊𝖗𝖘𝖔𝖓𝖆𝖑 𝖀𝖘𝖊 \n\n ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝕸𝖔𝖛𝖎𝖊 𝕮𝖍𝖆𝖓𝖓𝖊𝖑', url='https://t.me/trvpn')
                ],
                [
                    InlineKeyboardButton('𝕲-𝕯𝖗𝖎𝖛𝖊 𝕸𝖔𝖛𝖎𝖊 𝕮𝖍𝖆𝖓𝖓𝖊𝖑', url='https://t.me/tamilblasters_win')
                ]
            ]
        )
    )


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'Here is your👉 [𝕾𝖍𝖔𝖗𝖙𝖋𝖑𝖞 𝖑𝖎𝖓𝖐🎈]({short_link}) \n\n 𝖄𝖔𝖚𝖗 𝕾𝖍𝖔𝖗𝖙𝖋𝖑𝖞 𝖑𝖎𝖓𝖐 = {short_link} \n\n 𝔒𝔲𝔯 𝔗𝔢𝔩𝔢𝔤𝔯𝔞𝔪 ℭ𝔥𝔞𝔫𝔫𝔢𝔩 ', quote=True,reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝕸𝖔𝖛𝖎𝖊 𝕮𝖍𝖆𝖓𝖓𝖊𝖑', url='https://t.me/trvpn'),
                    InlineKeyboardButton('Your Shorten Link', url=short_link)
                ],
                [
                    InlineKeyboardButton('𝕲-𝕯𝖗𝖎𝖛𝖊 𝕸𝖔𝖛𝖎𝖊 𝕮𝖍𝖆𝖓𝖓𝖊𝖑', url='https://t.me/tamilblasters_win')
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
