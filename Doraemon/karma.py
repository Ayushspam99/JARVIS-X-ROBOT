

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from JARVISROBO import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT, BOT_NAME

# <============================================== CONSTANTS =========================================================>
STATS_IMG = [
    "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",
]
START_IMG = [
    "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",
    "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",
    "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",
]

HEY_IMG = "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg"

ALIVE_ANIMATION = [
     "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",
     "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",
]

FIRST_PART_TEXT = "*KAISA HAIN * `{}` , 🥀 . . ."

PM_START_TEXT = """
*๏ ᴛʜɪs ɪs* ˹ĐʀᴀɢᴏƝ˼ !
➻ ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs✨

──────────────────
*๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.*
"""

START_BTN = [
   [
        InlineKeyboardButton(
            text="✧ ᴀᴅᴅ ᴍᴇ ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
   [
        InlineKeyboardButton(text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="❄ ᴀʙᴏᴜᴛ ❄", callback_data="Jarvis_"),
        InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=f"https://t.me/ll_DRAGON_XD_SUPPORT_ll"),
    ],
   [
        InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="☁️ sᴏᴜʀᴄᴇ ☁️", callback_data="git_source"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="✧ ᴀᴅᴅ ᴍᴇ ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=f"https://t.me/ll_DRAGON_XD_SUPPORT_ll"),
        InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="sᴜᴩᴩᴏʀᴛ", url="https://t.me/ll_DRAGON_XD_SUPPORT_ll"),
        ib(text="sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/ll_DRAGON_XD_SUPPORT_ll"),
    ],
    [
        ib(
            text="✧ ᴀᴅᴅ ᴍᴇ ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = f"""
*» ᴊᴀʀᴠɪs ᴇxᴄʟᴜsɪᴠᴇ ꜰᴇᴀᴛᴜʀᴇs*

ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ꜱᴇᴄᴛɪᴏɴ.
 ‣ ɪɴ ᴘᴍ : ᴡɪʟʟ ꜱᴇɴᴅ ʏᴏᴜ ʜᴇʟᴘ​ ꜰᴏʀ ᴀʟʟ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇꜱ.
 ‣ ɪɴ ɢʀᴏᴜᴘ : ᴡɪʟʟ ʀᴇᴅɪʀᴇᴄᴛ ʏᴏᴜ ᴛᴏ ᴘᴍ, ᴡɪᴛʜ ᴀʟʟ ᴛʜᴀᴛ ʜᴇʟᴘ​ ᴍᴏᴅᴜʟᴇꜱ.
 """
