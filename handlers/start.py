from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
I am ๐๐ผ๐๐ฒ๐ฟ๐ ๐๐๐ถ๐ฐ๐๐ผ๐ VC Music Player, an open-source bot that lets you play music in your Telegram groups.
For source code Join our support group @LoverMusicSupport.
/help to know my commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Supportโก๏ธ", url="https://t.me/LoverMusicSupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Creatorโก๏ธ", url="https://t.me/SarcasticLucky"
                    )
                    InlineKeyboardButton(
                        "Study Groupโก๏ธ", url="https://t.me/Class_9th_10th"
                    )

                ],
                [
                    InlineKeyboardButton(
                        "Add To Your Groupโก๏ธ", url="https://t.me/LoverMusicBot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "๐๐ปโโ๏ธ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No โ", callback_data="close"
                    )
                ]
            ]
        )
    )
