import logging
from VCPlayBot.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from VCPlayBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "Mᴜsɪᴄ ɢʀᴏᴜᴘ", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        " Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://{SUPPORT_GROUP}")
                    InlineKeyboardButton(
                           "Dᴇᴠ✨", url=f"https://t.me/Ok_bie_Bot")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = 'Mᴜsɪᴄ ɢʀᴏᴜᴘ', url=f"https://t.me/{UPDATES_CHANNEL}"),
             [InlineKeyboardButton(text = 'Sᴜᴘᴘᴏʀᴛ', url=f"https://t.me/{SUPPORT_GROUP}")],
            [InlineKeyboardButton(text = 'Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ', url=f"https://t.me/{SUPPORT_GROUP}")],
             [InlineKeyboardButton(text = 'Dᴇᴠ✨', url=f"https://t.me/Ok_bie_Bot")],
            [InlineKeyboardButton(text = ''«', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '<', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '>', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hello there! I can play music in the voice chats of telegram groups & channels.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Click Here For Help", url=f"https://t.me/{BOT_USERNAME}?start"
                    )
                ]
            ]
        ),
    )

